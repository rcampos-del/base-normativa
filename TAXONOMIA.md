# TAXONOMIA DO ACERVO

Como as normas são classificadas e como entra um setor ou uma UF nova.

---

## O acervo tem duas dimensões, não uma

Toda norma é classificada por **setor** e por **jurisdição**. Um cliente é sempre um cruzamento das duas: *transportadora do RJ*, *indústria de SP*.

### Setor

| valor | significado |
|---|---|
| `transversal` | vale para qualquer setor — **sempre incluída em toda consulta** |
| `trc` | transporte rodoviário de cargas |
| *(novos)* | um valor novo por setor atacado |

### Jurisdição

| valor | significado |
|---|---|
| `federal` | União |
| `nacional` | CONFAZ, CGIBS e notas técnicas de âmbito nacional (convênio ICMS depende de internalização estadual) |
| `rj` | Rio de Janeiro |
| *(novas)* | uma por UF atacada |

---

## Como consultar

Para um cliente de setor **X** na UF **Y**, o acervo aplicável é:

```
setor IN ('transversal', 'X')   E   jurisdicao IN ('federal', 'nacional', 'Y')
```

O `transversal` entra **sempre**. É o que evita duplicar a LC 214 em cada setor.

---

## Regra de classificação (importante)

**Classifica-se a norma, não o dispositivo que usamos dela.**

A Lei 10.833/2003 (COFINS) é `transversal`, ainda que o §19 do art. 3º trate do crédito presumido de subcontratação de TAC. A lei serve a todos os setores; o dispositivo é que é setorial.

Se classificássemos pelo dispositivo, toda lei geral acabaria etiquetada com todos os setores — e a taxonomia perderia utilidade.

O elo entre *dispositivo* e *setor* não mora aqui: mora na tabela de **regras** do sistema, onde cada regra aponta para seu dispositivo, seu parecer de origem e seu grau de segurança.

---

## Por que arquivos soltos, e não pastas por setor

Uma norma pode servir a vários setores ao mesmo tempo. Pasta obriga a escolher **um** lar — e a LC 214 não tem um lar só.

Duplicar o arquivo em duas pastas seria pior: duas cópias divergem, e um dia alguém cita a errada. É exatamente o que o MANIFESTO existe para impedir.

Por isso: **arquivo único, classificação como metadado.**

> Se o acervo passar de ~60 arquivos, vale reavaliar e agrupar por hierarquia (`02-complementar/`, `04-decreto/`). Agrupar por *hierarquia* é seguro, porque uma norma tem só uma. Por *setor*, não.

---

## Como entra um setor novo

1. Levantar as normas específicas do setor e normalizar com o `normalizar.py`.
2. Acrescentar uma linha em `fontes.tsv` para cada uma, com o novo valor de setor.
3. Acrescentar cada arquivo à tabela de integridade do `MANIFESTO.md`, com SHA-256.
4. Rodar `python3 validar.py` — deve fechar sem falhas.
5. As normas `transversal` **já estão prontas** e não se tocam.

**Teste de acerto do desenho:** se a chegada de um setor novo exigir mudar a *estrutura* (colunas, scripts, esquema do banco), o desenho estava errado. Se bastar **acrescentar linhas**, estava certo.

## Como entra uma UF nova

Mesmo procedimento, com dois cuidados que o RJ ensinou:

- **A lei do ICMS estadual e o adicional de pobreza são `transversal`** naquela UF — servem a qualquer cliente de lá, não só ao setor atacado.
- **Verificar fundos estaduais que corroem benefícios** (no RJ, o FOT). Costumam ser `transversal` e passam despercebidos porque não estão na lei do imposto.

---

## Estado atual

32 normas: **28 transversais** e **4 de TRC**. *(atualizado em 04/08/2026)*

| jurisdição | total | transversal | trc |
|---|---:|---:|---:|
| federal | 22 | 21 | 1 |
| nacional | 5 | 3 | 2 |
| rj | 5 | 4 | 1 |

Leitura prática: um cliente de **outro setor no RJ** já encontra **28 das 32 normas prontas e auditadas**. Só faltam as específicas do setor dele.

> **Nota de classificação — o FGTS e a Lei 8.212.** Ambas entram como `transversal` e
> `03-ordinaria`, pela regra de classificar a norma e não o dispositivo. A Lei 8.212 contém
> dispositivos escritos para o TRC — o art. 22, § 15, e o art. 28, § 11, que fixam a base de 20%
> na contratação de condutor autônomo —, mas a lei serve a qualquer empregador; é o mesmo caso da
> Lei 10.833 e do seu art. 3º, § 19. Quanto à hierarquia, a Lei 8.212 é alterada por lei
> complementar (LC 123/2006, LC 128/2008, LC 207/2024) **e** por lei ordinária (Leis 14.973/2024,
> 15.072/2024, 15.363/2026, além de medidas provisórias) — logo, ao contrário do CTN, não atende
> ao critério que justificou classificá-lo como `02-complementar`.

> **Nota de classificação — o CTN.** `LEI-5172-1966` entra como `02-complementar`, e não como
> `03-ordinaria`, embora seja formalmente lei ordinária. O critério é o do próprio arquivo: ele só
> é alterado por lei complementar — LC 104/2001, LC 118/2005, LC 143/2013, LC 187/2021,
> LC 194/2022, LC 208/2024, LC 214/2025 e LC 227/2026, todas visíveis no texto. A tese da recepção
> com status de lei complementar (art. 146 da Constituição) **não foi conferida em fonte primária**
> nesta classificação; se o sócio preferir a designação formal, muda-se um campo em `fontes.tsv`.

> **Nota de classificação — o IRPJ e a CSLL.** `LEI-9249-1995` e `LEI-9430-1996` entram como
> `transversal` e `03-ordinaria`. A Lei 9.249 contém dispositivo escrito para o transporte — o
> art. 15, § 1º, II, `a`, que excetua o transporte **de carga** do percentual de 16% e o devolve
> ao caput, 8% —, mas a lei rege o imposto de renda de qualquer pessoa jurídica; é o mesmo caso
> da Lei 10.833 e do seu art. 3º, § 19, e da Lei 8.212 e do seu art. 22, § 15. Classifica-se a
> norma, não o dispositivo.
