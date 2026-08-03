# MANIFESTO DO ACERVO

Proveniência e integridade. Gerado em 16/07/2026; atualizado em **03/08/2026**
(incorporação da LC 224/2025, da Lei 15.270/2025 e do Código Tributário Nacional; e,
no mesmo dia, do FGTS e da Lei Orgânica da Seguridade Social).

Cada arquivo foi normalizado a partir da fonte oficial, com conferência palavra a palavra.
O texto **não foi reescrito** — apenas reformatado e reparado quanto a caracteres
corrompidos na conversão (ver "Reparos").

Para conferir a integridade a qualquer momento:

    python3 validar.py

> **Sobre a coluna "Palavras".** Conta os tokens `[0-9A-Za-zÀ-ÿ]+` do arquivo final, de
> forma uniforme para todos os diplomas. Pode divergir em alguns pontos percentuais de
> contagens anteriores, que usavam método distinto para acentuação. **A integridade real é
> ancorada no SHA-256** — os hashes permanecem idênticos aos originais auditados.

## Integridade

| Arquivo | Norma | Setor | Jurisdição | Linhas | Palavras | SHA-256 (12) |
|---|---|---|---|---:|---:|---|
| `EC-132-2023.txt` | Emenda Constitucional nº 132, de 20/12/2023 — ADCT arts. 128-129 (transição do ICMS 2029-2033) | transversal | federal | 623 | 14.770 | `4742874996d7` |
| `LEI-5172-1966.txt` | Lei nº 5.172, de 25/10/1966 — **Código Tributário Nacional**, compilado. Normas gerais de direito tributário. Alterado pela LC 227/2026 (ITBI: arts. 35, 38 e 41; COSIP: art. 82-A, Título V-A) e pela LC 214/2025 (art. 9º, IV e IV, `b`) | transversal | federal | 1.003 | 16.768 | `fdb04bb3f84c` |
| `LC-214-2025.txt` | Lei Complementar nº 214, de 16/01/2025 — compilada (c/ LC 227). Espinha dorsal do IBS/CBS | transversal | federal | 6.094 | 126.519 | `ad53bd0bcd8d` |
| `LC-227-2026.txt` | Lei Complementar nº 227, de 13/01/2026 — CGIBS; alterou a LC 214 | transversal | federal | 3.004 | 61.623 | `dc36fa1b24cc` |
| `LC-192-2022.txt` | Lei Complementar nº 192, de 11/03/2022 — ICMS monofásico de combustíveis | transversal | federal | 107 | 3.734 | `b5d0ae61a73a` |
| `LC-224-2025.txt` | Lei Complementar nº 224, de 26/12/2025 — redução linear dos incentivos e benefícios federais (art. 4º, § 4º: crédito presumido limitado a 90%; presunção do lucro presumido +10% acima de R$ 5 milhões); teto global de 2% do PIB (art. 5º); alterou a LRF (arts. 14 e 14-A) | transversal | federal | 184 | 3.773 | `dec32aa34701` |
| `LEI-8036-1990.txt` | Lei nº 8.036, de 11/05/1990 — **FGTS**, compilada. Depósito de 8% sobre a remuneração (art. 15) e exclusão expressa do autônomo da condição de trabalhador (art. 15, § 2º); multa rescisória de 40% (art. 18, § 1º); encargos do atraso (art. 22) e multa administrativa de 30% do débito (art. 23, § 2º, `b`) | transversal | federal | 716 | 24.785 | `695be98c2d0c` |
| `LEI-8212-1991.txt` | Lei nº 8.212, de 24/07/1991 — **Lei Orgânica da Seguridade Social** (custeio), compilada. Contribuição patronal de 20% (art. 22, I e III) e RAT (art. 22, II); **base de 20% da nota fiscal na contratação de transporte rodoviário de carga prestado por condutor autônomo (art. 22, § 15)** e salário-de-contribuição do condutor autônomo em 20% do frete bruto (art. 28, § 11); retenção de 11% na cessão de mão de obra (art. 31); contribuições em reclamatória trabalhista (art. 43) | transversal | federal | 1.234 | 48.938 | `573b9d8d8aeb` |
| `LEI-10637-2002.txt` | Lei nº 10.637, de 30/12/2002 — PIS não cumulativo | transversal | federal | 382 | 18.003 | `71e6275b73fe` |
| `LEI-10833-2003.txt` | Lei nº 10.833, de 29/12/2003 — COFINS não cumulativo (art. 3º, §§ 19-20) | transversal | federal | 780 | 39.807 | `002fd3028601` |
| `LEI-15270-2025.txt` | Lei nº 15.270, de 26/11/2025 — IRPF: redução do imposto até R$ 5.000,00/mês (art. 3º-A da Lei 9.250), retenção de 10% sobre dividendos acima de R$ 50.000,00/mês (art. 6º-A), tributação mínima de altas rendas acima de R$ 600.000,00/ano (art. 16-A) e redutor do art. 16-B. O art. 5º destina o excedente de arrecadação ao cálculo da alíquota de referência da CBS | transversal | federal | 148 | 3.910 | `e63d9b614ecf` |
| `LC-123-2006.txt` | Lei Complementar nº 123, de 14/12/2006 — Estatuto da ME/EPP e Simples Nacional; compilada do Planalto. **Dupla camada:** a redação de 2027 (IBS/CBS no DAS) vive no art. 517 da `LC-214-2025.txt` | transversal | federal | 6.223 | 47.763 | `718da17ee0b0` |
| `DEC-12955-2026.txt` | Decreto nº 12.955, de 29/04/2026 — Regulamento da CBS | transversal | federal | 5.606 | 130.507 | `6ccde9b698aa` |
| `RES-CGIBS-6-2026.txt` | Resolução CGIBS nº 6, de 30/04/2026 — Regulamento do IBS | transversal | nacional | 6.934 | 143.186 | `bc41cb73a72c` |
| `RES-CGSN-140-2018.txt` | Resolução CGSN nº 140, de 22/05/2018 — Regulamento do Simples Nacional (DOU 24/05/2018), consolidada, c/ Anexos | transversal | nacional | 7.959 | 63.852 | `9cd0b3106a57` |
| `RES-CGSN-186-2026.txt` | Resolução CGSN nº 186, de 09/04/2026 — opção pelo Simples e pelo regime regular de IBS/CBS para 2027 (janela 01-30/09/2026) | transversal | nacional | 64 | 875 | `afc1ec7df6b4` |
| `LEI-11442-2007.txt` | Lei nº 11.442, de 05/01/2007 — Transporte Rodoviário de Cargas (TAC, ETC, CTC) | trc | federal | 152 | 6.423 | `e3c44dd58953` |
| `CONV-ICMS-106-1996.txt` | Convênio ICMS 106/96 (CONFAZ) — crédito outorgado de 20% ao transporte | trc | nacional | 7 | 397 | `ab5f1f4728c8` |
| `NT-CTE-2025.001.txt` | Nota Técnica CT-e 2025.001 v1.00, de 28/03/2025 — **DESATUALIZADA** | trc | nacional | 11 | 5.809 | `3af4c6200b5e` |
| `RJ-LEI-2657-1996.txt` | Lei estadual RJ nº 2.657, de 26/12/1996 — Lei do ICMS-RJ (art. 14: interna a 20%, Lei 10.253/2023) | transversal | rj | 2.012 | 58.163 | `5c2f0f08021b` |
| `RJ-LC-210-2023.txt` | Lei Complementar estadual RJ nº 210, de 21/07/2023 — FECP (c/ LC 217/2023) | transversal | rj | 53 | 2.475 | `7dbf8ae93cb4` |
| `RJ-DEC-47057-2020-FOT.txt` | Decreto estadual RJ nº 47.057, de 04/05/2020 — FOT, consolidado c/ o Dec. 50.248/2026 | transversal | rj | 123 | 5.827 | `bcb6498d5a3e` |
| `RJ-DEC-50248-2026-FOT.txt` | Decreto estadual RJ nº 50.248, de 23/03/2026 — altera o FOT; escalonamento 20%→60% | transversal | rj | 98 | 3.996 | `b8fc87ea3469` |
| `RJ-DEC-27427-2000-LIVRO-IX.txt` | RICMS-RJ (Dec. 27.427/2000), só o Livro IX — prestação de transporte (art. 82-C) | trc | rj | 333 | 15.326 | `795a9cb2b9ec` |

**Resumo:** 24 normas — 20 transversais, 4 de TRC. Por jurisdição: 14 federais, 5 nacionais, 5 do RJ.

## Incorporação de 29/07/2026 — o eixo do Simples Nacional

Três normas incorporadas para fundar o PARECER 06 (Simples Nacional na reforma). Proveniência:
LC 123 do compilado oficial do Planalto (captura de 29/07/2026, 00:16); Resolução CGSN 140/2018
do sistema oficial de normas da RFB (sijut2consulta, consulta 92278, 00:18); Resolução CGSN
186/2026 do DOU/Imprensa Nacional (ed. 73, seç. 1, p. 63, captura 00:17 — o portal adverte que o
conteúdo não substitui a versão certificada; advertência registrada).

Reparos de pré-processamento, sem tocar o texto normativo: quebras de página do extrator
(44 + 118 + 2), rodapés com carimbo de hora, URL, contador de página e título repetido, e — só na
Resolução 140 — 709 linhas de artefatos de interface do sijut (`home`, `print`, `keyboard_arrow_*`,
`event`, `format_list_bulleted`), removidas apenas como linha exata, jamais dentro de texto. A rotina
de verificação recusou-se, por desenho, a aceitar caractere de controle desconhecido; nada
encontrou. Hifenização de fim de linha: zero ocorrências nos três.

Provas de conteúdo executadas e aprovadas: LC 123 — art. 3º, § 4º, III-IV; art. 13, VI; art. 17,
V-VI; art. 18, § 5º-E; art. 23, § 1º; Anexo III vigente (6ª faixa, dedução 648.000,00); fecho.
Res. 186 — arts. 1º a 4º íntegros. Res. 140 — ementa, publicação e anexos.

Nota de leitura conjunta: o compilado do Planalto da LC 123 **não** contém a camada que produz
efeitos em 2027 — ela consta do art. 517 da LC 214 (renumeração da LC 227 já refletida no arquivo
do acervo). As duas peças leem-se juntas.

## Incorporação de 03/08/2026 — o eixo do IRPF, os benefícios federais e o CTN

Três normas incorporadas a pedido do sócio, em incorporação **parcial** — outras normas do mesmo
lote seguem por subir. Proveniência: as três de captura própria do Planalto em 03/08/2026
(Lcp 224 e L15270 às 17h19; L5172COMPILADO às 17h18), em PDF de impressão da página oficial.

**Mudança de método de extração, e a razão dela.** Estes três vieram com `pdftotext -layout`, e
não no modo padrão. O modo padrão foi testado primeiro e **corrompeu 5 palavras** nos três
arquivos, todas em quebra de linha hifenizada: `ano-calendário` → `anocalendário` (2x),
`pré-constituída` → `préconstituída`, `Decreto-lei` → `Decretolei` e `PIS/Pasep-Importação` →
`PasepImportação`. É exatamente o padrão de corrupção que a seção "Reparos" já documentava para
o `U+0002`. O modo `-layout` preserva o hífen no fim da linha, e a junção passa a ser
determinística. A rotina `limpar_pdf.py` executa essa junção e conta o que removeu.

Reparos de pré-processamento, sem tocar o texto normativo: quebras de página do extrator
(9 + 9 + 34), cabeçalho de página (carimbo de data/hora + título, 9 + 9 + 34), rodapé (URL +
contador de página, 9 + 9 + 34) e junção de hífen de fim de linha (1 + 2 + 2). Zero caractere de
controle não mapeado; zero palavra perdida na conferência do `normalizar.py`.

Provas de conteúdo executadas e aprovadas. **LC 224** — art. 4º, § 4º, I a VII íntegros; § 5º
(R$ 5.000.000,00); § 8º, I a XIII; art. 5º (2% do PIB); art. 14 (produção de efeitos); fecho.
**Lei 15.270** — arts. 3º-A, 6º-A, 11-A, 16-A (inclusive a fórmula do § 2º, II) e 16-B; art. 5º
(CBS); fecho. **CTN** — arts. 3º, 9º (IV, com a redação da LC 214/2025), 35, 38, 82-A, 116, 150,
173, 174, 204 e 218; 23 remissões à LC 227/2026 presentes.

**Por que entram, e a que se ligam.** A LC 224 reduz benefícios federais de PIS/COFINS e do lucro
presumido durante a transição e alcança **crédito presumido** (art. 4º, § 4º, IV: aproveitamento
limitado a 90%) — toca o marco de comparação do Parecer 05. A Lei 15.270 altera o custo da
distribuição de lucros a partir de 1º/01/2026 e, no art. 5º, liga o excedente de arrecadação ao
cálculo da alíquota de referência da CBS. O CTN é a moldura geral e passou a ser peça da própria
reforma (ITBI e COSIP pela LC 227/2026; art. 9º, IV, pela LC 214/2025).

**Tese em aberto, não afirmada:** o alcance da LC 224 sobre o crédito presumido do art. 3º, § 19,
da Lei 10.833 (subcontratação de TAC). O § 2º, II, `d`, do art. 4º lista créditos presumidos
nominalmente e **não inclui** aquele dispositivo; o § 2º, I, porém, alcança o que estiver no
demonstrativo de gastos tributários anexo à LOA de 2026 — documento **fora deste acervo**.
Sem ele, não se afirma nem se nega.

## Incorporação de 03/08/2026 (segundo lote) — o eixo do custo do trabalho

Duas normas, conclusão do lote iniciado na incorporação anterior. Proveniência: captura própria
do Planalto em 03/08/2026 (Lei 8.036 às 17h18; Lei 8.212 às 17h17), em PDF de impressão da
página oficial, ambas na versão **compilada**.

**Por que entram, e a que se ligam.** São as duas leis que dão preço ao risco central do
PARECER 02 — o reconhecimento de vínculo empregatício em arranjo de TAC-agregado. Enquanto o
motorista é autônomo, a contratação custa à empresa **20% sobre 20% do valor da nota fiscal**
(art. 22, § 15, da Lei 8.212, com o correspondente salário-de-contribuição do art. 28, § 11) e
**não gera FGTS**, porque o art. 15, § 2º, da Lei 8.036 exclui o autônomo da definição de
trabalhador. Reconhecido o vínculo, a base passa a ser a remuneração integral (art. 22, I e II,
da Lei 8.212) e nasce o depósito de 8% (art. 15) com a multa de 40% na dispensa (art. 18, § 1º),
mais os encargos do art. 22 e a multa administrativa de 30% do art. 23, § 2º, `b`, ambos da
Lei 8.036. **Nenhuma dessas contribuições é alcançada pela LC 214/2025** — a reforma é do
consumo —, o que faz destas duas leis o marco de comparação que sobrevive intacto a 2027 e
permite quantificar o risco do Parecer 02 em vez de apenas descrevê-lo.

Extração com `pdftotext -layout -enc UTF-8` e `limpar_pdf.py`, pelo motivo já documentado na
seção anterior — e reconfirmado aqui. O modo padrão foi rodado em paralelo, só para prova, e
**corromperia 14 termos**: `pró-cotista` na Lei 8.036 e, na Lei 8.212, `salário-de-contribuição`,
`salário-família`, `pré-constituída`, `médico-hospitalares`, `Seguro-Desemprego`, `Social-INSS`,
`Trabalho-CLT`, `Público-PASEP`, `aplicar-se`, `sujeitar-se`, `extingui-lo` e `Saúde-SUS`.
Nenhum deles entrou no acervo.

Reparos de pré-processamento, sem tocar o texto normativo: quebras de página (34 + 65),
cabeçalho de página (34 + 65), rodapé (34 + 65) e junção de hífen de fim de linha (7 + 20).
As 27 junções foram conferidas **uma a uma**: todas são hífen legítimo de palavra composta
(`FI-FGTS`, `infra-estrutura`, `mão-de-obra`, `salário-de-contribuição`); nenhuma é silabação.
Zero caractere de controle não mapeado.

**Defeito do instrumento, corrigido nesta incorporação.** O `normalizar.py` abortou a Lei 8.212
acusando divergência de conteúdo com contagem idêntica dos dois lados (48.938 → 48.938). A
investigação mostrou que o conteúdo estava íntegro e o **medidor** é que errava: a rotina
`conferir()` comparava o bruto **ainda em NFD** contra a saída **já em NFC**, e o par
`a` + U+0300 (dois tokens para a expressão regular) não casa com `à` (um token). As duas únicas
ocorrências decompostas do arquivo estão no art. 45-A, § 4º, acrescido pela Lei 15.363/2026 — o
dispositivo mais novo do texto. Corrigido: `conferir()` passa a normalizar em NFC **os dois
lados**. O instrumento foi provado nos dois sentidos depois da correção — aceita o texto íntegro,
recusa saída com uma palavra a menos (48.938 → 48.937) e recusa saída com **uma palavra trocada**
e contagem igual. É a quinta vez neste projeto que o instrumento de medida erra mais que a
construção; a regra da casa se confirma.

Provas de conteúdo executadas e aprovadas. **Lei 8.036** — art. 15 (caput, §§ 2º e 7º), art. 18
(caput e § 1º), art. 19-A, art. 20, art. 22, art. 23 (§ 2º, `b`), art. 23-A, art. 25, art. 32 e o
ANEXO da Lei 13.932/2019 (tabela do saque-aniversário); fecho com assinaturas. **Lei 8.212** —
art. 11, parágrafo único; art. 12, V, `g`; art. 15, parágrafo único; arts. 21, 22 (I, II, III,
§ 15), 28 (III e § 11), 30 (I, `b`), 31, 33, 43 (§ 2º), 45-A (§ 4º), 47, 89 e 105; fecho e as 25
notas de rodapé da republicação.

**Camada de 2027 fora do arquivo, registrada.** O compilado da Lei 8.212 traz no cabeçalho
"Vide Lei nº 15.371, de 2026 — Vigência", **sem** incorporar-lhe o conteúdo ao corpo. Lido o
texto oficial no Planalto em 03/08/2026: a Lei 15.371, de 31/03/2026, institui o
salário-paternidade e, pelo art. 7º, altera a Lei 8.212 em dois pontos — art. 28, § 9º, `a`
(o salário-paternidade passa a **integrar** o salário-de-contribuição, ao lado do
salário-maternidade) e art. 89, § 11 (rito de reembolso). O art. 14 fixa a vigência em
**1º/01/2027**, a mesma data da entrada plena do IBS/CBS. É o mesmo padrão da LC 123, cuja
camada de 2027 vive no art. 517 da LC 214: as duas peças leem-se juntas. A Lei 15.371 **não
está neste acervo** — recomenda-se incorporá-la quando o eixo trabalhista for atacado
(https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15371.htm).

## Fontes

As URLs oficiais de cada norma estão em `fontes.tsv`, junto da classificação de setor e
jurisdição. Só as fontes do Planalto são baixáveis por script; CONFAZ, CGIBS, SEFAZ-RJ,
ALERJ e CT-e exigem obtenção manual — o `baixar.sh` avisa e pula.

## Reparos aplicados

**Diplomas federais (fonte HTML do Planalto).** A conversão do original corrompeu 83
caracteres, verificados um a um em 16/07/2026 e restaurados. **Apagá-los teria corrompido o
texto** — "ano-calendário" viraria "anocalendário", e o termo deixaria de ser localizável.

| Corrompido | Restaurado | Ocorrências | O que era |
|---|---|---:|---|
| `U+0002` | `-` | 65 | hífen não-separável: ano-calendário, considera-se, matéria-prima |
| `U+F0B7` | `•` | 16 | marcador de lista (fonte Symbol) |
| `U+F0FC` | `✓` | 2 | visto (fonte Wingdings) |

**Convênio 106/96 e diplomas do RJ (fonte PDF oficial), acrescidos em 21/07/2026.**
Vieram de PDF (CONFAZ / SEFAZ-RJ / ALERJ) e exigiram três limpezas antes da normalização,
todas **preservadoras de conteúdo** — a verificação do `normalizar.py` confirmou zero
palavra perdida em cada um:

| Ruído removido | O que era | Onde |
|---|---|---|
| `U+000C` (form feed) | quebra de página do `pdftotext` | todos os PDF |
| `U+00AD` (hífen de sílaba) | hifenização de fim de linha ("MÁ-QUINAS" → "MÁQUINAS") | `RJ-LEI-2657-1996` (8x) |
| rodapé de página | URL + carimbo de data/hora + título repetido | todos os PDF do RJ |

**Diplomas federais em PDF do Planalto, acrescidos em 03/08/2026.** Extraídos com
`pdftotext -layout -enc UTF-8` e pré-processados por `limpar_pdf.py`, que conta e reporta o que
remove:

| Ruído removido | O que era | Ocorrências |
|---|---|---:|
| `U+000C` (form feed) | quebra de página do `pdftotext` | 52 |
| cabeçalho de página | carimbo de data/hora + título repetido | 52 |
| rodapé de página | URL oficial + contador de página | 52 |
| hífen de fim de linha | `ano-` + `calendário` → `ano-calendário` (junção, não remoção) | 5 |

**Segundo lote do mesmo dia (Lei 8.036 e Lei 8.212).** Mesmo método, mesma rotina:

| Ruído removido | O que era | Ocorrências |
|---|---|---:|
| `U+000C` (form feed) | quebra de página do `pdftotext` | 99 |
| cabeçalho de página | carimbo de data/hora + título repetido | 99 |
| rodapé de página | URL oficial + contador de página | 99 |
| hífen de fim de linha | `salário-de-` + `contribuição` (junção, não remoção) | 27 |

O `normalizar.py` **falha com erro** diante de caractere de controle não mapeado, para que
uma corrupção nova nunca entre em silêncio. Desde 03/08/2026 a rotina `conferir()` compara os
dois lados em **NFC** — antes, comparava bruto em NFD contra saída em NFC e acusava divergência
onde não havia (ver "Incorporação de 03/08/2026 (segundo lote)").

## Limitações conhecidas

- `NT-CTE-2025.001.txt` é a **versão 1.00, de 28/03/2025 — desatualizada**. O cronograma
  vigente (homologação 01/07/2026, produção 03/08/2026) não está nela. Substituir pela
  versão consolidada do Portal Nacional do CT-e.
- `DEC-12955-2026.txt`: o ANEXO I (tabela de depreciação por NCM) não tem estrutura de
  artigo e permanece em linha única. Não afeta a leitura dos dispositivos.
- `RJ-DEC-27427-2000-LIVRO-IX.txt` cobre **apenas o Livro IX** do RICMS-RJ, não o
  Regulamento inteiro. Suficiente para o escopo de transporte.
- A vigência do crédito outorgado do transporte no RJ está evidenciada na **Consulta
  SEFAZ-RJ 043/25** (18/11/2025), mantida **fora** deste acervo por ser parecer
  administrativo, não legislação.
- **Defeito herdado da incorporação de 29/07, verificado em 03/08:** há **7 ocorrências** de
  `anocalendário` — hífen perdido na quebra de linha da extração — em `LC-123-2006.txt` (2) e
  `RES-CGSN-140-2018.txt` (5). O conteúdo está íntegro e o termo aparece corretamente em 61 e 109
  outros pontos dos mesmos arquivos; o efeito é que **nesses 7 pontos o termo não é localizável por
  busca**, o que importa diretamente ao eixo do Simples. Correção pendente de reextração da fonte
  com `-layout` — não se emenda o texto sem o original à vista.
- `LEI-15270-2025.txt`: as duas tabelas de redução (art. 3º-A e art. 11-A da Lei 9.250) são
  **linearizadas** pelo extrator e as células das faixas ficam intercaladas. Nenhum valor se perdeu
  — todos conferidos —, mas a associação faixa/valor deve ser lida contra o texto oficial antes de
  ir a cálculo.
- `LEI-5172-1966.txt` é o **compilado** do Planalto: traz as alterações da LC 227/2026 e da
  LC 214/2025, mas os dispositivos com produção de efeitos diferida seguem a regra de cada lei
  alteradora, que o compilado não repete.
- `LEI-8036-1990.txt`: o **ANEXO** (faixas de saldo, alíquota e parcela adicional do
  saque-aniversário) é **linearizado** pelo extrator e as células ficam em sequência na mesma
  linha. Nenhum valor se perdeu — todos conferidos —, mas a associação faixa/valor deve ser lida
  contra o texto oficial antes de ir a cálculo. Mesma ressalva já feita à `LEI-15270-2025.txt`.
- `LEI-8212-1991.txt`: idem para as três tabelas do texto (art. 20, alíquotas do empregado;
  art. 29, escala de salários-base — **revogada** pela Lei 9.876/1999; art. 32, § 4º, multa por
  faixa de segurados, **revogado**). Duas das três já não vigem; a do art. 20 tem valores em
  cruzeiros de 1991, substituídos por portaria anual do MPS **fora deste acervo**.
- **Defeito estrutural do `normalizar.py`, medido em 03/08/2026 e ainda não corrigido.** A regra
  de quebra não reconhece três formas, e o efeito é de *estrutura de linha*, não de conteúdo —
  a integridade palavra a palavra segue garantida:
  1. **`§` de dois dígitos escrito com ponto** (`§ 15.`, estilo do Planalto a partir do § 10):
     a regra exige espaço depois do número e não quebra. 379 ocorrências no acervo publicado
     (as maiores: RES-CGIBS-6 com 91, DEC-12955 com 82, LC-214 com 77) e 133 nas duas normas
     novas.
  2. **Ordinal grafado com a letra `o`** (`Art. 3o`, `§ 7o`), herdado do HTML antigo do Planalto:
     50 ocorrências no acervo, 5 na Lei 8.036.
  3. **Quebra falsa em remissão** — `§ 2º deste artigo`, no meio de uma frase, vira início de
     linha. Contagem por padrão conservador (`§ Nº` seguido de `deste`, `desta`, `do`, `da`,
     `e`, `ou`): **ao menos** 1.119 ocorrências no acervo publicado — 435 só na LC 214 e 266 na
     LC 227 — e 114 nas duas normas novas. O número real é maior.
  Consequência prática: nesses pontos o dispositivo não começa em linha própria, e uma busca
  ancorada em início de linha (`grep "^§ 15"`) falha. Corrigir a regra **altera o SHA-256 de
  todos os arquivos afetados** e por isso não foi feita aqui: pede commit corretivo próprio,
  com renormalização de todo o acervo de uma vez e nova rodada de provas de conteúdo.
- Faltam (a obter quando o tema for atacado): Lei 10.209/2001, Lei 13.703/2018,
  ADI 7181/7191 (STF), Resolução ANTT do RNTR-C, **Lei 15.371/2026** (salário-paternidade;
  altera a Lei 8.212 a partir de 1º/01/2027).
