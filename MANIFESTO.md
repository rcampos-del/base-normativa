# MANIFESTO DO ACERVO

Proveniência e integridade. Gerado em 16/07/2026; atualizado em **05/08/2026**
(sexto e sétimo lotes — o eixo do crédito presumido do Rio de Janeiro: o Manual de Benefícios em duas
camadas, as leis e os anexos do FOT, os Convênios 100/01, 190/17 e 106/96 recapturado, e a LC 160/2017).
Antes, em **04/08/2026**
(incorporação da Nota Técnica CT-e 2026.002 v1.01, que corrige a data de exigência dos campos da RTC).
Antes, no mesmo dia,
(incorporação de oito normas — o eixo setorial do TRC e a lei que faltava ao PIS cumulativo).
Antes, no mesmo dia,
(recaptura em HTML de dez normas — resíduo de impressão removido; ver seção própria).
No mesmo dia,
(renormalização geral — dezoito arquivos reescritos sem alteração de conteúdo; ver seção própria).
No mesmo dia,
(incorporação da Lei 12.546/2011 — primeira norma erguida de **página HTML salva**,
não de PDF de impressão — e, no mesmo dia, do eixo da renda: Lei 7.689, Lei 9.250,
Lei 9.718, Lei 14.789 e o Regulamento do Imposto sobre a Renda; e do fecho do eixo da folha:
Regulamento da Previdência Social, Lei 8.706, Lei 10.666, Lei 14.973 e Lei 15.371). Antes, em **03/08/2026**
(incorporação da LC 224/2025, da Lei 15.270/2025 e do Código Tributário Nacional; no mesmo dia,
do FGTS e da Lei Orgânica da Seguridade Social; e, ainda no mesmo dia, das Leis 9.249/1995 e
9.430/1996 — o eixo do IRPJ e da CSLL).

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
| `EC-132-2023.txt` | Emenda Constitucional nº 132, de 20/12/2023 — ADCT arts. 128-129 (transição do ICMS 2029-2033) | transversal | federal | 623 | 14.099 | `9944e85d8476` |
| `LEI-5172-1966.txt` | Lei nº 5.172, de 25/10/1966 — **Código Tributário Nacional**, compilado. Normas gerais de direito tributário. Alterado pela LC 227/2026 (ITBI: arts. 35, 38 e 41; COSIP: art. 82-A, Título V-A) e pela LC 214/2025 (art. 9º, IV e IV, `b`) | transversal | federal | 1.019 | 16.768 | `e84bded927cc` |
| `LC-214-2025.txt` | Lei Complementar nº 214, de 16/01/2025 — compilada (c/ LC 227). Espinha dorsal do IBS/CBS | transversal | federal | 6.097 | 126.519 | `3109e52ba74f` |
| `LC-227-2026.txt` | Lei Complementar nº 227, de 13/01/2026 — CGIBS; alterou a LC 214 | transversal | federal | 3.004 | 59.545 | `e21bafd8e035` |
| `LC-192-2022.txt` | Lei Complementar nº 192, de 11/03/2022 — ICMS monofásico de combustíveis | transversal | federal | 107 | 3.614 | `038193b4abc4` |
| `LC-224-2025.txt` | Lei Complementar nº 224, de 26/12/2025 — redução linear dos incentivos e benefícios federais (art. 4º, § 4º: crédito presumido limitado a 90%; presunção do lucro presumido +10% acima de R$ 5 milhões); teto global de 2% do PIB (art. 5º); alterou a LRF (arts. 14 e 14-A) | transversal | federal | 184 | 3.773 | `dec32aa34701` |
| `LEI-7689-1988.txt` | Lei nº 7.689, de 15/12/1988 — institui a **CSLL**. Fato gerador, base e **alíquota de 9% para as demais pessoas jurídicas — art. 3º, III, incluído pela Lei 13.169/2015**, que é a que alcança a transportadora. O artigo tem três camadas empilhadas e, dentro da vigente, incisos com várias redações sucessivas: os 15% do inciso I (red. LC 224/2025) valem para seguros privados e instituições da LC 105, não para pessoa jurídica comum | transversal | federal | 90 | 3.058 | `babe00dde50a` |
| `LEI-8036-1990.txt` | Lei nº 8.036, de 11/05/1990 — **FGTS**, compilada. Depósito de 8% sobre a remuneração (art. 15) e exclusão expressa do autônomo da condição de trabalhador (art. 15, § 2º); multa rescisória de 40% (art. 18, § 1º); encargos do atraso (art. 22) e multa administrativa de 30% do débito (art. 23, § 2º, `b`) | transversal | federal | 743 | 24.785 | `9912ea9a0525` |
| `LEI-8212-1991.txt` | Lei nº 8.212, de 24/07/1991 — **texto compilado** (troca decidida em 04/08/2026) — **Lei Orgânica da Seguridade Social** (custeio), compilada. Contribuição patronal de 20% (art. 22, I e III) e RAT (art. 22, II); **base de 20% da nota fiscal na contratação de transporte rodoviário de carga prestado por condutor autônomo (art. 28, § 11)** e salário-de-contribuição do condutor autônomo em 20% do frete bruto (art. 28, § 11); retenção de 11% na cessão de mão de obra (art. 31); contribuições em reclamatória trabalhista (art. 43) | transversal | federal | 816 | 23.961 | `964cbae0cac7` |
| `LEI-9249-1995.txt` | Lei nº 9.249, de 26/12/1995 — **IRPJ e CSLL**; página-base do Planalto, com as redações sucessivas empilhadas. Alíquota de 15% e adicional de 10% (art. 3º); **percentuais de presunção do lucro presumido (art. 15): transporte de carga a 8% pelo caput e os demais transportes a 16% (§ 1º, II, `a`)**; base da CSLL (art. 20, I a III); juros sobre capital próprio com IRRF de 17,5% (art. 9º, § 2º, red. LC 224/2025); dividendos e o crédito do beneficiário no exterior (arts. 10 e 10-A, red. Lei 15.270/2025); extinção de punibilidade e devedor contumaz (art. 34, §§ 3º-4º, LC 225/2026) | transversal | federal | 280 | 8.577 | `85dbcb5d4401` |
| `LEI-8706-1993.txt` | Lei nº 8.706, de 14/09/1993 — cria o **SEST e o SENAT**. Contribuição compulsória do **transportador autônomo: 1,5% ao SEST e 1,0% ao SENAT sobre o salário de contribuição previdenciária** (art. 7º, II) — 2,5% que se somam ao art. 28, § 11, da Lei 8.212 no custo total do TAC | trc | federal | 54 | 1.213 | `ba09d8453ee9` |
| `LEI-9250-1995.txt` | Lei nº 9.250, de 26/12/1995 — **IRPF**; página-base do Planalto. Fecha o circuito da `LEI-15270-2025.txt`: traz os **arts. 6º-A, 16-A e 16-B**, acrescidos por ela — retenção mínima sobre lucros e dividendos, tributação mínima de altas rendas e o redutor quando a soma das alíquotas efetivas ultrapassa o teto —, todos em camada única | transversal | federal | 490 | 16.231 | `a89afb39a2dd` |
| `LEI-9430-1996.txt` | Lei nº 9.430, de 27/12/1996 — legislação tributária federal; página-base do Planalto (`l9430.htm`), **não** o texto compilado, que tem página própria e não foi capturado. Apuração trimestral e estimativa (arts. 1º-2º); lucro presumido (art. 25) e arbitrado (art. 27); multas de ofício, com a qualificação de 100%/150% da Lei 14.689/2023 (art. 44, § 1º, VI-VII); retenção na fonte por órgãos federais (art. 64); compensação e o limite mensal (arts. 74 e 74-A); **inaptidão do CNPJ por prática reiterada das infrações do *split payment* (art. 81, VIII, incluído pela LC 227/2026, que remete aos arts. 471-D e 471-E da LC 214/2025)**; representação fiscal para fins penais (art. 83, c/ LC 225/2026). **Dupla camada** e **defeito de fonte** — ver Limitações | transversal | federal | 1.123 | 35.483 | `df09c244aeb4` |
| `LEI-10637-2002.txt` | Lei nº 10.637, de 30/12/2002 — PIS não cumulativo | transversal | federal | 566 | 17.514 | `5536dd10ce68` |
| `LEI-9718-1998.txt` | Lei nº 9.718, de 27/11/1998 — **PIS/COFINS no regime CUMULATIVO**, o que se aplica ao lucro presumido (art. 10, II, da Lei 10.833); página-base do Planalto. Base de cálculo no faturamento (art. 2º) e **COFINS elevada a 3% (art. 8º), com marca de "Vide LC 214/2025 — produção de efeitos"**. É a contraparte que faltava para comparar a CBS: o não cumulativo já estava no acervo, o cumulativo não | transversal | federal | 301 | 11.647 | `1543d8c7084d` |
| `LEI-10666-2003.txt` | Lei nº 10.666, de 08/05/2003, compilada — o **FAP**. O art. 10 permite que a alíquota de 1%, 2% ou 3% do RAT seja **reduzida em até 50% ou aumentada em até 100%**, conforme o desempenho da empresa na respectiva atividade econômica. Sem ele, o custo de folha do simulador é faixa, não número | transversal | federal | 43 | 1.327 | `baf18b343aba` |
| `LEI-10833-2003.txt` | Lei nº 10.833, de 29/12/2003 — COFINS não cumulativo (art. 3º, §§ 19-20) | transversal | federal | 1.174 | 38.715 | `412f123cf2b8` |
| `LEI-12546-2011.txt` | Lei nº 12.546, de 14/12/2011 — **desoneração da folha (CPRB)**, compilada. **Transporte rodoviário de cargas, CNAE 4930-2, no art. 8º, IX** (incluído pela Lei 13.670/2018), com **alíquota de 1,5% sobre a receita bruta** (art. 8º-A, que põe 2,5% como regra e excetua os incisos VI, IX, X e XI); a substituição integral terminou em 31/12/2024 (art. 8º, caput, red. Lei 14.973/2024) e o art. 9º-A instituiu substituição **parcial e escalonada** — 2025: 80% da alíquota sobre receita + 25% da folha; **2026: 60% + 50%**; 2027: 40% + 75% —, com retorno integral à folha em 1º/01/2028 (art. 9º-B); exclusão da receita de transporte internacional de carga (art. 9º, II, `b`) e opção irretratável no pagamento de janeiro (art. 9º, § 13) | transversal | federal | 374 | 12.036 | `0f9aafcd742a` |
| `LEI-14973-2024.txt` | Lei nº 14.973, de 16/09/2024 — a **reoneração gradual da folha**. É a lei que reescreveu os arts. 7º e 8º da Lei 12.546 ("Até 31 de dezembro de 2024") e acrescentou os arts. 9º-A e 9º-B, com o escalonamento de 2025 a 2027 e o retorno integral à folha em 2028. O art. 4º condiciona a opção a **manter quadro funcional médio de ao menos 75%** do ano anterior | transversal | federal | 289 | 9.120 | `a4b50b56aee8` |
| `LEI-15270-2025.txt` | Lei nº 15.270, de 26/11/2025 — IRPF: redução do imposto até R$ 5.000,00/mês (art. 3º-A da Lei 9.250), retenção de 10% sobre dividendos acima de R$ 50.000,00/mês (art. 6º-A), tributação mínima de altas rendas acima de R$ 600.000,00/ano (art. 16-A) e redutor do art. 16-B. O art. 5º destina o excedente de arrecadação ao cálculo da alíquota de referência da CBS | transversal | federal | 148 | 3.910 | `e63d9b614ecf` |
| `LEI-15371-2026.txt` | Lei nº 15.371, de 31/03/2026 — **salário-paternidade**; capturada do **DOU**, não do Planalto. Altera a Lei 8.212 (art. 7º da lei nova) e a Lei 8.213, institui o benefício e o incentivo fiscal, e **entra em vigor em 1º/01/2027** (art. 14). É a camada de 2027 que o compilado da Lei 8.212 não incorpora | transversal | federal | 144 | 3.114 | `b918a6e55bd0` |
| `LC-123-2006.txt` | Lei Complementar nº 123, de 14/12/2006 — Estatuto da ME/EPP e Simples Nacional; compilada do Planalto. **Dupla camada:** a redação de 2027 (IBS/CBS no DAS) vive no art. 517 da `LC-214-2025.txt` | transversal | federal | 1.581 | 47.823 | `8896c261d603` |
| `DEC-12955-2026.txt` | Decreto nº 12.955, de 29/04/2026 — Regulamento da CBS | transversal | federal | 5.606 | 130.507 | `6ccde9b698aa` |
| `LEI-14789-2023.txt` | Lei nº 14.789, de 29/12/2023 — **subvenções para investimento**. Substitui a exclusão da base pelo **crédito fiscal de 25% sobre as receitas de subvenção** (arts. 1º e 6º), computáveis só as receitas relacionadas a depreciação, amortização, exaustão, locação ou arrendamento de bens de capital (art. 8º). Decide se o crédito presumido do transporte entra na base do IRPJ — ver a Solução de Consulta COSIT 6/2026 | transversal | federal | 148 | 3.001 | `e58982474499` |
| `RES-CGIBS-6-2026.txt` | Resolução CGIBS nº 6, de 30/04/2026 — Regulamento do IBS | transversal | nacional | 6.934 | 143.186 | `bc41cb73a72c` |
| `RES-CGSN-140-2018.txt` | Resolução CGSN nº 140, de 22/05/2018 — Regulamento do Simples Nacional (DOU 24/05/2018), consolidada, c/ Anexos | transversal | nacional | 2.147 | 63.852 | `d875ca42eec3` |
| `DEC-3048-1999.txt` | Decreto nº 3.048, de 06/05/1999, compilado — **Regulamento da Previdência Social**. É onde vivem o enquadramento do RAT por atividade econômica e as regras de custeio que a Lei 8.212 remete a regulamento; segunda maior peça do acervo | transversal | federal | 3.862 | 131.023 | `fd0317d2bfc0` |
| `DEC-9580-2018.txt` | Decreto nº 9.580, de 22/11/2018 — **Regulamento do Imposto sobre a Renda (RIR/2018)**, 1.050 artigos. Costura em um só texto o que as leis dispersam: **base de cálculo do lucro presumido a 8% (art. 591)** e, no rendimento do **transportador autônomo, 10% do total no transporte de carga e 60% no de passageiros, com o vale-pedágio obrigatório expressamente fora (Lei 10.209/2001)** — dispositivo que dá tratamento de IRPF ao TAC | transversal | federal | 8.334 | 197.573 | `0ce0c0d986dd` |
| `RES-CGSN-186-2026.txt` | Resolução CGSN nº 186, de 09/04/2026 — opção pelo Simples e pelo regime regular de IBS/CBS para 2027 (janela 01-30/09/2026) | transversal | nacional | 21 | 875 | `9f8e11ffc204` |
| `LEI-11442-2007.txt` | Lei nº 11.442, de 05/01/2007 — Transporte Rodoviário de Cargas (TAC, ETC, CTC) | trc | federal | 211 | 6.207 | `29692daccb49` |
| `CONV-ICMS-106-1996.txt` | Convênio ICMS 106/96 — crédito presumido de 20% no transporte; consolidado c/ Convs. 95/99 e 85/03. **Recapturado em 05/08/2026**: a versão anterior tinha 397 palavras e perdia as notas de alteração | trc | nacional | 7 | 1.059 | `be51321baa9b` |
| `LEI-9715-1998.txt` | Lei nº 9.715. de 25/11/1998 — **a alíquota do PIS/PASEP cumulativo**. Art. 8º. I: **0.65% sobre o faturamento**. com marca de produção de efeitos pela LC 214/2025. Fecha o parâmetro que a semente do banco gravara como pendente. com valor nulo. por falta de norma no acervo | transversal | federal | 61 | 1.586 | `00d0cc138bc4` |
| `LEI-10209-2001.txt` | Lei nº 10.209. de 23/03/2001 — **vale-pedágio obrigatório no transporte rodoviário de carga**. O valor **não integra o frete** e é de responsabilidade do embarcador; o art. 8º impõe indenização equivalente a **duas vezes o valor do frete** em caso de infração (Vide ADIN 6031). É o dispositivo a que remete o art. 39. § 1º. do RIR | trc | federal | 63 | 1.762 | `b84261253c1d` |
| `LEI-13703-2018.txt` | Lei nº 13.703. de 08/08/2018 — **Política Nacional de Pisos Mínimos do Transporte Rodoviário de Cargas**. Lei que a ANTT regulamenta pela tabela de coeficientes | trc | federal | 84 | 2.716 | `472150bf2b62` |
| `LC-225-2026.txt` | Lei Complementar nº 225. de 2026 — **devedor contumaz**. Citada por cinco arquivos do acervo — Decreto 12.955. Leis 9.249. 9.430 e 10.637 — e até aqui ausente dele | transversal | federal | 587 | 10.445 | `51b6c1efaf36` |
| `RES-ANTT-5982-2022.txt` | Resolução ANTT nº 5.982. de 23/06/2022 — **RNTR-C**: inscrição e manutenção no Registro Nacional de Transportadores Rodoviários de Cargas. nas categorias TAC. ETC e CTC. Sustenta o Parecer nº 02 | trc | federal | 159 | 3.261 | `7f3ab55d94e6` |
| `RES-ANTT-6068-2025.txt` | Resolução ANTT nº 6.068. de 17/07/2025 — altera a Resolução nº 5.982 e vincula a manutenção do registro à contratação dos **seguros obrigatórios** | trc | federal | 19 | 684 | `27107a27b5d5` |
| `RES-ANTT-6084-2026.txt` | Resolução ANTT nº 6.084. de 16/07/2026 — **tabela vigente dos pisos mínimos de frete**; capturada do DOU. Atualiza os coeficientes do Anexo II da Resolução nº 5.867/2020 | trc | federal | 6 | 2.184 | `104864adf351` |
| `RJ-RES-SEFAZ-876-2026.txt` | Resolução SEFAZ-RJ nº 876. de 24/03/2026 — altera o **Anexo XXIII da Parte II da Resolução SEFAZ nº 720/2014**: escrituração do FOT na EFD sob a fórmula do Decreto RJ 50.248/2026 | transversal | rj | 16 | 511 | `0a3468be0a11` |
| `NT-CTE-2026.002.txt` | Nota Técnica CT-e nº 2026.002. **versão 1.01. de 16/07/2026** — Reforma Tributária do Consumo. aplicável a CT-e. CT-e Simplificado (mod. 57) e CT-e OS (mod. 67). Campos do grupo IBS/CBS. inscrição Suframa do emitente. validações de devolução. **alíquota da CBS de 0.90% para emissão em 2026 (art. 346 da LC 214/25)** e antecipação de pagamento. **A versão 1.01 alterou a data de exigência do preenchimento dos campos da RTC: a regra 001 traz HOMOLOGAÇÃO em 01/07/2026 e PRODUÇÃO em "implementação futura"** | trc | nacional | 7 | 3.544 | `df2c67bf4170` |
| `NT-CTE-2025.001.txt` | Nota Técnica CT-e 2025.001 v1.00, de 28/03/2025 — **DESATUALIZADA** | trc | nacional | 11 | 5.809 | `3af4c6200b5e` |
| `RJ-LEI-2657-1996.txt` | Lei estadual RJ nº 2.657, de 26/12/1996 — Lei do ICMS-RJ (art. 14: interna a 20%, Lei 10.253/2023) | transversal | rj | 2.012 | 58.163 | `5c2f0f08021b` |
| `RJ-LC-210-2023.txt` | Lei Complementar estadual RJ nº 210, de 21/07/2023 — FECP (c/ LC 217/2023) | transversal | rj | 53 | 2.475 | `7dbf8ae93cb4` |
| `RJ-DEC-47057-2020-FOT.txt` | Decreto estadual RJ nº 47.057, de 04/05/2020 — FOT, consolidado c/ o Dec. 50.248/2026 | transversal | rj | 123 | 5.827 | `bcb6498d5a3e` |
| `RJ-DEC-50248-2026-FOT.txt` | Decreto estadual RJ nº 50.248, de 23/03/2026 — altera o FOT; escalonamento 20%→60%. **Regerado em 05/08/2026** sob o recorte corrigido | transversal | rj | 98 | 4.003 | `4a68968bbaf1` |
| `RJ-DEC-27427-2000-LIVRO-IX.txt` | RICMS-RJ (Dec. 27.427/2000), só o Livro IX — prestação de transporte (art. 82-C) | trc | rj | 333 | 15.326 | `795a9cb2b9ec` |
| `RJ-DEC-27815-2001.txt` | Decreto estadual RJ nº 27.815, de 24/01/2001 — aprova o **Manual de Diferimento, Ampliação de Prazo de Recolhimento, Suspensão e de Incentivos e Benefícios de Natureza Tributária** | transversal | rj | 7 | 216 | `1930ecbb5cc9` |
| `RJ-MANUAL-BENEFICIOS.txt` | Manual de Benefícios (Dec. 27.815/2001) — **redação vigente**; apresentação v3 (Port. SUT 323/2020), última atualização SUPTRIB/MB nº 05/26, de 13/07/2026. Verbete *Prestação de serviço de transporte*: Conv. ICMS 106/1996 — crédito presumido — prazo indeterminado | transversal | rj | 22 | 33.138 | `0f068df99a3a` |
| `RJ-MANUAL-BENEFICIOS-2001.txt` | Manual de Benefícios — **redação original de 25/01/2001**, camada superada. Guarda a descrição do benefício, que a redação vigente não repete | transversal | rj | 135 | 24.042 | `9ae007b202f5` |
| `RJ-LEI-8645-2019-FOT.txt` | Lei estadual RJ nº 8.645, de 09/12/2019 — institui o FOT; compilada c/ a Lei 11.071/2025 | transversal | rj | 40 | 2.597 | `b123ee5869c1` |
| `RJ-LEI-11071-2025-FOT.txt` | Lei estadual RJ nº 11.071, de 22/12/2025 — altera a Lei 8.645/2019: escalonamento do FOT e vigência até 31/12/2032 | transversal | rj | 26 | 1.334 | `f26529ce15b9` |
| `RJ-POR-SUCIEF-65-2019.txt` | Portaria SUCIEF nº 65, de 15/08/2019 — códigos da tabela 5.2 da EFD vinculados ao Manual. **RJ805149 = Conv. ICMS 106/1996 — crédito presumido**, início 01/04/2019, sem data-fim | transversal | rj | 17 | 8.615 | `13f0e8e7e958` |
| `RJ-RES-SEFAZ-720-2014-ANEXO-XIII.txt` | Resolução SEFAZ RJ nº 720/2014, Parte II — **Anexo XIII**: armazém geral (Cap. II, arts. 7º a 19) | transversal | rj | 1.082 | 33.990 | `9a08ea1af502` |
| `RJ-RES-SEFAZ-720-2014-ANEXO-XVIII.txt` | Resolução SEFAZ RJ nº 720/2014, Parte II — **Anexo XVIII**: escrituração de benefícios. Art. 10 (E115) e art. 12 (estorno RJ018003 + crédito presumido RJ028001) | transversal | rj | 94 | 4.127 | `697e6f1ffde8` |
| `RJ-RES-SEFAZ-720-2014-ANEXO-XXIII.txt` | Resolução SEFAZ RJ nº 720/2014, Parte II — **Anexo XXIII**: depósito no FOT na EFD (RJ050019). Alínea `c` do inc. II do art. 2º **REVOGADA** pela Res. SEFAZ 892/2026 | transversal | rj | 19 | 838 | `44d57c55152a` |
| `RJ-RES-SEFAZ-720-2014-ANEXO-XXV.txt` | Resolução SEFAZ RJ nº 720/2014, Parte II — **Anexo XXV**: contribuinte com decisão judicial suspendendo a exigibilidade | transversal | rj | 17 | 620 | `91919d5a1073` |
| `RJ-RES-SEFAZ-875-2026.txt` | Resolução SEFAZ RJ nº 875, de 20/03/2026 — ferramenta de cálculo do FOT e **Anexo Único** de classificação dos benefícios (≈190 atos; só Decreto e Lei estaduais — **nenhum convênio**) | transversal | rj | 36 | 9.491 | `48e305fbf244` |
| `CONV-ICMS-100-2001.txt` | Convênio ICMS 100/01 — autoriza dez UFs a revogar o crédito presumido no transporte **dutoviário**. **O RJ não está na lista** | trc | nacional | 1 | 1.397 | `9a02c1c1991c` |
| `CONV-ICMS-190-2017.txt` | Convênio ICMS 190/17 — remissão e reinstituição de benefícios instituídos **em desacordo** com a alínea `g` do inc. XII do § 2º do art. 155 da CF | transversal | nacional | 243 | 10.192 | `eeb578f91d9f` |
| `LC-160-2017.txt` | Lei Complementar nº 160, de 07/08/2017 — moldura da remissão/reinstituição de benefícios **unilaterais**. Art. 3º, § 2º: prazos-limite | transversal | federal | 80 | 2.419 | `87860c24590d` |

**Resumo:** 60 normas — 48 transversais, 12 de TRC. Por jurisdição: 35 federais, 8 nacionais, 17 do RJ.

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
(art. 28, § 11, da Lei 8.212, com o correspondente salário-de-contribuição do art. 28, § 11) e
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

## Incorporação de 03/08/2026 (terceiro lote) — o eixo do IRPJ e da CSLL

Duas normas: a Lei nº 9.249, de 26/12/1995, e a Lei nº 9.430, de 27/12/1996, ambas na versão
**compilada**. Proveniência: captura própria do Planalto em 03/08/2026, às 17h17, em PDF de
impressão da página oficial (`l9249.htm` e `l9430.htm`).

**Por que entram, e a que se ligam.** São a sede do imposto de renda da pessoa jurídica e da
contribuição sobre o lucro — os dois tributos que a reforma do consumo **não** alcança e que,
por isso, atravessam intactos a transição. Três elos concretos com o acervo:

1. **O percentual do transporte de carga.** O art. 15, § 1º, II, `a`, da Lei 9.249 põe os serviços
   de transporte em 16% de presunção **e excetua expressamente o de carga**, que segue o caput —
   **8%**. A base da CSLL correspondente é de 12% (art. 20, III). É o marco de comparação do
   lucro presumido para a transportadora, que até agora estava fora do acervo.
2. **A reforma tocou as duas leis em três pontos.** O art. 502 da LC 214/2025 dá nova redação ao
   caput do art. 64 da Lei 9.430 (a retenção federal passa a alcançar só IR e CSLL) e o art. 542,
   V, revoga a partir de 1º/01/2027 os §§ 7º e 8º do mesmo art. 64 e o art. 66 — as pernas de
   PIS/COFINS. E o art. 81, VIII, da Lei 9.430, **incluído pela LC 227/2026**, torna inapta a
   inscrição no CNPJ de quem praticar reiteradamente as infrações do art. 471-D da LC 214/2025 —
   as do *split payment*, dirigidas ao prestador de serviço de pagamento e ao operador de sistema
   de pagamento, na forma do art. 471-E.
3. **Fecha-se o circuito das alteradoras.** A LC 224/2025 e a Lei 15.270/2025 já estavam no acervo
   **como leis alteradoras, sem o texto alterado**. Agora estão as duas pontas: o IRRF de 17,5%
   sobre juros sobre capital próprio (art. 9º, § 2º, da Lei 9.249, red. LC 224/2025) e a
   tributação dos dividendos remetidos ao exterior a 10%, com o crédito do art. 10-A (red. Lei
   15.270/2025), leem-se agora no próprio dispositivo.

**Método de extração.** `pdftotext -layout -enc UTF-8` e `limpar_pdf.py`, pelo motivo já
documentado nas duas seções anteriores. O modo padrão foi rodado em paralelo, só para prova, e
**corromperia 5 termos**: `utilizá-lo` e `intimá-lo` na Lei 9.430; `trimestre-calendário`,
`ano-base` e `ano-calendário` na Lei 9.249. Nenhum deles entrou no acervo.

Reparos de pré-processamento, sem tocar o texto normativo: quebras de página (48 + 13), cabeçalho
de página (48 + 13), rodapé (48 + 13) e junção de hífen de fim de linha (2 + 3). As 5 junções
foram conferidas **uma a uma** — todas são hífen legítimo (ênclise pronominal e palavra composta);
nenhuma é silabação. Zero caractere de controle não mapeado; zero palavra perdida na conferência
do `normalizar.py`.

**O medidor foi provado antes de medir**, como manda a regra da casa: a `LC-214-2025.txt` devolveu
**126.519** palavras, exatamente o registro desta tabela. Só então se contaram as duas novas.

Provas de conteúdo executadas e aprovadas. **Lei 9.249** — art. 3º (caput e §§ 1º-4º, nas duas
redações); art. 9º, § 2º (17,5%, LC 224/2025); arts. 10 e 10-A (Lei 15.270/2025, inclusive o § 5º,
I a II); art. 13; **art. 15 (caput, § 1º, I a IV, e §§ 2º-4º)**; art. 20, I a III; art. 34,
§§ 3º-4º (LC 225/2026); fecho com assinaturas. **Lei 9.430** — arts. 1º, 2º, 9º-A, 25, 27; art. 44
(caput, I e II, § 1º, VI-VII, § 1º-A e § 1º-C); art. 64 (caput e §§ 7º-8º); art. 66; art. 74
(inclusive § 12, II, `g` e `h`, red. Lei 15.265/2025) e art. 74-A; **art. 81, VIII (LC 227/2026)**;
art. 83, § 5º, I-II e § 7º (LC 225/2026); fecho com assinaturas.

**Camada de 2027 fora do arquivo, registrada.** Como já sucedeu com a LC 123 (cuja camada de 2027
vive no art. 517 da LC 214) e com a Lei 8.212 (Lei 15.371/2026), o compilado do Planalto da
Lei 9.430 traz no cabeçalho apenas "Vide Lei Complementar nº 214, de 2025 — Produção de efeitos",
**sem** incorporar-lhe o conteúdo ao corpo: o art. 64 aparece com a redação antiga, ainda com
COFINS e PIS/PASEP. A redação que vale a partir de 1º/01/2027 e as revogações estão nos arts. 502
e 542, V, da `LC-214-2025.txt`. **As duas peças leem-se juntas.**

**Defeito da fonte — confirmado no HTML oficial em 03/08/2026.** O arquivo traz **748 ocorrências
de `pela` contra 1 de `pelo`**, e ao menos **103 delas estão em lugar de `pelo`**: "pela sujeito
passivo" (17), "pela contribuinte" (12), "pela art." (9), "pela valor" (7), "pela inciso" (7),
"pela método" (6), "pela pagamento" (5), "pela Banco Central" (4), "pela juiz", "pela Supremo",
"pela Senado", "pela órgão", "pela devedor", entre outras.

A causa foi **determinada**, e não é nossa. O sócio capturou o HTML da página oficial e o confronto
devolveu **exatamente a mesma contagem — 748 `pela` contra 1 `pelo`** — na marcação original, antes
de qualquer extração. A substituição está **na página do Planalto**. Não é do extrator (as demais
palavras em `-o` estão íntegras: `prazo` 57, `imposto` 129, `lucro` 107, `artigo` 113), não é da
impressão em PDF, e não é do tratamento: a Lei 9.249, do mesmo lote e método, traz `pelo`
corretamente 31 vezes. A única sobrevivente de `pelo` no arquivo está no art. 9º-A, acrescido pela
Lei 14.043/2020 — dispositivo dos mais recentes, o que sugere substituição global feita na página
em algum momento, com o texto acrescido depois escapando dela. **A sugestão não se afirma**: só a
medição está provada.

Consequência prática: o conteúdo normativo está completo (35.501 palavras, zero perdidas na
conferência) e nenhum dispositivo se alterou em substância, mas busca por "pelo sujeito passivo"
**falha** e citação literal reproduziria a preposição da página. Pela regra da casa — **não se
emenda o texto sem o original à vista**, e aqui o original **é** o texto com o defeito —, o arquivo
entra como capturado. **Recomenda-se capturar a página compilada**
(`https://www.planalto.gov.br/ccivil_03/leis/L9430compilada.htm`, cujo link está no alto da própria
página-base): é artefato distinto, pode não carregar o defeito, e é a convenção da casa para as
leis federais — `l10637compilado`, `l10.833compilado`, `l5172compilado`, `l8036consol`,
`l8212cons`. Substituindo-se o arquivo, muda o SHA-256 desta tabela e a URL do `fontes.tsv`.

**Achado que excede estas duas normas: o tachado se perde na extração.** A conferência do HTML
mostrou **695 blocos tachados** (`<strike>` e `line-through`) somando **18.196 palavras — 51% do
arquivo**. São as redações revogadas ou superadas, que a página oficial distingue **visualmente** e
que o texto puro **não distingue de modo algum**: no `.txt`, a redação velha e a nova ficam em
parágrafos consecutivos, sem marca. Quem ler o art. 15 da Lei 9.249 pela primeira ocorrência lê a
redação anterior à Lei 12.973/2014.

O sintoma é mensurável em todo o acervo, e **não é próprio destas duas normas**: contando os
dispositivos cujo cabeçalho `Art. N` aparece mais de uma vez no mesmo arquivo — proxy conservador
de redação empilhada —, obtêm-se `LEI-8036-1990` 48%, `RJ-LEI-2657-1996` 34%, `LEI-9430-1996` 30%,
`LEI-8212-1991` 29%, `LC-227-2026` 20%, `LEI-10833-2003` 20%, `LEI-10637-2002` 19%,
`LEI-9249-1995` 14%, `LC-214-2025` 6%. Os regulamentos novos (`DEC-12955-2026`,
`RES-CGIBS-6-2026`) e o CTN dão zero. **A página "compilada" do Planalto não resolve**: a
`LEI-10833-2003`, capturada de `l10.833compilado.htm`, dá 20%.

**O tachado não é marcador de vigência — medido no mesmo HTML, e isto reduz o peso do achado
anterior.** Classificados os 639 blocos tachados com texto, o tachado marca coisas heterogêneas:
160 trazem "(Incluído por …)" e 98 "(Redação dada por …)" — são versões que *vigeram* e foram
substituídas; 27 são versões de medida provisória "(Sem eficácia)", que nunca vigeram; 27 trazem
"(Revogado)"; e **262 não trazem nota alguma** (redação originária de 1996, depois substituída).

E, sobretudo, o **inverso**: das 59 notas "(Revogado pela …)" da página, **32 estão FORA do
tachado**. Quem tomasse "não tachado = vigente" leria como em vigor todo o capítulo de preços de
transferência da Lei 9.430 — arts. 18 a 24-B —, **revogado pela Lei 14.596/2023**, que na página
aparece em tipo normal.

Conclusão que corrige a redação anterior desta seção: **o sinal de vigência nunca foi o tachado —
é a nota entre parênteses, e a nota sobrevive íntegra no `.txt`.** As 15 ocorrências de "(Revogado
pela Lei nº 14.596, de 2023)" estão no arquivo do acervo. O que se perde na extração é um atalho
visual que, na própria fonte, é ambíguo nos dois sentidos. A regra de leitura não muda e não é nova:
**ler o artigo inteiro até o fecho e conferir a nota**; e, quando a nota remeter a lei com produção
de efeitos diferida, **ir à lei alteradora** — foi assim que se apanharam a camada de 2027 da LC 123
(art. 517 da LC 214), a da Lei 8.212 (Lei 15.371/2026) e a desta Lei 9.430 (arts. 502 e 542, V, da
LC 214).

**Instrumento criado nesta sessão: `camadas.py`.** Devolve o atalho perdido **sem tocar em texto
nenhum** — nenhum SHA muda. Separa as camadas de um dispositivo, imprime as notas oficiais de cada
uma e classifica em REDAÇÃO SUPERADA, REVOGADO e SEM EFICÁCIA. Provado, antes de usado, em oito
casos de resposta conhecida: art. 2º da Lei 9.430 (vige a redação da Lei 12.973/2014), art. 18 da
mesma lei (revogado pela Lei 14.596/2023), art. 44 (vige, apesar de incisos revogados), art. 15 da
Lei 9.249, art. 15 da Lei 8.036, arts. 47 e 169 da LC 214 e art. 3º da LC 123. **O primeiro ensaio
reprovou o instrumento**: sem restringir a leitura ao caput, as notas dos parágrafos entravam na
conta e o art. 44 saía como revogado. Corrigido e reprovado — é a sexta vez neste projeto que o
medidor erra antes da construção.

Auditoria que ele devolve sobre o acervo de 26 normas: **202 dispositivos com redação empilhada**,
dos quais 91 com a última camada sem nota no caput. A concentração é toda em lei antiga —
`RJ-LEI-2657-1996` 42, `LEI-8212-1991` 33, `LEI-9430-1996` 27, `LEI-8036-1990` 25, `LC-123-2006` 21,
`LEI-10833-2003` 16, `RES-CGSN-140-2018` 15. **A espinha dorsal da reforma dá zero**: `LC-214-2025`,
`LC-227-2026`, `DEC-12955-2026`, `LEI-5172-1966`, `LC-224-2025` e `LEI-15270-2025` não têm um só
dispositivo empilhado, e a `RES-CGIBS-6-2026` tem um.

Uma convenção de marcação no acervo (prefixar o bloco superado) daria o atalho de volta, mas
**alteraria o texto** e o SHA de quase todos os arquivos — e teria de decidir, bloco a bloco, entre
"superado", "revogado" e "sem eficácia", que são coisas juridicamente distintas. É decisão do sócio,
não do assistente.

## Incorporação de 04/08/2026 — a Lei 12.546 e o caminho novo de captura

**Uma norma e um instrumento.** A Lei nº 12.546, de 14/12/2011, na versão **compilada**, é a
primeira norma do acervo erguida de **página HTML salva**, e não de PDF de impressão.
Proveniência: captura própria do sócio em 04/08/2026, `l12546compilado.htm`.

**Por que o caminho mudou.** A página-base desta lei carrega os Anexos I e II com centenas de
códigos NCM; impressa, vira PDF de centenas de páginas, que o canal de envio recusa. A página
**compilada** não tem esse peso — os dois anexos foram revogados pela Lei 13.670/2018 e aparecem
como uma linha. E a página salva em HTML é **melhor fonte** que o PDF: foi nela que se provou que
o defeito `pela`/`pelo` da Lei 9.430 era do Planalto, e que se mediram os 695 blocos tachados.
O PDF descarta essa informação.

**O instrumento: `limpar_html.py`.** Descarta script, estilo, comentário e o `<head>`; converte
elementos de bloco em quebra de linha; remove a marcação restante **sem espaço no lugar**, porque
no Planalto ela cai dentro da palavra; resolve entidades; normaliza espaço. A saída ainda passa
pelo `normalizar.py`, como no caminho do PDF. Mede e **relata** o tachado, mas não o marca no
texto — a distinção lê-se pela nota entre parênteses, na forma do `camadas.py`.

**Provado antes de usado, e reprovado na primeira.** O ensaio foi reprocessar pelo HTML a
`LEI-9430-1996.txt`, já publicada, e comparar palavra por palavra. Na primeira versão o
instrumento trocava a marcação por espaço e **partia 226 palavras**: `1º` virava `1 o`,
`Sem eficácia` virava `S em eficácia`. Corrigido o tratamento da marcação intrapalavra, os dois
caminhos convergiram.

**O ensaio apanhou defeito no arquivo já publicado.** Restaram 18 divergências, e **em todas o
HTML está certo e o PDF errado**: o `pdftotext -layout` desloca o ordinal sobrescrito, e a
`LEI-9430-1996.txt` traz, por exemplo, `. o § 2 Nas operações` onde a norma diz `. § 2o Nas
operações`. São 18 ocorrências, todas de ordinal, nenhuma altera substância — mas ficam
registradas, e reforçam a recomendação de recapturar em HTML os arquivos vindos de PDF. Fica
como débito, junto do commit de renormalização geral.

**Números da conversão.** 762 `<p>`, 52 `<blockquote>`, 4 `<td>`, 2 `<h1>`, entre outros, viraram
quebra de linha; 2.786 marcações removidas; 1 script e 1 comentário descartados. Resultado: 374
linhas, **12.036 palavras**, zero perdidas na conferência do `normalizar.py`. Apenas **15 blocos
tachados, 92 palavras** — a página compilada quase não carrega redação superada, ao contrário da
página-base da Lei 9.430, com 51%.

**Por que a norma entra, e o que ela destrava.** É a última perna do eixo do custo do trabalho,
ao lado da Lei 8.212 e da Lei 8.036. Sem ela não se compara o regime federal do cliente:
o transporte rodoviário de cargas está expressamente no art. 8º, IX, e paga **1,5% sobre a receita
bruta** em vez de 20% sobre a folha. E revela o que o simulador terá de modelar: **a desoneração
morre no mesmo intervalo em que o IBS/CBS nasce.** São duas transições sobrepostas, cada uma com
proporção anual própria — em 2026, 60% da alíquota sobre receita somados a 50% da folha. É o caso
exemplar do § 4.3 do PRD: regra é dado com vigência, nunca código.

**Dependência declarada.** O art. 9º-A e a redação atual dos arts. 7º e 8º são obra da
**Lei 14.973/2024**, que **não está no acervo**. O escalonamento pode ser lido aqui, mas a lei
alteradora não foi conferida no oficial. Continua na lista de faltantes, agora como prioridade.

Provas de conteúdo executadas e aprovadas: art. 7º e 7º-A; art. 8º, caput e IX; art. 8º-A;
art. 9º, II, `b`, e § 13; art. 9º-A, I a III; art. 9º-B; art. 52 e fecho com as oito assinaturas,
a nota do DOU de 15.12.2011 e os dois anexos revogados. `camadas.py` devolve camada única para os
arts. 7º-A, 8º, 8º-A, 9º-A e 9º-B.

## Incorporação de 04/08/2026 (segundo lote) — o eixo da renda

Cinco normas, todas erguidas de **página HTML salva** pelo caminho estreado horas antes, com o
`limpar_html.py`. Proveniência: captura própria do sócio em 04/08/2026.

| Arquivo | Página capturada | Palavras | Tachado na página |
|---|---|---:|---:|
| `LEI-7689-1988` | `l7689.htm` | 3.058 | 45 blocos · 1.516 palavras |
| `LEI-9250-1995` | `l9250.htm` | 16.231 | 203 blocos · 5.291 palavras |
| `LEI-9718-1998` | `l9718.htm` | 11.647 | 255 blocos · 6.518 palavras |
| `LEI-14789-2023` | `l14789.htm` | 3.001 | **zero** |
| `DEC-9580-2018` | `d9580.htm` | 197.573 | 2 blocos · 72 palavras |

Zero palavra perdida nas cinco conferências do `normalizar.py`. O Regulamento do Imposto sobre a
Renda entra como a maior peça do acervo — **197.573 palavras**, mais de uma vez e meia a LC 214.

**O que cada uma destrava.** A `LEI-7689-1988` é a alíquota da CSLL, sem a qual não há linha de
contribuição sobre o lucro em comparativo nenhum. A `LEI-9718-1998` é o **regime cumulativo** de
PIS/COFINS — o que o lucro presumido paga —, contraparte que faltava para comparar a CBS: o acervo
tinha as duas leis do não cumulativo e nenhuma do cumulativo. A `LEI-9250-1995` fecha o circuito
da Lei 15.270/2025, que estava no acervo como lei alteradora sem o texto alterado. A
`LEI-14789-2023` decide se o crédito presumido do transporte entra na base do IRPJ. E o
`DEC-9580-2018` costura tudo.

**Dois dispositivos do RIR que interessam diretamente ao transporte**, lidos no texto: o
**art. 591**, que põe a base do lucro presumido em oito por cento sobre a receita bruta; e o
dispositivo do rendimento do transportador autônomo, que fixa **dez por cento do rendimento total
no transporte de carga** e sessenta por cento no de passageiros, com a ressalva expressa de que o
**vale-pedágio obrigatório não integra** esse rendimento, na forma da Lei 10.209/2001. É o
tratamento de IRPF do TAC — que o acervo até agora não tinha, e que se soma ao art. 28, § 11, da
Lei 8.212 para dar o custo total do autônomo.

**Duas ressalvas de proveniência, declaradas.** A `LEI-9718-1998` e a `LEI-9250-1995` vieram da
**página-base**, não da compilada. Para a Lei 9.718 existe compilada (`l9718compilada.htm`,
endereço visto retornar do Planalto); para a Lei 9.250 não se verificou. Não é defeito — a
página-base é texto oficial —, mas destoa da convenção da casa e explica o volume de redação
empilhada nas duas. Recaptura fica recomendada, não urgente.

**Característica de fonte medida, não emendada.** A `LEI-9718-1998` mistura as duas grafias do
ordinal: **367 ocorrências de `º` e 46 de `°`** (sinal de grau). A `LEI-9250-1995` tem 9 de `°`.
Busca por `Art. 8º` **falha** onde a página escreveu `Art. 8°`. O `camadas.py` já aceita as três
grafias; o `grep` humano não. Está registrado no `CLAUDE.md`.

**Dependência que continua aberta.** A `LEI-14789-2023` responde pela regra geral das subvenções,
mas quem afasta o crédito presumido do Convênio 106/96 dessa regra é a **Solução de Consulta COSIT
nº 6/2026**, que não está no acervo e cuja leitura no oficial ainda não se fez.

Provas de conteúdo executadas e aprovadas: **Lei 7.689** — art. 3º nas três camadas, com a vigente
identificada pela nota da Lei 11.727/2008; fecho no art. 13 e nota do DOU de 16.12.1988.
**Lei 9.250** — arts. 6º-A, 16-A e 16-B em camada única; art. 42 e fecho. **Lei 9.718** — arts. 2º,
3º e 8º, este com a marca da LC 214/2025; fecho e assinaturas de 27/11/1998. **Lei 14.789** —
arts. 1º, 6º e 8º; fecho, assinaturas e nota da edição extra do DOU de 29.12.2023. **RIR/2018** —
art. 591; dispositivo do transportador autônomo; assinaturas de Michel Temer e Eduardo Refinetti
Guardia, nota do DOU de 23.11.2018, abertura do Anexo e fecho no art. 1.050.

## Incorporação de 04/08/2026 (terceiro lote) — o fecho do eixo da folha

Cinco normas, pelo caminho do HTML. Quatro do Planalto e **uma do Diário Oficial da União** — a
primeira do acervo com essa proveniência.

| Arquivo | Página capturada | Palavras | Tachado |
|---|---|---:|---:|
| `DEC-3048-1999` | `d3048compilado.htm` | 131.023 | 512 blocos · 0 palavras |
| `LEI-14973-2024` | `l14973.htm` | 9.120 | 6 blocos · 284 palavras |
| `LEI-15371-2026` | `in.gov.br` (DOU) | 3.114 | zero |
| `LEI-10666-2003` | `l10.666compilado.htm` | 1.327 | zero |
| `LEI-8706-1993` | `l8706.htm` | 1.213 | 1 bloco · 54 palavras |

Zero palavra perdida nas cinco conferências.

**Prova de reprodutibilidade, obtida de graça.** O sócio reenviou, junto deste lote, uma
**recaptura independente** da página da Lei 12.546, feita em momento diverso — o arquivo HTML
sequer tem o mesmo tamanho do primeiro. Processada pelo mesmo rito, devolveu **SHA-256 idêntico**,
`0f9aafcd742a`, ao arquivo já publicado. Duas capturas independentes da mesma página produzem o
mesmo arquivo: o caminho do HTML é reprodutível, e não só verificável.

**O instrumento aprendeu o DOU.** As páginas da Imprensa Nacional vêm embrulhadas em portal — menu,
rodapé, redes sociais. Na primeira tentativa entraram **97 linhas de navegação**, de "Ir para o
conteúdo" a "Facebook". Acrescentou-se ao `limpar_html.py` o recorte do miolo entre
`<div class="cabecalho-dou">` e o rodapé. O resultado guarda o cabeçalho de publicação — órgão,
seção, edição, data — que é justamente a prova de proveniência que o DOU dá e o Planalto não.
Fica registrado que o próprio DOU adverte: *"Este conteúdo não substitui o publicado na versão
certificada."*

**Por que estas cinco fecham o eixo da folha.** A Lei 8.212 dá a contribuição patronal e o RAT,
mas remete a regulamento o enquadramento por atividade econômica — que mora no **`DEC-3048-1999`**.
A **`LEI-10666-2003`** traz o FAP, que no art. 10 permite **reduzir o RAT em até 50% ou aumentá-lo
em até 100%** conforme o desempenho da empresa: sem ele, o custo de folha do simulador é faixa, e
não número. A **`LEI-14973-2024`** é a lei que reescreveu os arts. 7º e 8º da Lei 12.546 e
acrescentou os arts. 9º-A e 9º-B — a dependência declarada horas antes, agora fechada; e o seu
art. 4º condiciona a opção a manter **quadro funcional médio de ao menos 75%** do ano anterior,
condição que o simulador terá de checar antes de aplicar a alíquota sobre receita. A
**`LEI-15371-2026`** é a camada de 2027 que o compilado da Lei 8.212 não incorpora. E a
**`LEI-8706-1993`** dá os **1,5% do SEST e 1,0% do SENAT** sobre o salário de contribuição do
transportador autônomo (art. 7º, II) — 2,5% que se somam aos 20% sobre 20% da nota do art. 22,
§ 15, da Lei 8.212. Com isso o custo do TAC pode enfim ser somado por inteiro: previdenciário,
terceiros do transporte e IRPF pelo RIR.

**Classificação declarada.** A `LEI-8706-1993` entra como **`trc`**, e não como transversal: a lei
inteira é do setor de transporte, não apenas um dispositivo seu. É o critério do TAXONOMIA — a
norma é que se classifica. Sobem para cinco as normas setoriais.

**Defeito conhecido, agora visível.** A `LEI-10666-2003.txt` saiu com **13 linhas para 1.327
palavras**: a página escreve os ordinais como `Art. 1o`, com a letra `o`, e o `normalizar.py` não
quebra linha nesse padrão — defeito medido e registrado em 03/08/2026, ainda não corrigido. O
conteúdo está íntegro e a conferência não perdeu palavra; o que se perde é a legibilidade por
linha. Reforça o commit de renormalização geral, que continua pendente.

Provas de conteúdo executadas e aprovadas: **Lei 8.706** — art. 7º, II, com os percentuais do SEST
e do SENAT; 12 ocorrências de cada sigla. **Lei 10.666** — art. 10, com a redução de até cinquenta
e a majoração de até cem por cento. **Lei 14.973** — art. 1º, com a nova redação dos arts. 7º e 8º
da Lei 12.546, e art. 4º, com o compromisso dos 75%. **Lei 15.371** — art. 7º, que altera o art. 28
da Lei 8.212, e art. 14, com a vigência em 1º/01/2027; fecho com as assinaturas e a advertência do
DOU. **RPS** — 512 blocos tachados conferidos: envolvem apenas o sinal de ordinal, nenhuma palavra.

## Renormalização geral de 04/08/2026 — dívida técnica nº 1 do RTI nº 004

**O defeito.** O `normalizar.py` só reconhecia duas das três grafias do ordinal — `º` e `°` —, e
não a letra `o`. Artigos e parágrafos escritos `Art. 1o` e `§ 2o` não quebravam linha. O caso
extremo foi a `LEI-10666-2003.txt`, que entrou com **treze linhas para mil trezentas e vinte e
sete palavras**. Medido em 03/08/2026, corrigido hoje: a classe passou a `[ºo°]` no padrão do
artigo e no do parágrafo.

**Nenhum conteúdo mudou, e isto foi provado arquivo a arquivo.** O `conferir()` do próprio
`normalizar.py` compara os fluxos de palavras antes e depois e aborta se divergirem. Os trinta e
sete arquivos passaram; **zero falhas de conteúdo**. O que mudou foi onde a linha quebra.

**Dezenove arquivos saíram byte a byte idênticos** — prova de que a rotina é idempotente e de que
a correção não mexe onde não devia.

**Quinze arquivos ganharam quebras, e a causa é a corrigida.** Todos têm ocorrências de `Art. No`
ou `§ No`: `LEI-10833-2003` (26 e 370), `LEI-10637-2002` (11 e 173), `LEI-8212-1991` (196 no
parágrafo), `DEC-3048-1999` (139), `LEI-9430-1996` (136), e assim por diante. A Lei 10.666 passou
de treze para quarenta e três linhas.

**Três arquivos foram REFLUÍDOS, e a causa é outra — declara-se.** A `LC-123-2006`, a
`RES-CGSN-140-2018` e a `RES-CGSN-186-2026` **nunca haviam passado por este normalizador**:
conservavam a quebra de linha da própria fonte, com largura média de 47, 48 e 79 caracteres por
linha — o texto vinha embrulhado como no documento de origem, e não quebrado por dispositivo.
Ao passarem pela rotina, foram reagrupadas no formato canônico do acervo: uma linha por
dispositivo. A `LC-123-2006` foi de 6.223 para 1.583 linhas; a `RES-CGSN-140-2018`, de 7.959 para
2.147. **O conteúdo é o mesmo, palavra por palavra** — o `git diff` é que fica enorme, porque
compara embrulhos diferentes. Ganha-se com isso o que o acervo perseguia desde o início: diferença
legível por dispositivo, e não por largura de página.

**Consequência para o banco.** Dezoito assinaturas mudaram. A tabela `normas` do projeto
`analise-rt` espelha essas assinaturas e ficou defasada no instante em que este commit subiu.
Acompanha a este lote o arquivo `atualizar-normas-v2.sql`, que refaz o espelho. **Sem ele, o
sistema citaria número conferido contra versão que já não existe** — exatamente o que a coluna
`sha256` foi criada para impedir.

## Recaptura em HTML de 04/08/2026 — dez normas, e um defeito que ninguém medira

**O que se procurava.** Corrigir, nos arquivos vindos de documento impresso, o ordinal sobrescrito
que o `pdftotext` desloca. **O que se achou** foi mais grave: **resíduo de impressão dentro do
texto normativo**. Sete arquivos dos lotes de 16 a 21 de julho — anteriores ao `limpar_pdf.py` —
carregavam **227 carimbos de data-hora e 243 endereços de internet** entre os dispositivos. Não
corrompiam palavra: acrescentavam texto estranho, que sairia junto em qualquer citação literal.

| Arquivo | Antes | Agora | Carimbos | URLs |
|---|---:|---:|---|---|
| `LC-227-2026` | 61.623 | 59.545 | 104 → 0 | 104 → 0 |
| `LEI-10833-2003` | 39.807 | 38.715 | 54 → 0 | 55 → 1 |
| `EC-132-2023` | 14.770 | 14.094 | 29 → 0 | 29 → 0 |
| `LEI-10637-2002` | 18.003 | 17.514 | 25 → 0 | 25 → 0 |
| `LEI-11442-2007` | 6.423 | 6.207 | 9 → 0 | 9 → 0 |
| `LC-192-2022` | 3.734 | 3.614 | 6 → 0 | 6 → 0 |

A única URL remanescente é **do próprio texto legal** — o art. 32 da Lei 10.833 manda a Receita
divulgar ato no seu sítio, e o endereço está na norma. Fica.

**Erro de proveniência, anterior a esta sessão, corrigido.** O `fontes.tsv` registrava a Lei 10.637
e a Lei 10.833 como capturadas da página compilada. Não foram: o carimbo preservado dentro do
arquivo publicado dizia `20/07/2026, 12:34 L10637` — título da **página-base**. As duas URLs foram
retificadas.

**Troca de artefato na Lei 8.212, decidida pelo sócio.** O acervo trazia a página **consolidada**
(`l8212cons.htm`, 48.938 palavras); passa a trazer a **compilada** (`l8212compilado.htm`, 23.961).
Mediu-se o custo antes de aplicar: **nenhum artigo se perde** — o confronto dos cabeçalhos devolveu
conjunto vazio. Perde-se apenas a redação superada: o art. 31 vai de sete camadas para uma, o
art. 43 de duas para uma. **Os dispositivos que a semente do banco cita continuam lá**, conferidos
um a um: art. 22, incisos I, II e III, e **art. 28, § 11** — a base previdenciária do transportador
autônomo, com a mesma numeração.

**Três recapturas de ganho puro.** A `LEI-9249-1995` conserta o ordinal deslocado (`o § 2 O valor`
→ `§ 2o O valor`). A `LEI-9430-1996` conserta dezoito ordinais. A `LC-123-2006` desfaz colagens que
o documento impresso produzira: `anocalendário` (2 → 0), e as variáveis das fórmulas dos anexos,
`XP` (40 → 0) e `Nx` (20 → 0).

**O instrumento reprovou de novo, e foi corrigido.** A primeira passagem pela Emenda Constitucional
132 produziu palavras coladas — `docaputdeste`, `ocaputpoderão`. A causa: aquela página **usa margem
de estilo no lugar do espaço**, escrevendo `do<strong style="margin-left:4px">caput</strong>deste`.
O `limpar_html.py` passou a converter em espaço a marcação que carrega `margin-left` ou
`margin-right`. Reprovado no ensaio de resposta conhecida da Lei 9.430 — devolveu as mesmas 35.483
palavras — e então aplicado. Varreu-se em seguida todo o acervo à procura de colagens: **zero**,
inclusive nos onze arquivos que já haviam entrado por HTML.

**O vício das preposições da Lei 9.430 NÃO tem conserto.** A página compilada foi capturada e
medida: **332 ocorrências de `pela` contra 1 de `pelo`**, com `pela sujeito passivo` seis vezes.
Está nas duas páginas do Planalto. Encerra-se a dívida que previa recaptura como remédio: não há.

## Incorporação de 04/08/2026 (quarto lote) — o eixo setorial e a lacuna do PIS

Oito normas, todas por página salva. **Quatro do Planalto, três da ANTT — duas do sistema próprio
de legislação e uma do Diário Oficial — e uma do portal da SEFAZ-RJ.** O acervo passa de trinta e
sete a **quarenta e cinco normas**, e as setoriais dobram, de cinco para dez.

**A que fecha uma lacuna do banco.** A `LEI-9715-1998` traz, no art. 8º, inciso I, a alíquota de
**zero vírgula sessenta e cinco por cento sobre o faturamento** — a contribuição para o PIS no
regime cumulativo, que é o do lucro presumido. A semente de hoje gravara esse parâmetro como
**pendente, com valor nulo**, precisamente porque a norma não estava no acervo e a regra da casa
proíbe afirmar de memória. Agora pode ser preenchido, e o comparador fecha a linha. O dispositivo
traz marca de produção de efeitos pela LC 214/2025.

**A que cinco arquivos já citavam.** A `LC-225-2026` — devedor contumaz — era invocada pelo
Decreto 12.955 e pelas Leis 9.249, 9.430 e 10.637, e não estava no acervo. Foi erro do assistente
tê-la relacionado, no comando de pesquisa de hoje, entre as normas já presentes; ficou consignado
no Registro nº 004 e agora se resolve.

**O eixo do transportador autônomo, completo.** A `LEI-10209-2001` fecha o vale-pedágio: o valor
**não integra o frete**, a responsabilidade é do embarcador, e o art. 8º impõe indenização de
**duas vezes o valor do frete** em caso de infração. É a lei a que remete o art. 39, § 1º, do
Regulamento do Imposto sobre a Renda, que já estava no acervo apontando para o vazio. Somam-se a
`LEI-13703-2018`, dos pisos mínimos, e a `RES-ANTT-6084-2026`, com a tabela vigente de
coeficientes; e as Resoluções ANTT nº 5.982 e nº 6.068, que regem o registro nacional de
transportadores e o vinculam aos seguros obrigatórios — base do Parecer nº 02.

**O instrumento aprendeu dois portais novos, e reprovou duas vezes antes.** O sistema de
legislação da ANTT embrulha o ato em ementário, busca e um "Carregando..." final; o portal da
SEFAZ-RJ, entre barra de acessibilidade e caixa de busca. Sem recorte, entravam no texto normativo
linhas como "EMENTÁRIO PUBLICAÇÕES DO DIA" e "COPIAR LINK TAGS IMPRESSÃO PDF". Acrescentou-se ao
`limpar_html.py` o recorte por contêiner: `<div id="conteudo">` na ANTT e o elemento `<main>` do
HTML5 na SEFAZ. **A primeira tentativa mirou `id="texto-compilado"`, que naquela página não é o
contêiner e sim uma âncora de link** — o recorte não pegou e o ementário continuou entrando. Achado
o contêiner certo, a Resolução nº 5.982 caiu de 3.473 para 3.261 palavras e a nº 6.068 de 700 para
684, e o texto passou a começar no título do ato. **Reprovado, antes e depois, no ensaio de
resposta conhecida da Lei nº 9.430**, que devolveu assinatura idêntica à publicada nas duas vezes:
o recorte novo não toca em página do Planalto.

Provas de conteúdo executadas e aprovadas: **Lei 9.715** — art. 8º, I. **Lei 10.209** — a cláusula
de que o vale-pedágio não integra o frete e o art. 8º, com a indenização em duas vezes o valor e a
remissão à ADIN 6031. **Lei 13.703** — o piso mínimo, vinte e nove ocorrências. **LC 225** —
devedor contumaz, trinta e nove ocorrências. **Resolução 5.982** — o registro nacional, trinta
ocorrências. **Resolução 6.068** — os seguros obrigatórios. **Resolução 6.084** — a tabela de
coeficientes. **Resolução SEFAZ 876** — a alteração do Anexo XXIII da Parte II da Resolução nº 720,
de 2014.

**Fora do acervo, como prova.** A Solução de Consulta COSIT nº 6, de 27 de janeiro de 2026,
chegou em documento impresso e **não entra no acervo normativo**: não é norma, é interpretação da
administração. Guarda-se no regime da Consulta SEFAZ-RJ 043/25 — junto das provas, e não das
normas. Lida no oficial, ela afasta a Lei nº 14.789 do crédito presumido do Convênio ICMS nº 106,
por não se tratar de subvenção para investimento, e sim de **método alternativo de apuração**
adotado opcionalmente pelo contribuinte, invocando a ADI nº 1.502-8/DF do Supremo Tribunal Federal.
Encerra-se a dívida que a mantinha em aberto.

**O que continua faltando, e por quê.** A Nota Técnica vigente do conhecimento de transporte não
foi obtida — o portal não devolveu página salvável. Permanece no acervo a versão 2025.001 v1.00,
**desatualizada e assim marcada**, com obrigação em vigor desde 3 de agosto de 2026 apoiada em
versão que não temos.

## Incorporação de 04/08/2026 (quinto lote) — a Nota Técnica do CT-e, e uma correção urgente

Uma norma: a **Nota Técnica CT-e nº 2026.002, versão 1.01, de 16 de julho de 2026**, do Projeto
Conhecimento de Transporte Eletrônico (CGIBS, Receita Federal e ENCAT). Veio em **documento
impresso** — o portal do CT-e não devolve página salvável —, e é a única norma do acervo obtida
por esse caminho desde a criação do `limpar_html.py`.

Limpeza documentada, sem tocar o texto normativo: 12 quebras de página, 11 cabeçalhos de página
(três linhas fixas, com e sem recuo) e 11 rodapés de contador removidos, e 8 sequências de
pontilhado do sumário reduzidas a espaço. Zero palavra perdida na conferência. **A primeira
tentativa removeu apenas 1 dos 11 cabeçalhos**, porque a rotina foi escrita para linha sem recuo e
as páginas seguintes trazem o cabeçalho recuado; corrigida a expressão, os onze saíram.

**A correção que esta norma impõe, e que é grave.** O assistente vinha afirmando, desde a pesquisa
da manhã e em três mensagens ao sócio, que **o CT-e sem os campos de IBS/CBS passara a ser
rejeitado em produção desde 3 de agosto de 2026**. A afirmação apoiava-se no cronograma da versão
1.00 desta Nota Técnica, colhido em fonte secundária. **A versão 1.01, de 16 de julho, alterou
exatamente essa data.** Lê-se no histórico de alterações e na regra de validação 001:

> HOMOLOGAÇÃO: 01/07/2026 — **PRODUÇÃO: implementação futura**

Ou seja: a rejeição por falta do grupo IBS/CBS **está implantada apenas em homologação**, e a data
de produção **não foi fixada**. Não há, nesta data, rejeição em produção por esse motivo. O que
permanece com data certa é o **Ato Conjunto RFB/CGIBS nº 4, de 30/07/2026**, que trata de coisa
diversa — quais modelos de documento fiscal passam a ser exigíveis, e não do preenchimento dos
campos da reforma. **O assistente confundiu as duas obrigações.** Fica consignado como erro, e a
advertência ao cliente há de ser corrigida na mesma medida em que foi dada.

Registre-se, ainda em favor da leitura correta, o que continua valendo: quando o grupo CBS for
informado em documento emitido em 2026, **a alíquota deve ser de 0,90%**, na forma do art. 346 da
LC 214/2025, sob pena de rejeição 326.

A `NT-CTE-2025.001` permanece no acervo, agora marcada como **superada pela 2026.002 e mantida por
referência histórica** — a nova declara-se, na introdução, evolução daquela.

## Incorporação de 05/08/2026 — a sede do crédito presumido do Rio de Janeiro

Seis arquivos, cinco normas. Encerra-se a dívida mais antiga do eixo estadual: **onde a legislação
fluminense hospeda o crédito presumido de 20% do Convênio ICMS 106/96**.

A resposta não estava no RICMS, nem em decreto autônomo, nem em lei específica — estava no
**Manual de Diferimento, Ampliação de Prazo de Recolhimento, Suspensão e de Incentivos e Benefícios
de Natureza Tributária**, aprovado pelo `RJ-DEC-27815-2001`, cujo art. 1º o aprova e cujo art. 2º
delega ao Secretário de Fazenda os atos de atualização (a nota do decreto registra que a Resolução
SEFCON nº 5.720/2001 subdelegou ao Superintendente de Tributação). O Manual não tem artigos: é
organizado em **verbetes alfabéticos**, e o localizador correto é o verbete
*Prestação de serviço de transporte*, da letra "P".

**O Manual entra em duas camadas, e as duas são necessárias.** A vigente,
`RJ-MANUAL-BENEFICIOS`, colhida no portal da SEFAZ, traz a nota de apresentação v3 (Portaria SUT
nº 323/2020) e a de **última atualização — SUPTRIB/MB nº 05/26, de 13 de julho de 2026**. Nela o
verbete é enxuto:

> Prestação de serviço de transporte. Convênio ICMS 106/1996. Crédito Presumido. Prazo indeterminado.

Quatro linhas, sem nota de alteração — ao contrário dos verbetes vizinhos, que trazem marcações do
tipo "(Item alterado pela Atualização CELT/MB nº 02/23)". O verbete nunca foi tocado. **A linha do
prazo responde a pergunta que estava aberta: indeterminado**, sem data-limite.

A camada de 2001, `RJ-MANUAL-BENEFICIOS-2001`, é o anexo original do decreto, hospedado na ALERJ em
documento do Word, gravado pela última vez em 25/01/2001. **É mais extensa que a vigente**, e por
isso não é descartável: guarda a descrição do benefício, que a redação de hoje não repete —
o crédito de 20% adotado opcionalmente em substituição ao sistema de tributação, a vedação de
aproveitar outros créditos, a inaplicabilidade ao transporte aéreo e a obrigação de a opção alcançar
todos os estabelecimentos no território nacional, consignada no livro RUDFTO. Está **desatualizada e
assim marcada**: não traz o § 3º acrescido pelo Convênio ICMS 85/03, e remete apenas ao Convênio
95/99.

**Um caminho de captura novo.** O Manual de 2001 é o primeiro arquivo do acervo erguido de
**documento do Word (.doc)**, convertido por LibreOffice em modo texto. Não passa pelo
`limpar_html.py`; passa direto ao `normalizar.py`.

Completam o lote as duas leis do FOT — `RJ-LEI-8645-2019-FOT`, que o institui, e
`RJ-LEI-11071-2025-FOT`, que o escalona e prorroga até 31/12/2032 — e a
`RJ-POR-SUCIEF-65-2019`, que vincula o benefício ao código de escrituração
**RJ805149 — "Convênio ICMS 106 de 1996 – Crédito Presumido"**, com início em 01/04/2019 e **sem
data-fim**. Registre-se que, na coluna de norma daquela tabela, o RJ805149 remete **apenas ao
Convênio** — sem decreto ou resolução estadual, ao contrário de quase todos os códigos vizinhos.
É mais uma confirmação de que não há ato estadual concessivo autônomo.

Provas de conteúdo executadas e aprovadas: **Decreto 27.815** — a cláusula de aprovação do Manual.
**Manual vigente** — o verbete, a nota da atualização de 13/07/2026 e a da apresentação v3.
**Manual de 2001** — o verbete com a descrição e o fecho "Convênio ICMS 106/96 Alterado pelo
Convênio ICMS 95/99 Prazo indeterminado". **Lei 8.645** — o Fundo e o percentual. **Lei 11.071** —
a alteração e o termo final. **Portaria SUCIEF 65** — o código RJ805149 e a tabela 5.2.

## Incorporação de 05/08/2026 (segundo lote) — o FOT, os anexos da escrituração e a moldura da LC 160

Oito arquivos novos e uma substituição.

**Os quatro anexos da Resolução SEFAZ nº 720/2014** fecham a lacuna que a incorporação da Resolução
876/2026 havia aberto: o acervo guardava o ato **alterador** e não o **alterado**. O
`RJ-RES-SEFAZ-720-2014-ANEXO-XVIII` traz o mecanismo em dois tempos da escrituração de crédito
presumido — estorno total dos créditos relacionados pelo código **RJ018003** e lançamento do crédito
pelo **RJ028001**, com o código do benefício no campo `DESCR_COMPL_AJ` e no registro E115 (art. 10).
É o dispositivo que a Consulta SEFAZ-RJ nº 043/25 invoca, e agora está lido na fonte. O
`ANEXO-XXIII` disciplina o depósito no FOT na EFD pelo código **RJ050019**, e traz, já incorporada,
a **revogação da alínea `c` do inciso II do art. 2º pela Resolução SEFAZ nº 892/2026** — o registro
E113, exigido pela Resolução 876/2026, deixou de sê-lo com efeitos retroativos a 1º de abril de
2026. O `ANEXO-XIII` traz o armazém geral, e o `ANEXO-XXV`, o contribuinte com decisão judicial
suspendendo a exigibilidade.

**A Resolução SEFAZ nº 875/2026 e o seu Anexo Único, com um achado.** O Anexo classifica os
benefícios para efeito do FOT, em tabela de sete colunas — tipo de ato, número, data, ementa,
**data-limite da fruição**, **oneroso?** e dispositivo. São cerca de 190 atos. **As espécies
listadas são apenas duas: Decreto (142) e Lei (48). Nenhum convênio.** E a data-limite é 31/12/2032
em 174 das linhas.

Isso identifica o universo da tabela: são os **benefícios estaduais unilaterais reinstituídos** —
exatamente o alcance da LC 160/2017 e do Convênio ICMS 190/17. **O crédito presumido do Convênio
106/96 não consta do Anexo Único, e não poderia constar**, por não ser benefício unilateral.
A ausência confirma a leitura, em vez de contrariá-la.

**A moldura, agora lida.** A `LC-160-2017`, art. 1º, incisos I e II, delibera sobre remissão e
reinstituição de benefícios *"instituídos em desacordo com o disposto na alínea 'g' do inciso XII do
§ 2º do art. 155 da Constituição Federal"*; o `CONV-ICMS-190-2017`, cláusula primeira, repete a
delimitação. O crédito do 106/96 foi instituído **em acordo** — por convênio celebrado nos termos da
LC 24/75, com ratificação nacional pelo Ato COTEPE-ICMS 01/97. Logo os prazos escalonados do art.
3º, § 2º da LC 160 não o alcançam, e **o prazo indeterminado do Manual permanece íntegro**. Deixa de
ser tese declarada e passa a conclusão com dispositivo lido.

**O `CONV-ICMS-100-2001` encerra a questão do dutoviário.** A cláusula primeira vigente, após a
adesão de São Paulo pelo Convênio ICMS 174/25, autoriza dez unidades federadas a revogar o crédito
presumido no transporte dutoviário: Alagoas, Amazonas, Ceará, Espírito Santo, Mato Grosso, Mato
Grosso do Sul, Paraná, Rio Grande do Norte, São Paulo e Sergipe. **Busca por "Rio de Janeiro" no
arquivo: zero ocorrências.** No Rio, o crédito alcança também o dutoviário. A página traz ainda duas
redações anteriores, que o `camadas.py` separa.

**Substituição.** O `CONV-ICMS-106-1996` foi recapturado. A versão anterior tinha 397 palavras; a
nova tem 1.059, e traz as notas de alteração que faltavam — a renumeração do parágrafo único para
§ 1º e o acréscimo do § 2º pelo Convênio 95/99, com efeitos de 01.01.00, e o acréscimo do § 3º pelo
Convênio 85/03, com efeitos de 03.11.03.

Provas de conteúdo executadas e aprovadas: **Anexo XVIII** — RJ018003, RJ028001, RJ10080000 e o
registro E115. **Anexo XXIII** — "REVOGADO", a remissão à Resolução 892/2026 e o código RJ050019.
**Anexo XIII** — o armazém geral, sessenta e sete ocorrências, e o art. 11. **Resolução 875** — o
Anexo Único e as colunas "ONEROSO?" e "DATA LIMITE DA FRUIÇÃO". **Convênio 100/01** — a lista das
dez unidades e a ausência do Rio. **Convênio 190/17 e LC 160** — a expressão "em desacordo".
**Convênio 106/96** — o § 3º e a remissão ao Convênio 85/03.

### Os instrumentos reprovaram duas vezes, e foram corrigidos

**O `recortar_portal` truncou o Manual em 86 palavras.** A rotina testava primeiro a regra da ANTT —
`<div id="conteudo">` — e só depois o `<main>` do HTML5. O portal da SEFAZ-RJ usa `<main>`, mas o seu
**rodapé institucional também carrega um `<div id="conteudo">`**, que na página do Manual fica no fim
do arquivo (posição 660.484 de 687.745). O recorte casou com o rodapé e devolveu o endereço, o
telefone e o menu do portal — **86 palavras no lugar de 33.138**. Corrigido: o recorte passa a
**rotear pelo host** da página salva, e não pela ordem das regras. O ensaio de resposta conhecida
foi o Decreto 50.248, já publicado: sob a regra nova ele sai com 4.003 palavras contra 3.996, e as
sete de diferença são cosméticas e confinadas ao preâmbulo — o hífen de `SEI-040007` **preservado**
(a versão anterior o perdia) e o `D E C R E T A :` espaçado da fonte. O arquivo foi **regerado** sob
a regra única, e a sua assinatura mudou de `b8fc87ea3469` para `4a68968bbaf1`. Sob o recorte novo,
os Anexos XIII, XVIII e XXIII também emagreceram — 34.065→33.990, 4.210→4.127 e 921→838 —, e as
palavras que saíram eram trilha de navegação acima do título do ato.

**O `conferir` acusou perda onde havia conserto.** O Manual de 2001, vindo do Word, tem **230 hifens
de sílaba (U+00AD)** partindo palavras em dois tokens — `exclusi`+`vamente`, `pro`+`pulsão`,
`multimoto`+`res`. O `reparar()` os remove, e a conferência lia 24.272 → 24.042 como perda de 230
palavras, quando eram 230 palavras **remendadas**. Corrigido: a conferência passa a comparar o bruto
**depois** de `reparar()`, que é reparo declarado e auditado, e não alteração de conteúdo. É a mesma
patologia da conferência em NFD, corrigida em 03/08/2026: o instrumento é que media mal.

### Sentinela de dado pessoal no `validar.py`

Quatro das páginas capturadas no portal da SEFAZ foram salvas **com sessão aberta**, e trazem no
cabeçalho o nome e o CPF do usuário logado. O repositório é público. O `limpar_html.py` já descartava
esse bloco por recortar o `<main>` — a varredura sobre os 60 arquivos não achou **nenhum CPF, nenhum
e-mail e nenhum vestígio de sessão** —, mas instrumento que confia na boa execução de outro
instrumento é instrumento frágil. Acrescentou-se ao `validar.py` uma varredura: **CPF e vestígio de
sessão reprovam**; CNPJ e e-mail apenas se relatam, porque há CNPJ **dentro do texto normativo** —
um no Anexo XIII, em exemplo de escrituração, e três no Anexo Único da Resolução 875, em ementas de
atos concessivos. Apagá-los corromperia a norma.

### Fora do acervo, e por quê

A **Resolução SEFAZ nº 892/2026** só foi obtida em reprodução de agregador comercial, que é fonte
secundária. Não entra como norma. Não faz falta: a revogação que ela promove está registrada no
texto oficial do próprio Anexo XXIII, que é primário e já traz a alínea como REVOGADA. Fica no
regime de prova, ao lado da Consulta SEFAZ-RJ nº 043/25 e da Solução COSIT nº 6 — que são
interpretação da administração, e não norma.

### O que continua faltando, e por quê

**A faixa do FOT aplicável ao RJ805149.** O Decreto 47.057/2020, na redação do 50.248/2026, atribui
quatro faixas — W (18,18%, oneroso), X (não oneroso, escalonado de 20% em 2026 a 60% em 2032),
Y (10%) e Z (20%). O benefício **está abrangido** (art. 1º, § 2º, I: benefícios do Manual) e **não
consta das exceções** (alíneas `a` a `h` e inciso II; zero ocorrências de "106/96" no decreto), e
não é oneroso. Por subsunção, faixa **X**. Mas **nenhum texto o diz**, e o Anexo Único da Resolução
875, agora lido, não o classifica. Fica como **tese fundamentada e declarada**, com o cenário
alternativo ao lado — nunca como conclusão. Caminhos para encerrar: a página de consulta pública da
ferramenta de cálculo, que o art. 2º da Resolução 875 manda a SEFAZ manter, ou consulta tributária
formal.

**A Portaria SUT nº 323/2020**, que aprova a versão 3 da Apresentação do Manual, não foi localizada
em endereço oficial. O acervo funciona sem ela; com ela, ficaria completo.

**O FECP perante o crédito presumido** — se os 20% incidem também sobre os dois pontos do Fundo.
Nenhuma manifestação primária específica. Segue para consulta formal.

## Retificação terminológica de 05/08/2026

Até esta data o acervo e os pareceres chamavam o benefício do Convênio ICMS nº 106/96 de **crédito
outorgado**. A designação é imprecisa no Rio de Janeiro, e a correção fica registrada aqui em vez de
ser feita em silêncio.

**O que a legislação fluminense diz.** Todos os instrumentos que regem o benefício o chamam de
**crédito presumido**: o Manual de Benefícios, no verbete e no campo de modalidade; a Portaria SUCIEF
nº 65/2019, na descrição do código RJ805149; o art. 82-C do Livro IX do RICMS-RJ; o art. 12 do Anexo
XVIII da Parte II da Resolução SEFAZ nº 720/2014; e o próprio Convênio, na sua ementa. Medição sobre
os seis arquivos: **145 ocorrências de "crédito presumido" e nenhuma de "crédito outorgado"**. As
modalidades do Manual são quatro — Isenção, Diferimento, Redução de Base de Cálculo e Crédito
Presumido —, e não há modalidade "Crédito Outorgado".

**O que a correção NÃO significa.** As duas expressões são juridicamente sinônimas: o Convênio ICMS
nº 190/17, cláusula primeira, § 4º, V, arrola "crédito outorgado ou crédito presumido" como uma só
espécie, e a LC 214/2025, art. 385, escreve "tal como crédito presumido de ICMS, crédito outorgado de
ICMS, entre outros". Não houve, portanto, erro de direito — houve imprecisão diante da terminologia
local. Registre-se ainda que **o Rio usa a expressão "crédito outorgado"**, mas para outros
benefícios: o Decreto nº 46.538/2018, de projetos culturais e desportivos, e o Decreto nº 49.386/2024,
de infraestrutura de distribuição de energia elétrica.

**Cautela que fica.** A LC 214/2025 emprega "crédito presumido" com sentido técnico próprio no art.
169 — o do transportador autônomo pessoa física. Num mesmo documento haverá dois créditos presumidos
de institutos diversos, e cada um há de vir identificado pela norma-fonte.

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

**Terceiro lote do mesmo dia (Lei 9.249 e Lei 9.430).** Mesmo método, mesma rotina:

| Ruído removido | O que era | Ocorrências |
|---|---|---:|
| `U+000C` (form feed) | quebra de página do `pdftotext` | 61 |
| cabeçalho de página | carimbo de data/hora + título repetido | 61 |
| rodapé de página | URL oficial + contador de página | 61 |
| hífen de fim de linha | `utilizá-` + `lo`, `ano-` + `base` (junção, não remoção) | 5 |

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
- A vigência do crédito presumido do transporte no RJ está evidenciada na **Consulta
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
- **`LEI-9430-1996.txt` — defeito da própria página oficial, confirmado no HTML.** 103 ocorrências,
  ao menos, de `pela` onde a norma diz `pelo` (748 `pela` contra 1 `pelo`). O HTML capturado do
  Planalto devolve a mesma contagem: **o defeito é da fonte**, não do extrator nem do tratamento. O
  conteúdo normativo está completo e a substância é a oficial, mas **busca por `pelo` falha neste
  arquivo** e citação literal reproduz a preposição da página. Recomendada a captura da página
  compilada (`L9430compilada.htm`), artefato distinto, para verificar se carrega o mesmo defeito.
- **Redação empilhada e tachado perdido — limitação de todo o acervo, medida em 03/08/2026.** As
  páginas do Planalto marcam **visualmente** (tachado) as redações revogadas e superadas; o texto
  puro não conserva essa marca. Em `LEI-9430-1996.txt` são **695 blocos, 18.196 palavras — 51% do
  arquivo**. Proxy por artigo repetido em outros: `LEI-8036-1990` 48%, `RJ-LEI-2657-1996` 34%,
  `LEI-8212-1991` 29%, `LC-227-2026` e `LEI-10833-2003` 20%, `LC-214-2025` 6%; zero em
  `DEC-12955-2026`, `RES-CGIBS-6-2026` e `LEI-5172-1966`. A página "compilada" **não** resolve.
  Consequência: a primeira ocorrência de um dispositivo pode ser a redação velha. **Mas o tachado
  nunca foi o marcador de vigência**: na própria página, 32 das 59 notas "(Revogado pela …)" estão
  fora do tachado — os arts. 18 a 24-B da Lei 9.430, revogados pela Lei 14.596/2023, aparecem em
  tipo normal. O marcador é a **nota entre parênteses**, e ela sobrevive íntegra no `.txt`. Ler o
  artigo inteiro até o fecho e conferir a nota; havendo remissão a lei com efeitos diferidos, ir à
  lei alteradora.
- **`LEI-9430-1996.txt` — dupla camada.** O compilado traz o art. 64 com a redação anterior à
  reforma (ainda com COFINS e PIS/PASEP) e o art. 66 vigente. A redação de 2027 está no art. 502
  da `LC-214-2025.txt` e a revogação dos §§ 7º-8º do art. 64 e do art. 66, no art. 542, V, da
  mesma lei, a partir de 1º/01/2027. Não afirmar a redação de 2027 a partir deste arquivo.
- `LEI-9249-1995.txt`: os arts. 10 e 10-A remetem aos arts. 6º-A, 16-A e 16-B da **Lei 9.250/1995**,
  que **não está neste acervo**. O cálculo do redutor e da tributação mínima de altas rendas não se
  faz só com este arquivo — a `LEI-15270-2025.txt` traz o texto acrescido, mas não a lei hospedeira.
- Faltam (a obter quando o tema for atacado): Lei 10.209/2001, Lei 13.703/2018,
  ADI 7181/7191 (STF), Resolução ANTT do RNTR-C, **Lei 15.371/2026** (salário-paternidade;
  altera a Lei 8.212 a partir de 1º/01/2027) e **Lei 9.250/1995** (IRPF — lei hospedeira dos
  arts. 6º-A, 16-A e 16-B acrescidos pela Lei 15.270/2025 e remetidos pelo art. 10 da Lei 9.249).
