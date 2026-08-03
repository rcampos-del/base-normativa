#!/usr/bin/env python3
"""
camadas.py — mostra as redações empilhadas de um dispositivo e o que cada uma é.

PARA QUE SERVE. As páginas do Planalto empilham as redações sucessivas de cada
artigo: a superada primeiro, a vigente depois. Na página, a superada aparece
TACHADA; no texto puro, o tachado não sobrevive. Este programa devolve o atalho
sem tocar no texto — lê o mesmo arquivo do acervo e separa as camadas.

O QUE NÃO FAZ. Não decide vigência. Devolve as notas oficiais de cada camada e
uma LEITURA SUGERIDA, que é hipótese a conferir, nunca conclusão. Três coisas
que o tachado confunde e que aqui ficam separadas:

  REDAÇÃO SUPERADA  o dispositivo VIGE, com outra redação
  REVOGADO          o dispositivo não existe mais
  SEM EFICÁCIA      versão de medida provisória que nunca vigeu

Medido em 03/08/2026 na página da Lei 9.430: das 59 notas "(Revogado pela ...)",
32 estavam FORA do tachado. O tachado nunca foi o marcador; a nota é.

USO
    python3 camadas.py LEI-9430-1996.txt 2        # as camadas do art. 2º
    python3 camadas.py LEI-9430-1996.txt 2 -v     # com o texto de cada camada
    python3 camadas.py LEI-9430-1996.txt          # auditoria do arquivo
    python3 camadas.py --acervo                   # auditoria de todo o acervo
"""
import re, sys, os, glob

RAIZ = os.path.dirname(os.path.abspath(__file__))

# Início de artigo. Aceita as três grafias do ordinal (º, °, o) e o artigo com
# letra (9º-A). Não casa depois de '(' nem de palavra, para não apanhar remissão
# ("nos termos do art. 15"). Mesma cautela do normalizar.py.
ART = re.compile(
    r'(?<![\(\w\-àâãáéêíóôõúçÀÂÃÁÉÊÍÓÔÕÚÇ])'
    r'Art\.\s*(\d+)\s*(?:[ºo°]\s*)?(-[A-Z])?'
    r'(?=[\.\s])')

NOTA = re.compile(r'\(([^()]{3,90})\)')

CLASSES = [
    ('Revogad',        'REVOGADO'),
    ('Sem eficácia',   'SEM EFICÁCIA'),
    ('Redação dada',   'REDAÇÃO DADA'),
    ('Incluíd',        'INCLUÍDO'),
    ('Renumerado',     'RENUMERADO'),
]


def notas(trecho):
    """Notas oficiais do CAPUT da camada, na ordem em que aparecem.

    Lê só a primeira linha do trecho — o caput. Sem esse corte, as notas dos
    parágrafos e incisos entram na conta e falseiam o veredito: no ensaio de
    03/08/2026 o art. 44 da Lei 9.430, que VIGE, saiu como revogado, porque
    incisos seus foram revogados em 2007. Instrumento provado depois do corte.
    """
    uteis = ('Redação dada', 'Incluíd', 'Revogad', 'Sem eficácia', 'Vigência',
             'Vide', 'Produção de efeito', 'Regulamento', 'Renumerado', 'VETADO')
    caput = trecho.split('\n')[0]
    return [n.strip() for n in NOTA.findall(caput)
            if any(u in n for u in uteis)]


def classificar(ns):
    for chave, rotulo in CLASSES:
        if any(chave in n for n in ns):
            return rotulo
    return 'REDAÇÃO ORIGINÁRIA'


def citacao(trecho, antes=''):
    """Bloco de alteração de OUTRA lei — não é camada deste artigo.

    Três sinais, medidos em 03/08/2026: a reticência do Planalto no trecho
    omitido ('Art. 41. .........'), o fecho '(NR)' do artigo reescrito, e a
    aspa de abertura imediatamente anterior. Sem estes cortes a LC 214 devolvia
    25 falsos empilhamentos — são os arts. 490 a 520, que reescrevem artigos de
    outras leis e os transcrevem por inteiro."""
    cabeca = trecho[:2500]
    if re.search(r'\.{6,}', trecho[:200]):
        return True
    if '(NR)' in cabeca:
        return True
    if antes.rstrip()[-1:] in ('\u201c', '"'):
        return True
    return len(trecho.strip()) < 60


def fatiar(texto):
    """Devolve [(numero, sufixo, trecho)] na ordem do arquivo."""
    marcas = [(m.start(), m.group(1), m.group(2) or '') for m in ART.finditer(texto)]
    saida = []
    for i, (pos, num, suf) in enumerate(marcas):
        fim = marcas[i + 1][0] if i + 1 < len(marcas) else len(texto)
        saida.append((num, suf, texto[pos:fim], texto[max(0, pos - 40):pos]))
    return saida


def camadas_de(texto, alvo, sufixo=''):
    return [(t, notas(t)) for n, s, t, a in fatiar(texto)
            if n == str(alvo) and s == sufixo and not citacao(t, a)]


def mostrar(arquivo, alvo, verboso=False):
    texto = open(arquivo, encoding='utf-8').read()
    alvo = str(alvo)
    sufixo = ''
    if '-' in alvo:
        alvo, sufixo = alvo.split('-')[0], '-' + alvo.split('-')[1].upper()
    cam = camadas_de(texto, alvo, sufixo)
    if not cam:
        print(f'art. {alvo}{sufixo}: não encontrado em {os.path.basename(arquivo)}.')
        print('   (pode estar dentro de bloco de alteração de outra lei — '
              'confira com grep antes de concluir que falta)')
        return
    print(f'\n{os.path.basename(arquivo)} — art. {alvo}{sufixo}: '
          f'{len(cam)} camada(s)\n')
    for i, (trecho, ns) in enumerate(cam, 1):
        classe = classificar(ns)
        print(f'  [{i}/{len(cam)}] {classe}')
        print(f'        notas: {"; ".join(ns) if ns else "— nenhuma —"}')
        corpo = re.sub(r'\s+', ' ', trecho).strip()
        print(f'        {corpo[:160] if not verboso else corpo}'
              f'{"..." if not verboso and len(corpo) > 160 else ""}')
        print()
    vivas = [(i, c) for i, (t, n) in enumerate(cam, 1)
             if (c := classificar(n)) != 'SEM EFICÁCIA']
    if not vivas:
        print('  LEITURA SUGERIDA: nenhuma camada com eficácia. CONFERIR.')
    else:
        i, c = vivas[-1]
        if c == 'REVOGADO':
            print(f'  LEITURA SUGERIDA: dispositivo REVOGADO — a última camada '
                  f'({i}) traz nota de revogação.')
        else:
            print(f'  LEITURA SUGERIDA: vige a camada {i} ({c}).')
    print('  Isto é hipótese, não conclusão: ler o artigo inteiro e, havendo '
          'remissão a lei\n  com efeitos diferidos, ir à lei alteradora.\n')


def auditar(arquivo):
    texto = open(arquivo, encoding='utf-8').read()
    grupos = {}
    for n, s, t, a in fatiar(texto):
        if citacao(t, a):
            continue
        grupos.setdefault(n + s, []).append(notas(t))
    empilhados = {k: v for k, v in grupos.items() if len(v) > 1}
    duvidosos = []
    for k, vs in empilhados.items():
        classes = [classificar(n) for n in vs]
        vivas = [c for c in classes if c != 'SEM EFICÁCIA']
        if not vivas or vivas[-1] == 'REDAÇÃO ORIGINÁRIA':
            duvidosos.append(k)
    return len(grupos), len(empilhados), duvidosos


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a != '-v']
    verboso = '-v' in sys.argv
    if args and args[0] == '--acervo':
        print(f'{"arquivo":<32} {"disp.":>6} {"empilhados":>11} {"a conferir":>11}')
        tot_e = tot_d = 0
        for p in sorted(glob.glob(os.path.join(RAIZ, '*.txt'))):
            g, e, d = auditar(p)
            tot_e += e; tot_d += len(d)
            print(f'{os.path.basename(p):<32} {g:>6} {e:>11} {len(d):>11}')
        print(f'\nACERVO: {tot_e} dispositivos com redação empilhada; '
              f'{tot_d} em que a última camada não traz nota — estes pedem olho.')
    elif len(args) == 1:
        g, e, d = auditar(args[0])
        print(f'{os.path.basename(args[0])}: {g} dispositivos, '
              f'{e} com redação empilhada.')
        if d:
            print('A conferir (última camada sem nota): ' + ', '.join(sorted(d, key=lambda x: int(re.match(r"\d+", x).group()))))
    elif len(args) == 2:
        mostrar(args[0], args[1], verboso)
    else:
        print(__doc__)
