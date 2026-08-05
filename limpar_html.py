#!/usr/bin/env python3
"""
limpar_html.py — converte a PÁGINA HTML SALVA de norma oficial em texto puro.

POR QUE EXISTE. Até 04/08/2026 o acervo se erguia de PDF de impressão da página
oficial. O caminho tem dois defeitos: leis com anexo extenso geram PDF de
centenas de páginas, que o canal de envio recusa (foi o caso da Lei 12.546, com
os anexos de NCM na página-base); e o PDF descarta a marcação, que é onde vive a
distinção entre redação vigente e superada. A página salva em HTML não tem
nenhum dos dois problemas.

O QUE FAZ. Descarta script, estilo e comentário; converte os elementos de bloco
em quebra de linha; remove a marcação restante; resolve as entidades HTML; e
normaliza o espaço em branco. O texto normativo não é tocado.

O QUE NÃO FAZ. Não decide vigência. O tachado do Planalto é medido e RELATADO,
mas não vira marca no texto — a distinção entre redação superada, dispositivo
revogado e versão sem eficácia lê-se pela nota entre parênteses, que sobrevive
inteira. Ver `camadas.py`.

A SAÍDA AINDA PASSA PELO `normalizar.py`, como no caminho do PDF.

USO
    python3 limpar_html.py L12546compilado.html bruto.txt
"""
import html as _html
import re
import sys
import unicodedata

# Blocos que valem quebra de linha. `p` e `br` fazem o grosso do serviço nas
# páginas do Planalto, que são FrontPage antigo.
BLOCOS = ('p', 'br', 'div', 'tr', 'td', 'th', 'li', 'ul', 'ol', 'dd', 'dt',
          'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'blockquote', 'hr')

PAL = re.compile(r'[0-9A-Za-zÀ-ÿ]+')


def ler(caminho):
    """Lê respeitando o charset declarado na própria página."""
    cru = open(caminho, 'rb').read()
    m = re.search(rb'charset=["\']?([\w-]+)', cru[:4000], re.I)
    cod = m.group(1).decode('ascii').lower() if m else 'utf-8'
    if cod in ('windows-1252', 'cp1252', 'iso-8859-1', 'latin-1', 'latin1'):
        cod = 'cp1252'
    return cru.decode(cod, errors='replace'), cod


def medir_tachado(h):
    """Diagnóstico, não intervenção: quanto da página é redação superada."""
    faixas = []
    for m in re.finditer(r'(?is)<strike[^>]*>.*?</strike>', h):
        faixas.append((m.start(), m.end()))
    for m in re.finditer(r'(?is)<(\w+)[^>]*line-through[^>]*>.*?</\1>', h):
        faixas.append((m.start(), m.end()))
    faixas.sort()
    uniao, ini, fim = [], None, None
    for a, b in faixas:
        if ini is None:
            ini, fim = a, b
        elif a <= fim:
            fim = max(fim, b)
        else:
            uniao.append((ini, fim))
            ini, fim = a, b
    if ini is not None:
        uniao.append((ini, fim))
    pal = sum(len(PAL.findall(_html.unescape(re.sub(r'(?s)<[^>]+>', ' ', h[a:b]))))
              for a, b in uniao)
    return len(uniao), pal


# Páginas do Diário Oficial (in.gov.br) vêm embrulhadas em portal: menu,
# rodapé, redes sociais. O texto da matéria mora em <div class="texto-dou">,
# precedido do cabeçalho <div class="cabecalho-dou">. Recorta-se o miolo antes
# de converter — do contrário entram 200 linhas de navegação no acervo.
def recortar_dou(h):
    ini = re.search(r'<div[^>]*class="[^"]*cabecalho-dou[^"]*"', h, re.I)
    if not ini:
        ini = re.search(r'<div[^>]*class="[^"]*texto-dou[^"]*"', h, re.I)
    if not ini:
        return h, False
    fim = re.search(r'(?is)<(footer|div[^>]*class="[^"]*rodape)', h[ini.start():])
    corte = ini.start() + (fim.start() if fim else len(h) - ini.start())
    return h[ini.start():corte], True


def converter(h):
    contas = {}

    def some(padrao, rotulo, repo=' '):
        nonlocal h
        h, n = re.subn(padrao, repo, h)
        if n:
            contas[rotulo] = contas.get(rotulo, 0) + n

    h, dou = recortar_dou(h)
    if dou:
        contas['miolo do DOU recortado'] = 1
    some(r'(?is)<head[^>]*>.*?</head>', 'cabeçalho do documento descartado')
    some(r'(?is)<script[^>]*>.*?</script>', 'script descartado')
    some(r'(?is)<style[^>]*>.*?</style>', 'estilo descartado')
    some(r'(?s)<!--.*?-->', 'comentário descartado')

    for t in BLOCOS:
        some(rf'(?is)</?{t}(\s[^>]*)?/?>', f'<{t}> vira quebra', '\n')

    # ANTES da remoção geral: marcação que carrega margem de estilo separa
    # palavras VISUALMENTE, sem espaço no texto. Na Emenda Constitucional 132 o
    # Planalto escreve `do<strong style="margin-left:4px">caput</strong>deste`,
    # e removê-la sem espaço produzia `docaputdeste`. Medido em 04/08/2026.
    some(r'(?is)<[a-z]+[^>]*margin-(?:left|right)[^>]*>', 'marcação com margem -> espaço', ' ')

    # Marcação restante — sobretudo `sup`, `font`, `span`, `a`, `u`, `strike` —
    # sai SEM espaço no lugar: no Planalto ela cai DENTRO da palavra. O ensaio
    # de 04/08/2026 mostrou o preço de errar isso: trocando por espaço, `1º`
    # virava `1 o` (226 vezes) e `Sem eficácia` virava `S em eficácia`.
    some(r'(?s)<[^>]+>', 'marcação restante removida', '')

    h = _html.unescape(h)
    h = h.replace('\xa0', ' ').replace('\u200b', '')
    h = unicodedata.normalize('NFC', h)

    linhas = []
    for l in h.split('\n'):
        l = re.sub(r'[ \t\r\f\v]+', ' ', l).strip()
        if l:
            linhas.append(l)
    return '\n'.join(linhas) + '\n', contas


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    origem, destino = sys.argv[1], sys.argv[2]
    bruto, cod = ler(origem)
    blocos, pal_tach = medir_tachado(bruto)
    texto, contas = converter(bruto)
    open(destino, 'w', encoding='utf-8').write(texto)

    total = len(PAL.findall(texto))
    print(f'{origem} -> {destino}   [charset da página: {cod}]')
    for k, v in contas.items():
        print(f'   {k:<34} {v:>7}')
    print(f'   {"linhas":<34} {len(texto.splitlines()):>7}')
    print(f'   {"palavras":<34} {total:>7,}')
    print(f'   {"blocos tachados na página":<34} {blocos:>7}'
          f'   ({pal_tach:,} palavras — redação superada, NÃO marcada no texto)')
