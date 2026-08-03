#!/usr/bin/env python3
"""
limpar_pdf.py — pré-processamento do texto extraído de PDF do Planalto,
ANTES do normalizar.py. Só remove ruído de impressão e restaura hifenização
de fim de linha. Não toca no texto normativo.

Uso: python3 limpar_pdf.py entrada.layout.txt saida.limpo.txt "TITULO DO CABECALHO"
"""
import re, sys, collections

ent, sai, titulo = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(ent, encoding='utf-8').read()

removidas = collections.Counter()

# 1. form feed (quebra de página do pdftotext)
n_ff = t.count('\x0c'); t = t.replace('\x0c', '\n')
removidas['U+000C (quebra de página)'] = n_ff

# 2. cabeçalho de página: "03/08/2026, 17:19        <titulo>"
cab = re.compile(r'^[ \t]*\d\d/\d\d/\d{4},[ \t]*\d\d:\d\d[ \t]+' + re.escape(titulo) + r'[ \t]*$', re.M)
removidas['cabeçalho (data/hora + título)'] = len(cab.findall(t)); t = cab.sub('', t)

# 3. rodapé de página: "https://...    N/M"
rod = re.compile(r'^[ \t]*https?://\S+[ \t]+\d+/\d+[ \t]*$', re.M)
removidas['rodapé (URL + contador de página)'] = len(rod.findall(t)); t = rod.sub('', t)

# 4. hifenização de fim de linha: "ano-\n   calendário" -> "ano-calendário"
hif = re.compile(r'(?<=[0-9A-Za-zÀ-ÿ])-[ \t]*\n[ \t]*(?=[0-9A-Za-zÀ-ÿ])')
achados = [m for m in hif.finditer(t)]
removidas['junção de hífen de fim de linha'] = len(achados)
t = hif.sub('-', t)

# 5. sobras: linhas de carimbo/URL/contador isoladas (extração em coluna simples)
sobra = re.compile(r'^[ \t]*(?:\d\d/\d\d/\d{4},[ \t]*\d\d:\d\d|https?://\S+|\d+/\d+|' + re.escape(titulo) + r')[ \t]*$', re.M)
removidas['sobras isoladas de cabeçalho/rodapé'] = len(sobra.findall(t)); t = sobra.sub('', t)

open(sai, 'w', encoding='utf-8').write(t)
print(f'{ent} -> {sai}')
for k, v in removidas.items():
    print(f'   {k:<40} {v}')
