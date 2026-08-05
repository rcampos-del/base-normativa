#!/usr/bin/env python3
"""
validar.py — confere a integridade do acervo e varre dado pessoal.

O que faz: para cada .txt do repositório, recalcula o SHA-256 e compara com o
registrado no MANIFESTO.md. Acusa arquivo alterado, arquivo sem registro e
registro sem arquivo. Em seguida varre o acervo em busca de dado pessoal.

POR QUE A VARREDURA. As páginas do portal da SEFAZ-RJ, quando salvas com sessão
aberta, trazem no cabeçalho o nome e o CPF do usuário logado. O `limpar_html.py`
descarta esse bloco por recortar o `<main>`, e a varredura de 05/08/2026 sobre os
60 arquivos não achou nenhum CPF. Mas instrumento que confia na boa execução de
outro instrumento é instrumento frágil: o repositório é PÚBLICO, e o custo de um
CPF publicado não é simétrico ao custo de uma conferência a mais.

CPF e vestígio de sessão REPROVAM. CNPJ e e-mail apenas se RELATAM: há CNPJ
dentro do texto normativo — o Anexo XIII traz um em exemplo de escrituração e o
Anexo Único da Resolução 875 traz três em ementas de atos concessivos. Apagá-los
corromperia a norma.

Por que assim: a versão anterior procurava originais em 'fontes/*/*.html', pasta
que não existe no repositório — encontrava zero arquivos e retornava "tudo certo"
sem conferir nada. Falsa segurança. Esta versão valida o que de fato está aqui.
"""
import re, glob, hashlib, sys, os

RAIZ = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.join(RAIZ, "MANIFESTO.md")

if not os.path.exists(MAN):
    print("!! MANIFESTO.md não encontrado."); sys.exit(1)

registrado = {}
for linha in open(MAN, encoding="utf-8"):
    arq = re.search(r"`([^`]+\.txt)`", linha)
    shas = re.findall(r"`([0-9a-f]{12})`", linha)
    if arq and shas:
        registrado[arq.group(1)] = shas[-1]

presentes = {os.path.basename(p) for p in glob.glob(os.path.join(RAIZ, "*.txt"))}
falhas = 0

for arq in sorted(presentes | set(registrado)):
    caminho = os.path.join(RAIZ, arq)
    if arq not in registrado:
        print(f"  [!!] {arq:<34} presente, mas SEM registro no MANIFESTO"); falhas += 1; continue
    if arq not in presentes:
        print(f"  [!!] {arq:<34} registrado, mas AUSENTE do repositório"); falhas += 1; continue
    real = hashlib.sha256(open(caminho, "rb").read()).hexdigest()[:12]
    if real == registrado[arq]:
        print(f"  [ok] {arq:<34} {real}")
    else:
        print(f"  [!!] {arq:<34} ALTERADO — real {real} / manifesto {registrado[arq]}"); falhas += 1

print("")
print(f"{len(presentes)} arquivos · {len(registrado)} registros · {falhas} falha(s)")

# --- varredura de dado pessoal -------------------------------------------
GRAVE = {
    "CPF":     re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
    "sessão":  re.compile(r"Conta Fazenda RJ|Minha conta\b|Notificações\s+99"),
}
AVISO = {
    "CNPJ":    re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"),
    "e-mail":  re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]{2,}\b"),
}
graves = avisos = 0
for arq in sorted(presentes):
    texto = open(os.path.join(RAIZ, arq), encoding="utf-8").read()
    for rotulo, padrao in GRAVE.items():
        for achado in padrao.findall(texto):
            print(f"  [!!] {arq:<38} DADO PESSOAL ({rotulo}): {achado}"); graves += 1
    for rotulo, padrao in AVISO.items():
        n = len(padrao.findall(texto))
        if n:
            print(f"  [..] {arq:<38} {rotulo} no texto normativo: {n} (conferir)"); avisos += 1

print(f"varredura de dado pessoal: {graves} grave(s) · {avisos} a conferir")
sys.exit(1 if (falhas or graves) else 0)
