# Instruções para o Claude neste acervo

## Contexto

Escritório: Nahid, De Vitto & Campos Advogados. Sócios tributaristas.
Projeto: consultoria em Reforma Tributária, entregue por setor.

**Primeiro setor atacado: transporte rodoviário de cargas (TRC).** O acervo, porém, é
multissetorial: das 46 normas, **35 são transversais** e servem a qualquer setor. Ver
`TAXONOMIA.md` antes de acrescentar norma nova.

## Regra inegociável

**Nenhuma afirmação sem dispositivo lido.** Antes de responder qualquer coisa sobre o regime
jurídico, faça `grep` nos arquivos deste acervo e cite artigo, parágrafo e inciso. Se o
dispositivo não estiver aqui, diga que falta — não preencha por memória.

`grep` acha string, não dispositivo. **Ler o artigo inteiro** antes de afirmar.

Já aconteceu de uma síntese afirmar que o teto de 26,5% estava no art. 18 da LC 214. Está no
**art. 475, §§ 10-12**, e **não é teto**: é dever do Executivo de propor PLP. A alíquota pode
legalmente superar 26,5%. Esse é o padrão de erro a evitar.

## Como pesquisar

Os arquivos estão **na raiz** do repositório (não em `texto/`).

    grep -n "transporte de carga" LC-214-2025.txt
    grep -n -A 12 "^Art. 169" LC-214-2025.txt
    python3 mapear.py DEC-12955-2026.txt | awk -F'\t' '$2==169'

**Antes de citar artigo de lei antiga, rodar `camadas.py`.** Ele separa as redações empilhadas e
devolve as notas oficiais de cada uma, distinguindo redação **superada** (o dispositivo vige, com
outra redação), dispositivo **revogado** e versão **sem eficácia**:

    python3 camadas.py LEI-9430-1996.txt 2      # duas camadas: vige a de 2014
    python3 camadas.py LEI-9430-1996.txt 18     # revogado pela Lei 14.596/2023
    python3 camadas.py --acervo                 # onde há empilhamento

A leitura que ele devolve é **hipótese, não conclusão** — continua valendo ler o artigo inteiro.

A numeração da LC **não** bate com a dos regulamentos. LC art. 169 → Decreto arts. 250,
252-255 (cinco artigos, mais o 251, que trata da obrigação do TAC). LC art. 180 → Decreto
art. 267. Sempre consultar o mapa.

## Antes de acrescentar norma

0. **Se a fonte for PDF:** extrair com `pdftotext -layout -enc UTF-8 fonte.pdf bruto.txt` e passar
   por `python3 limpar_pdf.py bruto.txt limpo.txt "TÍTULO DO CABEÇALHO"`. **Nunca o modo padrão do
   `pdftotext`**: ele junta a quebra de linha hifenizada e engole o hífen — `ano-calendário` vira
   `anocalendário`, e o termo deixa de ser localizável. Verificado em 03/08/2026.
1. Normalizar com `python3 normalizar.py bruto.txt NOME.txt` — ele **aborta** se perder palavra.
2. Classificar em `fontes.tsv` (setor e jurisdição — ver `TAXONOMIA.md`).
3. Registrar no `MANIFESTO.md` com o SHA-256.
4. `python3 validar.py` — deve fechar sem falhas.

Norma estadual de imposto geral (lei do ICMS, adicional de pobreza, fundos que corroem
benefício) é **transversal** naquela UF, não do setor que motivou a busca.

## Pontos em aberto (não afirmar como resolvidos)

- **Art. 169, §1º, I** — "contribuinte que adquire bens *e* serviços": o beneficiário é só o
  embarcador (FOB), ou também a ETC que subcontrata TAC? O Decreto 12.955, art. 250, reproduz
  o texto literalmente e **não resolve**. Adotamos a leitura ampla (o §8º, sobre cooperativas,
  é o argumento decisivo), mas a controvérsia é real — consulta à RFB recomendada.
- **Percentuais do art. 169 (§4º)**, alíquotas de referência do IBS e alíquota específica do
  diesel: **pendentes de ato**. Sem eles não há quantificação — só cenário condicional.
- **Crédito de diesel no ano-teste de 2026**: o art. 267 do Decreto não está diferido para
  2027, mas a articulação com os arts. 346/348 **não foi examinada**.
- **Art. 82-C do Livro IX do RICMS-RJ** afasta o Convênio 106/96 na subcontratação e no TAC.
  A modelagem disso no simulador é **simplificada** e carece de validação.
- **Alcance da LC 224/2025 sobre o crédito presumido do art. 3º, § 19, da Lei 10.833**
  (subcontratação de TAC): o art. 4º, § 2º, II, `d`, lista créditos presumidos nominalmente e
  **não o inclui**; o § 2º, I, alcança o que constar do demonstrativo de gastos tributários anexo
  à LOA de 2026, que **não está neste acervo**. Se alcançado, o aproveitamento cai a 90%
  (art. 4º, § 4º, IV). **Não afirmar em nenhum sentido** sem o demonstrativo.
- **Sete ocorrências de `anocalendário`** em `LC-123-2006.txt` (2) e `RES-CGSN-140-2018.txt` (5):
  hífen perdido na extração de 29/07. Conteúdo íntegro, busca prejudicada nesses pontos —
  `grep "ano-calendário"` **não** os encontra. Correção pendente de reextração.
- **A Lei 8.212 do acervo não tem a camada de 2027.** O compilado traz "Vide Lei nº 15.371, de
  2026" no cabeçalho e nada mais. A Lei 15.371/2026, art. 7º, altera o art. 28, § 9º, `a`
  (salário-paternidade passa a integrar o salário-de-contribuição) e o art. 89, § 11, com
  vigência em **1º/01/2027**. A lei alteradora **não está no acervo** — não afirmar a redação
  de 2027 a partir deste arquivo.
- **A quebra de linha não é confiável como âncora de busca.** O `normalizar.py` não quebra em
  `§ 15.` (§ de dois dígitos com ponto), nem em `Art. 3o` / `§ 7o` (ordinal com a letra `o`), e
  quebra **indevidamente** em remissão (`§ 2º deste artigo`). Buscar por conteúdo
  (`grep -n "§ 15\. Na contratação"`), nunca por `^§`. Medido em 03/08/2026; correção pendente
  de commit próprio, porque altera o SHA de todos os arquivos.

- **`LEI-9430-1996.txt` tem defeito da própria página do Planalto: `pela` no lugar de `pelo`** —
  ao menos 103 ocorrências (748 `pela` contra 1 `pelo`). **Confirmado no HTML oficial em 03/08/2026**
  — mesma contagem na marcação original. Busca por `pelo sujeito passivo`, `pelo contribuinte` ou
  `pelo valor` **falha neste arquivo**; buscar por `pela` nesses casos. O conteúdo normativo está
  completo. **Não citar trecho literal deste arquivo sem conferir a preposição.**
- **Metade do arquivo é redação superada, e a primeira ocorrência de um dispositivo pode ser a
  velha.** As páginas do Planalto empilham as redações sucessivas: em `LEI-9430-1996.txt` são 51%
  do arquivo; em grau menor, quase todo o acervo (`LEI-8036-1990` 48%, `RJ-LEI-2657-1996` 34%,
  `LEI-8212-1991` 29%, `LC-214-2025` 6%). **Nunca inferir vigência pela posição.**
- **Vigência se lê pela nota entre parênteses — não pelo tachado, que a extração perde e que na
  fonte já é ambíguo.** Medido na página da Lei 9.430: dos 639 blocos tachados, 160 trazem
  "(Incluído …)" e 98 "(Redação dada …)" — versões que vigeram e foram substituídas —, 27 são
  "(Sem eficácia)" (MP que nunca vigeu), 27 "(Revogado)" e 262 sem nota nenhuma. E **32 das 59
  notas "(Revogado pela …)" estão FORA do tachado**: os arts. 18 a 24-B, revogados pela
  Lei 14.596/2023, aparecem em tipo normal. As notas **estão** no `.txt`. Procedimento: ler o
  artigo inteiro até o fecho, achar a nota, e — se ela remeter a lei com produção de efeitos
  diferida — ir à lei alteradora. Distinguir sempre três coisas que o tachado confunde: redação
  **superada** (dispositivo vigente com outra redação), dispositivo **revogado**, e versão **sem
  eficácia**.
- **`LEI-9430-1996.txt` é dupla camada.** O art. 64 aparece com a redação anterior à reforma (ainda
  com COFINS e PIS/PASEP) e o art. 66 vigente. A redação de 2027 está no art. 502 da LC 214 e a
  revogação dos §§ 7º-8º do art. 64 e do art. 66, no art. 542, V, a partir de 1º/01/2027 — como
  na LC 123 (art. 517) e na Lei 8.212 (Lei 15.371/2026).
- **A Lei 9.250/1995 não está no acervo.** Os arts. 10 e 10-A da Lei 9.249 remetem aos seus
  arts. 6º-A, 16-A e 16-B (acrescidos pela Lei 15.270/2025). Sem ela não se fecha o cálculo do
  redutor nem o da tributação mínima de altas rendas.

- **Captura nova vem em HTML, não em PDF.** Salvar a página do Planalto com `Ctrl+S` e processar
  com `limpar_html.py` + `normalizar.py`. Preferir sempre a URL **compilada**. O PDF de impressão
  continua válido para o que já entrou, mas erra o ordinal sobrescrito — 18 ocorrências medidas na
  `LEI-9430-1996.txt` em 04/08/2026 — e joga fora o tachado.

- **O ordinal tem três grafias no acervo: `º`, `o` e `°`.** A `LEI-9718-1998.txt` traz 367 de `º` e
  **46 de `°`** (sinal de grau); a `LEI-9250-1995.txt`, 9 de `°`. Busca por `Art. 8º` **falha** onde
  a página escreveu `Art. 8°`. Usar classe `[ºo°]` ao procurar dispositivo, como faz o `camadas.py`.
- **O eixo da renda tem cinco arquivos e uma ordem de leitura.** Alíquota da CSLL na
  `LEI-7689-1988` (art. 3º, red. Lei 11.727/2008); percentuais de presunção na `LEI-9249-1995`
  (art. 15) e a mecânica na `LEI-9430-1996`; PIS/COFINS **cumulativo** na `LEI-9718-1998` e **não
  cumulativo** nas Leis 10.637 e 10.833 — a escolha entre os dois segue o art. 10, II, da Lei
  10.833; IRPF e o circuito dos dividendos na `LEI-9250-1995` com a `LEI-15270-2025`; subvenções na
  `LEI-14789-2023`; e o `DEC-9580-2018` costurando tudo, com o art. 591 (presumido a 8%) e o
  rendimento do transportador autônomo (10% no transporte de carga).

- **O custo do TAC soma-se de três leis, não de uma.** Previdenciário: 20% sobre 20% do valor da
  nota (art. 28, § 11, da `LEI-8212-1991`). Terceiros do transporte: **1,5% ao SEST e 1,0% ao SENAT**
  sobre o salário de contribuição (art. 7º, II, da `LEI-8706-1993`). IRPF do próprio autônomo: **10%
  do rendimento total no transporte de carga**, com o vale-pedágio obrigatório fora
  (`DEC-9580-2018`). Nenhuma delas é alcançada pela LC 214.
- **O RAT não é número fixo.** A alíquota de 1%, 2% ou 3% depende do enquadramento por atividade
  econômica, que mora no `DEC-3048-1999`, e o FAP a **reduz em até 50% ou aumenta em até 100%**
  (art. 10 da `LEI-10666-2003`). Sem os dois, o custo de folha é faixa, não número.
- **O `normalizar.py` já aceita as três grafias do ordinal.** Corrigido em 04/08/2026, com
  renormalização geral: dezoito arquivos reescritos, zero alteração de conteúdo, dezenove
  inalterados. A `LEI-10666-2003.txt` passou de 13 para 43 linhas. As Resoluções CGSN e a LC 123,
  que conservavam a quebra da fonte, foram reagrupadas no formato canônico — uma linha por
  dispositivo.

- **Duas citações que o assistente errou em 04/08/2026 e que ficam advertidas.** A base
  previdenciária do transportador autônomo — 20% do valor bruto do frete — está no **art. 28,
  § 11** da `LEI-8212-1991` (red. Lei 13.202/2015), e **não** no art. 22, § 15, que é (VETADO).
  E a alíquota da CSLL da transportadora é a do **art. 3º, III, da `LEI-7689-1988`** (9%,
  incl. Lei 13.169/2015); os 15% do inciso I são de seguros privados e instituições da LC 105.
  Ambas foram apanhadas ao ler o texto para semear o banco.

- **`LEI-8212-1991.txt` é o texto COMPILADO desde 04/08/2026.** Traz só a redação vigente; nenhum
  artigo falta, mas não há camadas anteriores. Para história dessa lei, ir à página consolidada
  `l8212cons.htm`. O art. 28, § 11 — base do TAC — está lá, com a mesma numeração.
- **`LEI-10637-2002` e `LEI-10833-2003` vêm da PÁGINA-BASE**, não da compilada. O `fontes.tsv`
  registrava errado até 04/08/2026.

- **O custo do TAC agora fecha com o vale-pedágio.** A `LEI-10209-2001` diz que ele **não integra o
  frete** — é o que o art. 39, § 1º, do `DEC-9580-2018` pressupõe. Descontar antes de aplicar os
  10% do imposto de renda e os 20% da base previdenciária.
- **A alíquota do PIS cumulativo está na `LEI-9715-1998`, art. 8º, I** — 0,65% sobre o faturamento.
  Não está na Lei 9.718, que só trata da COFINS a 3%. Erro fácil de cometer.

- **NÃO afirmar que o CT-e é rejeitado em produção por falta dos campos de IBS/CBS.** A NT CT-e
  2026.002 **v1.01** alterou a data: regra 001 com HOMOLOGAÇÃO em 01/07/2026 e **PRODUÇÃO em
  "implementação futura"**. Não confundir com o Ato Conjunto RFB/CGIBS 4/2026, que trata de quais
  modelos passam a ser exigíveis — obrigação diversa. O que vale com data certa: informado o grupo
  CBS em documento de 2026, a alíquota tem de ser **0,90%** (art. 346 da LC 214/25), sob pena de
  rejeição 326.

## Estilo

Português. Citação no formato "art. 169, § 1º, I, da LC 214/2025". Separar sempre
**o que está normatizado** do **que ainda é indefinido**. Nenhum número dependente de ato
pendente vai a cliente como previsão — só como cenário condicional, com a premissa à vista.
