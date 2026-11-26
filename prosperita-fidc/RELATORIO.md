# PROSPERITÀ FIDC (CNPJ 53.033.766/0001-39): conferência da coleta e respostas da operação

Data: 26/11/2026. Base: coleta pública do Soul no `Dnagy765/hub-diego`, branch `dot/prosperita-fidc-coleta-2026-11-26`, PR #91 em rascunho. A primeira conferência foi feita sobre o commit `ab1ca53` (305 arquivos); esta versão incorpora o complemento do commit `770cb10` (mais 235 arquivos: diário completo, QSA, processos, identificação do cedente e `COLETA.md`), também conferido nos brutos.

O estudo para a operação está em `ESTUDO.md` e as listas de pedidos em `PEDIDOS_DE_DOCUMENTOS.md`.

Convenção usada em todo o texto:

| Marca | Significado |
|---|---|
| **Fato** | consta em arquivo bruto do hub, com caminho indicado |
| **Leitura** | inferência minha a partir dos números; precisa de confirmação |
| **Não verificado** | sem arquivo bruto, sem URL ou fonte que não abriu |

Caminhos `raw/...` e `dados/...` são relativos a `dossies/prosperita-fidc/` no hub. Arquivos em `dados/` e `scripts/` desta pasta são meus.

---

## Resumo

1. **A coleta do informe mensal está íntegra.** Refiz a extração dos 24 zips da CVM para os 35 meses (12/2023 a 10/2026) e comparei linha a linha com os 18 CSVs do Soul: zero divergência. Os demais blocos estão parciais ou ausentes (seção 1).
2. **A cota rendeu 3,94% em 35 meses contra 41,70% do CDI.** A TIR do cotista foi 8,3% a.a. Os mesmos aportes a 100% do CDI valeriam R$ 9,67 mi; o PL é R$ 8,82 mi.
3. **A carteira gera retorno; custo fixo e provisão o consomem.** O resultado antes de provisão foi R$ 1,88 mi desde o início (16,7% a.a. sobre o PL em 2026). Os pisos de taxa custaram 14,4% do PL em 2024 e 4,9% em 2025, e o saldo de PDD é R$ 0,69 mi.
4. **O fundo não cresceu por falta de capital, com um intervalo de falta de lastro.** Captou R$ 7,73 mi em nove aportes, o último em 08/2025. De 09/2025 a 03/2026 ficou com R$ 1,6 mi parado em média (22% do PL). De 04/2026 em diante está 94% alocado.
5. **O ativo é CCB com desconto feito pela Jaguafrangos, não duplicata de risco sacado clássico.** Cedente único (BMP SCD), 25 maiores devedores com 72% da carteira, prazo médio perto de 290 dias, pagamento em conta de livre movimentação do cedente ou da Jaguafrangos, sem notificação ao devedor.
6. **O FIF era o cotista único do FIDC até 01/2026.** Foi liquidado em 02/2026 com entrega dos ativos aos seus 2 cotistas, que hoje aparecem no FIDC como 2 pessoas físicas. A identidade não é pública. A consultoria e agente de cobrança do fundo tem os mesmos dois sócios-administradores da Jaguafrangos.
7. **A queda de 09 para 10/2026 (R$ 275 mil) é provisão.** A PDD subiu R$ 409 mil com vencidos praticamente estáveis; o resto do mês rendeu R$ 134 mil. Não houve amortização nem resgate.
8. **Três pontos que a compradora precisa resolver antes de preço:** a decisão do TJMT que reconheceu sucessão empresarial de fato da Jaguafrangos na falência do Grupo Pesqueiro (confirmada no Diário de Justiça Eletrônico Nacional); a responsabilidade ilimitada do cotista no regulamento vigente; e a conciliação de recebimentos, que em 03/2026 levou a cota a cair 23% e voltar 42% no mês seguinte.

---

## 1. Inventário da coleta

| # | Bloco pedido | Status | O que chegou | O que falta |
|---|---|---|---|---|
| 1 | Informe mensal FIDC | **ok** | 24 zips CVM em `raw/fidc/` (2023 e 2024 anuais, 01/2025 a 10/2026 mensais), dicionário de campos, 18 CSVs em `dados/inf_mensal_fidc_tab_*.csv`, manifesto com URL e sha256 | nada |
| 2 | Cadastro e histórico de prestadores | **parcial** | `registro_fundo_classe.zip` (situação atual dos dois fundos), `cad_fi.csv`, `cad_fi_hist.zip` | `cad_fi` e `cad_fi_hist` não trazem o FIDC (0 linhas); só há histórico do FIF. O histórico de prestadores do FIDC não existe nessa fonte e foi reconstruído por informe mensal e atas (seção 3.f) |
| 3 | Documentos do Fundos.NET | **ok com ressalvas** | 81 de 81 documentos do FIDC (44 informes mensais XML, 13 trimestrais, 12 de assembleia, 5 regulamentos, 3 DFs, 4 outros). FIF: zero no Fundos.NET; 2 regulamentos e 3 DFs via CVM | 3 URLs da CVM com HTTP 429 (2 regulamentos do FIDC que têm cópia pelo Fundos.NET; regulamento do FIF de 08/04/2024 sem cópia). Ata de 08/04/2024, trimestral do 2T26 e resultado da AGC de 25/05/2026 não existem na fonte |
| 4 | CDA e informe diário do FIF | **ok** | CDA: 35 zips (12/2023 a 10/2026). Informe diário: 36 zips (12/2023 a 11/2026), 530 dias com dado do FIF, o último em 11/02/2026. CSVs derivados e manifestos com URL e sha256 | nada |
| 5 | CDI | **ok** | `raw/bcb/sgs_12.json` (série 12, 749 dias), `cdi_diario.csv`, `cdi_mensal.csv` | nada |
| 6 | Quadro societário | **parcial** | QSA oficial da Receita (dados abertos, 27 linhas) de Prosperita Consultoria, Jaguafrangos, S&PB, Finaxis CTVM, Banco Finaxis e Petra; cadastro e 36 filiais por espelho | Cartões de CNPJ oficiais em PDF; percentuais de participação (o QSA não traz); QSA da BMP e da FIDD |
| 7 | Processos e sanções | **parcial** | 60 brutos: três processos sancionadores da CVM de 2016 (Finaxis, Petra), cinco atos da ANBIMA (Finaxis, Petra), publicações do Diário de Justiça Eletrônico Nacional sobre a Jaguafrangos (TJMT, TRF4, TRT9, TJPR), notas do MPT | Protestos; distribuição completa por CNPJ; PGFN; dois extratos de julgamento da CVM; nada localizado sobre a FIDD na CVM. 14 downloads do manifesto falharam e não têm arquivo |
| 8 | Grupo BTZ | **parcial** | 30 brutos, 23 registros em `dados/bloco8_registros.csv` (unidades, habilitações, benefício fiscal GO, Fomento Paraná, autuações) | Faturamento, endividamento e DFs não localizados. 7 brutos citados no manifesto não estão no repositório |
| 9 | Pedidos não públicos | **ok** | `PEDIDOS.md`, 15 itens, nada enviado | Acrescento itens na seção 5 |
| – | `COLETA.md` | **ok** | índice por bloco, com status e fontes | chegou no complemento |

---

## 2. Conferência

### 2.1 O que foi testado

| Teste | Resultado |
|---|---|
| sha256 dos 24 zips de `raw/fidc/` contra `fontes_bloco1.csv` | 24 de 24 iguais |
| Reextração do informe mensal por CNPJ com e sem máscara, em qualquer coluna, 18 tabelas, 35 meses | 1.523 linhas; mesmas contagens do Soul |
| Comparação linha a linha, todas as colunas, todos os meses (não só amostra) | **0 divergências** |
| Meses faltando | nenhum; as 18 tabelas existem nos zips para os 35 meses. A tabela VIII só tem dados do fundo em 26 meses, o que é da fonte |
| Filtro de CNPJ | correto. Busca por nome achou 1.399 linhas de homônimos (AGGA Prosperitas, Avance Prosperity, JMP Prosperity e outros), nenhuma do fundo |
| PL x quantidade de cotas x valor da cota | fecha em todos os meses (diferença menor que R$ 0,01) |
| Rentabilidade informada x variação da cota | bate em 33 de 35 meses (ver D15) |
| CDI mensal recalculado do JSON bruto | igual ao `cdi_mensal.csv` em todos os meses |
| Cadastro: busca nos brutos por CNPJ e nome | confirma o que o Soul reteve; o FIDC de fato não consta em `cad_fi.csv` nem em `cad_fi_hist` |
| Zips de CDA e diário contra os índices de diretório da CVM salvos em `raw/` | 49 de 49 listados no índice, tamanhos compatíveis |
| Citações usadas neste relatório | conferidas por busca no texto dos PDFs |

**Limite do teste.** Este ambiente não alcança `dados.cvm.gov.br` nem `api.bcb.gov.br` (bloqueio de rede). Conferi os CSVs contra os zips que estão no hub e os zips contra o manifesto do próprio Soul. Não baixei de novo da CVM para comparar na origem.

### 2.2 Divergências registradas

**Da coleta**

- **D1.** Resolvida no complemento. `COLETA.md` existe e há o PR #91. Na primeira conferência não havia nenhum dos dois.
- **D2.** Resolvida. O informe diário veio completo; reextraí os 36 zips e as 530 linhas do FIF são idênticas às do CSV do Soul.
- **D3.** Resolvida. O bloco 4 agora tem CSVs derivados; os 26 registros de cotas do FIDC no CDA do FIF batem com a minha extração.
- **D4.** Resolvida. Os 71 zips de CDA e diário têm URL e sha256 em manifesto, e os hashes conferem.
- **D5.** Esclarecida. Sete entradas de `bloco8_fontes.csv` e 14 de `bloco7_fontes.csv` são downloads que falharam, marcados como "não encontrado" no próprio manifesto; não há arquivo. Os registros que dependem só delas ficam **não verificados**.
- **D6.** Resolvida para o essencial. As decisões do TJMT de 07 e 10/2026 estão nas publicações do Diário de Justiça Eletrônico Nacional arquivadas em `raw/processos/cnj_djen_jaguafrangos_tjmt_1073997.json`, com o mesmo texto das cópias de site de notícia.
- **D23.** O cadastro de capital, endereço e abertura das empresas (bloco 6) vem de espelho de terceiros, não de cartão oficial. O QSA, sim, é da Receita.

**Dos documentos do próprio fundo** (o Soul coletou certo; o erro é de quem publicou)

- **D7.** O documento Fundos.NET 648627, classificado como ata da AGE de 08/04/2024, é um protocolo de envio de outra ata. A ata da 2ª emissão não está publicada.
- **D8.** O documento 1113702, ata de 02/02/2026 publicada no FIDC e depois cancelada, é do FIF: aprova a liquidação antecipada do FIF. É PDF de imagem e tem 3 páginas de 4.
- **D9.** As atas do FIDC de 05/05/2025 e 02/07/2025 (4ª emissão) trazem no anexo o nome e o CNPJ do FIF.
- **D10.** A DF de 31/12/2025 do FIDC se contradiz: a ênfase do auditor fala em "transferência de administração do fundo" aprovada em 02/02/2026; a nota 20 fala em "liquidação antecipada do Fundo" na mesma data. A assembleia de 02/02/2026 que está pública é a do FIF.
- **D11.** O índice da CVM marca a DF de 2023 do FIF como "Abstenção de Opinião". O documento não tem relatório de auditor; declara dispensa de auditoria.
- **D12.** Data da transferência para a Finaxis: 27/07/2026 na ata e na capa do regulamento; 20/07/2026 no trimestral de 09/2026 e na data de referência do Fundos.NET.
- **D13.** Trimestrais de 09/2025 a 03/2026 (primeira versão) têm o anexo assinado por "Menestys Gestora de Recursos Ltda", sem nenhum ato de troca de gestor. A segunda versão do 1T26 volta a FIDD Administração de Recursos.
- **D14.** Trimestrais de 3T25 e 4T25 dizem que "não houve operações de cessão" enquanto o informe mensal registra aquisições em todos esses meses.

**Dos dados do informe mensal** (qualidade do que o administrador reportou)

- **D15.** Rentabilidade informada difere da variação da cota em 10/2025 (-2,51% x -3,77%, explicado pela amortização de R$ 100 mil) e em 07/2026 (-1,09% x -0,51%, mês da troca de administrador, sem explicação).
- **D16.** A classe é única, mas foi reportada como "Subordinada" até 12/2025 e "Sênior" de 01/2026 em diante. O tipo do cotista oscila entre "outros fundos", "outros" e "pessoa física" em meses em que o cotista era o mesmo.
- **D17.** De 10/2025 a 01/2026 o CDA do FIF mostra 8.558,78 cotas do FIDC; o FIDC informa 8.550,15 em circulação. Diferença de 8,63 cotas, cerca de R$ 8 mil. A captação de 2025 no informe soma R$ 4.300 mil; a DF registra R$ 4.292 mil.
- **D18.** Tabela VII (negócios do mês): aquisições zeradas até 11/2024 e em 07/2025, meses em que a carteira cresceu. Recompras e substituições nunca aparecem, embora a DF de 2025 cite "envio de recursos à Classe para recompra de direitos creditórios".
- **D19.** Tabela I, cedente: participação acima de 100% em oito meses (144,27% em 03/2026); CNPJ `00000000000000` em 05/2024 e `99999999999999` em 05/2025; em branco de 06 a 09/2024 e em 07/2026.
- **D20.** Tabela IX (taxas): 8% a 14% ao ano em 2025, abaixo do CDI e incompatível com a taxa média de 17,3% a 21,6% da DF do mesmo ano. Zerada até 11/2024, em 07/2025 e em 07/2026.
- **D21.** Tabela VIII (25 maiores): soma de 116,7% da carteira em 10/2024. O dicionário da CVM não descreve os campos; o maior valor de 12/2025 (R$ 1.045 mil) coincide com o "Devedor 1" da DF, então trato a tabela como maiores devedores.
- **D22.** Disponibilidades negativas em 10/2026 (-R$ 4,85).

---

## 3. Respostas

### a) Série histórica

Fonte: `dados/painel_mensal_fidc.csv`, montado da minha reextração. "Fundo acum." encadeia as rentabilidades mensais informadas, o que neutraliza a amortização de 10/2025. O CDI de 12/2023 conta só de 28/12, data da primeira integralização.

| Mês | PL (R$ mil) | Cota (R$) | Rent. mês | CDI mês | Fundo acum. | CDI acum. | Cotistas | Adm. |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 12/2023 | 949 | 999,16 | -0,08% | 0,09% | -0,08% | 0,09% | 0 | FIDD |
| 01/2024 | 919 | 967,85 | -3,13% | 0,97% | -3,21% | 1,06% | 1 | FIDD |
| 02/2024 | 910 | 957,61 | -1,06% | 0,80% | -4,23% | 1,86% | 1 | FIDD |
| 03/2024 | 892 | 939,13 | -1,93% | 0,83% | -6,08% | 2,71% | 1 | FIDD |
| 04/2024 | 1.355 | 920,96 | -1,93% | 0,89% | -7,89% | 3,62% | 1 | FIDD |
| 05/2024 | 1.346 | 915,06 | -0,64% | 0,83% | -8,48% | 4,48% | 1 | FIDD |
| 06/2024 | 1.739 | 910,32 | -0,52% | 0,79% | -8,96% | 5,31% | 1 | FIDD |
| 07/2024 | 1.741 | 911,35 | 0,11% | 0,91% | -8,86% | 6,26% | 1 | FIDD |
| 08/2024 | 2.554 | 916,10 | 0,52% | 0,87% | -8,39% | 7,19% | 1 | FIDD |
| 09/2024 | 2.975 | 922,86 | 0,74% | 0,84% | -7,71% | 8,08% | 1 | FIDD |
| 10/2024 | 3.403 | 931,15 | 0,90% | 0,93% | -6,88% | 9,08% | 1 | FIDD |
| 11/2024 | 3.371 | 922,26 | -0,95% | 0,79% | -7,76% | 9,95% | 1 | FIDD |
| 12/2024 | 3.417 | 934,88 | 1,37% | 0,93% | -6,50% | 10,97% | 1 | FIDD |
| 01/2025 | 3.470 | 949,32 | 1,54% | 1,01% | -5,06% | 12,10% | 1 | FIDD |
| 02/2025 | 3.433 | 939,39 | -1,05% | 0,99% | -6,06% | 13,20% | 1 | FIDD |
| 03/2025 | 3.349 | 916,31 | -2,46% | 0,96% | -8,37% | 14,29% | 1 | FIDD |
| 04/2025 | 3.259 | 891,77 | -2,68% | 1,06% | -10,82% | 15,50% | 1 | FIDD |
| 05/2025 | 4.466 | 871,54 | -2,27% | 1,14% | -12,85% | 16,82% | 1 | FIDD |
| 06/2025 | 6.411 | 862,89 | -0,99% | 1,10% | -13,71% | 18,10% | 1 | FIDD |
| 07/2025 | 6.581 | 885,77 | 2,65% | 1,28% | -11,42% | 19,60% | 1 | FIDD |
| 08/2025 | 7.589 | 886,74 | 0,11% | 1,16% | -11,32% | 21,00% | 1 | FIDD |
| 09/2025 | 7.978 | 932,15 | 5,12% | 1,22% | -6,78% | 22,47% | 1 | FIDD |
| 10/2025 | 7.670 | 897,02 | -2,51% | 1,28% | -9,12% | 24,03% | 1 | FIDD |
| 11/2025 | 7.565 | 884,81 | -1,36% | 1,05% | -10,36% | 25,34% | 1 | FIDD |
| 12/2025 | 7.934 | 927,96 | 4,88% | 1,22% | -5,99% | 26,87% | 1 | FIDD |
| 01/2026 | 7.999 | 935,55 | 0,82% | 1,16% | -5,22% | 28,35% | 1 | FIDD |
| 02/2026 | 7.338 | 858,24 | -8,26% | 1,00% | -13,04% | 29,63% | 2 | FIDD |
| 03/2026 | 5.647 | 660,46 | -23,04% | 1,21% | -33,08% | 31,20% | 2 | FIDD |
| 04/2026 | 8.007 | 936,52 | 41,80% | 1,09% | -5,11% | 32,63% | 2 | FIDD |
| 05/2026 | 8.469 | 990,49 | 5,76% | 1,07% | 0,36% | 34,05% | 2 | FIDD |
| 06/2026 | 8.908 | 1.041,80 | 5,18% | 1,12% | 5,56% | 35,55% | 2 | FIDD |
| 07/2026 | 8.862 | 1.036,50 | -1,09% | 1,22% | 4,41% | 37,20% | 2 | FINAXIS |
| 08/2026 | 8.925 | 1.043,80 | 0,70% | 1,09% | 5,14% | 38,70% | 2 | FINAXIS |
| 09/2026 | 9.098 | 1.064,08 | 1,94% | 1,08% | 7,18% | 40,20% | 2 | FINAXIS |
| 10/2026 | 8.823 | 1.031,91 | -3,02% | 1,07% | 3,94% | 41,70% | 2 | FINAXIS |

| Período | Fundo | CDI | Resultado (R$ mil) | Variação de PDD (R$ mil) | PL médio (R$ mil) |
|---|---:|---:|---:|---:|---:|
| 2024 | -6,42% | 10,88% | -12 | 29 | 2.052 |
| 2025 | 0,55% | 14,32% | 317 | 424 | 5.809 |
| 2026 até outubro | 10,56% | 11,69% | 889 | 238 | 8.208 |
| Desde 28/12/2023 | 3,94% | 41,70% | 1.193 | 691 | – |

- **Fato.** As rentabilidades de 2024 e 2025 batem com as DFs auditadas (-6,43% e 0,55%).
- **Fato.** Cotistas: 1 até 01/2026 (o FIF); 2 de 02/2026 em diante.
- **Fato.** 02 a 04/2026: -8,26%, -23,04% e +41,80%. Tratado em (c).

### b) Por que o fundo não cresceu

Caixa = disponibilidades + cotas de fundos de liquidez + títulos públicos. DC líquido já desconta a PDD. Valores em R$ mil.

| Mês | PL | DC líquido | DC/PL | Caixa | Caixa/PL | Aquisições (qtd) | Aquisições (R$ mil) | Captação | Amortização | Valores a pagar |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 12/2023 | 949 | 0 | 0,0% | 950 | 100,1% | 0 | 0 | 950 | – | 1 |
| 01/2024 | 919 | 0 | 0,0% | 945 | 102,7% | 0 | 0 | – | – | 25 |
| 02/2024 | 910 | 0 | 0,0% | 928 | 102,0% | 0 | 0 | – | – | 26 |
| 03/2024 | 892 | 0 | 0,0% | 919 | 103,0% | 0 | 0 | – | – | 27 |
| 04/2024 | 1.355 | 0 | 0,0% | 1.383 | 102,1% | 0 | 0 | 480 | – | 28 |
| 05/2024 | 1.346 | 308 | 22,9% | 1.060 | 78,8% | 0 | 0 | – | – | 28 |
| 06/2024 | 1.739 | 1.243 | 71,5% | 533 | 30,6% | 0 | 0 | 400 | – | 42 |
| 07/2024 | 1.741 | 1.350 | 77,5% | 415 | 23,8% | 0 | 0 | – | – | 25 |
| 08/2024 | 2.554 | 2.474 | 96,9% | 195 | 7,6% | 0 | 0 | 800 | – | 115 |
| 09/2024 | 2.975 | 2.477 | 83,3% | 563 | 18,9% | 0 | 0 | 400 | – | 66 |
| 10/2024 | 3.403 | 3.095 | 90,9% | 481 | 14,1% | 0 | 0 | 400 | – | 173 |
| 11/2024 | 3.371 | 2.927 | 86,8% | 681 | 20,2% | 0 | 0 | – | – | 238 |
| 12/2024 | 3.417 | 2.694 | 78,9% | 754 | 22,1% | 6 | 61 | – | – | 32 |
| 01/2025 | 3.470 | 2.795 | 80,6% | 708 | 20,4% | 30 | 264 | – | – | 34 |
| 02/2025 | 3.433 | 2.923 | 85,1% | 545 | 15,9% | 77 | 387 | – | – | 35 |
| 03/2025 | 3.349 | 3.215 | 96,0% | 173 | 5,2% | 143 | 467 | – | – | 39 |
| 04/2025 | 3.259 | 3.120 | 95,7% | 165 | 5,1% | 25 | 367 | – | – | 27 |
| 05/2025 | 4.466 | 3.893 | 87,2% | 619 | 13,9% | 43 | 931 | 1.300 | – | 51 |
| 06/2025 | 6.411 | 5.312 | 82,9% | 1.173 | 18,3% | 49 | 1.671 | 2.000 | – | 80 |
| 07/2025 | 6.581 | 6.356 | 96,6% | 352 | 5,4% | 0 | 0 | – | – | 131 |
| 08/2025 | 7.589 | 6.794 | 89,5% | 824 | 10,9% | 84 | 801 | 1.000 | – | 33 |
| 09/2025 | 7.978 | 6.517 | 81,7% | 1.499 | 18,8% | 70 | 813 | – | – | 50 |
| 10/2025 | 7.670 | 6.341 | 82,7% | 1.553 | 20,2% | 86 | 415 | – | 100 | 227 |
| 11/2025 | 7.565 | 6.048 | 79,9% | 1.839 | 24,3% | 42 | 253 | – | – | 325 |
| 12/2025 | 7.934 | 6.770 | 85,3% | 1.314 | 16,6% | 138 | 1.112 | – | – | 153 |
| 01/2026 | 7.999 | 6.545 | 81,8% | 1.500 | 18,8% | 84 | 432 | – | – | 49 |
| 02/2026 | 7.338 | 6.164 | 84,0% | 1.760 | 24,0% | 28 | 263 | – | – | 589 |
| 03/2026 | 5.647 | 5.139 | 91,0% | 1.668 | 29,5% | 59 | 645 | – | – | 1.163 |
| 04/2026 | 8.007 | 6.870 | 85,8% | 1.253 | 15,6% | 129 | 1.165 | – | – | 119 |
| 05/2026 | 8.469 | 8.023 | 94,7% | 536 | 6,3% | 77 | 1.453 | – | – | 96 |
| 06/2026 | 8.908 | 8.196 | 92,0% | 840 | 9,4% | 67 | 1.059 | – | – | 135 |
| 07/2026 | 8.862 | 8.228 | 92,8% | 887 | 10,0% | 64 | 701 | – | – | 257 |
| 08/2026 | 8.925 | 8.961 | 100,4% | 139 | 1,6% | 122 | 1.253 | – | – | 181 |
| 09/2026 | 9.098 | 8.982 | 98,7% | 250 | 2,8% | 20 | 327 | – | – | 139 |
| 10/2026 | 8.823 | 8.140 | 92,3% | 733 | 8,3% | 35 | 281 | – | – | 54 |

| Período | DC/PL médio | Caixa/PL médio | Caixa médio (R$ mil) | Aquisições por mês (R$ mil) | Captação no período (R$ mil) |
|---|---:|---:|---:|---:|---:|
| 06/2024 a 12/2024 | 83,7% | 19,6% | 517 | não informado até 11/2024 | 2.000 |
| 01/2025 a 08/2025 | 89,2% | 11,9% | 570 | 611 | 4.300 |
| 09/2025 a 03/2026 | 83,8% | 21,7% | 1.590 | 562 | 0 |
| 04/2026 a 10/2026 | 93,8% | 7,7% | 663 | 891 | 0 |

Os números:

- **Fato.** Captação total de R$ 7.730 mil em nove aportes (12/2023 a 08/2025), todos do mesmo cotista. Amortização de R$ 100 mil em 10/2025. Nenhuma captação depois de 08/2025.
- **Fato.** A 1ª emissão autorizava R$ 9,5 mi. O suplemento da 4ª (2025) fala em até R$ 7 mi, mas cita o FIF por engano (D9). O teto de emissão nunca foi o limite.
- **Fato.** Cada aporte foi alocado em um a dois meses: o DC/PL voltou a 96% ou mais em 08/2024, 03/2025, 07/2025.
- **Fato.** De 09/2025 a 03/2026 o caixa ficou entre R$ 1,3 mi e R$ 1,8 mi por sete meses, com aquisições de R$ 250 mil a R$ 1,1 mi por mês.
- **Fato.** De 05/2026 a 09/2026 o DC/PL ficou entre 92% e 100%, com caixa de 1,6% a 10% do PL.
- **Fato.** A maior aquisição mensal registrada foi R$ 1.671 mil (06/2025). A média de 2026 é R$ 758 mil.

A leitura:

- **Leitura.** O limite estrutural foi capital. O fundo tem um investidor só, que parou de aportar em 08/2025, e a cota abaixo de R$ 1.000 até 05/2026 não permitia trazer terceiros.
- **Leitura.** Houve um intervalo de falta de lastro. Entre 09/2025 e 03/2026 a originação não absorveu o R$ 1 mi aportado em 08/2025. Coincide com a deterioração da carteira e com a saída da FIDD.
- **Leitura.** A carteira gira devagar. Com prazo médio perto de 290 dias, o retorno de principal é da ordem de R$ 600 mil a R$ 700 mil por mês, que é o que as aquisições de 2026 reinvestem. Hoje o fundo cresce só pelo resultado retido.
- **Leitura.** A capacidade de originação demonstrada é de R$ 1,2 mi a R$ 1,7 mi por mês no pico. Para uma compradora que queira escalar, esse é o número a testar com o grupo, não o PL.

### c) Qualidade da carteira

| Mês | Carteira bruta | Vencidos | % | 1–30d | 31–60d | 61–90d | >90d | PDD | PDD/carteira | PDD/vencidos | Taxa mín/méd/máx | Resultado | Var. PDD | Resultado ex-PDD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 10/2024 | 3.095 | 122 | 3,9% | 122 | 0 | 0 | 0 | 0 | 0,0% | 0% | – | 28 | 0 | 28 |
| 11/2024 | 2.984 | 70 | 2,3% | 60 | 10 | 0 | 0 | 56 | 1,9% | 81% | – | -32 | 56 | 24 |
| 12/2024 | 2.723 | 51 | 1,9% | 36 | 6 | 10 | 0 | 29 | 1,1% | 57% | 12,2 / 12,2 / 12,2 | 46 | -27 | 19 |
| 01/2025 | 2.795 | 31 | 1,1% | 31 | 0 | 0 | 0 | 0 | 0,0% | 0% | 9,8 / 9,8 / 9,8 | 53 | -29 | 24 |
| 02/2025 | 2.980 | 41 | 1,4% | 10 | 31 | 0 | 0 | 57 | 1,9% | 139% | 8,2 / 10,2 / 11,3 | -36 | 57 | 20 |
| 03/2025 | 3.393 | 123 | 3,6% | 79 | 18 | 25 | 0 | 178 | 5,2% | 145% | 8,7 / 9,3 / 10,5 | -84 | 122 | 37 |
| 04/2025 | 3.416 | 147 | 4,3% | 0 | 12 | 0 | 135 | 296 | 8,7% | 201% | 10,0 / 10,2 / 12,8 | -90 | 118 | 28 |
| 05/2025 | 4.317 | 175 | 4,0% | 73 | 76 | 0 | 25 | 425 | 9,8% | 243% | 9,8 / 11,1 / 18,4 | -93 | 129 | 36 |
| 06/2025 | 5.837 | 249 | 4,3% | 116 | 64 | 18 | 51 | 525 | 9,0% | 211% | 9,5 / 11,0 / 16,1 | -56 | 100 | 44 |
| 07/2025 | 6.785 | 235 | 3,5% | 118 | 59 | 36 | 21 | 430 | 6,3% | 183% | – | 170 | -95 | 75 |
| 08/2025 | 7.303 | 1.298 | 17,8% | 1.178 | 57 | 16 | 46 | 509 | 7,0% | 39% | 7,3 / 10,2 / 16,1 | 8 | 79 | 88 |
| 09/2025 | 6.731 | 194 | 2,9% | 99 | 56 | 11 | 29 | 213 | 3,2% | 110% | 7,8 / 13,1 / 13,3 | 389 | -296 | 93 |
| 10/2025 | 6.863 | 437 | 6,4% | 270 | 83 | 44 | 40 | 522 | 7,6% | 119% | 8,2 / 13,5 / 17,8 | -208 | 308 | 100 |
| 11/2025 | 6.764 | 489 | 7,2% | 284 | 109 | 28 | 69 | 716 | 10,6% | 146% | 12,0 / 12,2 / 12,7 | -104 | 195 | 90 |
| 12/2025 | 7.223 | 413 | 5,7% | 262 | 77 | 16 | 58 | 452 | 6,3% | 110% | 8,1 / 9,9 / 11,7 | 369 | -264 | 105 |
| 01/2026 | 7.041 | 368 | 5,2% | 247 | 66 | 43 | 12 | 495 | 7,0% | 135% | 9,8 / 12,3 / 17,4 | 65 | 43 | 108 |
| 02/2026 | 7.395 | 924 | 12,5% | 576 | 237 | 55 | 55 | 1.231 | 16,6% | 133% | 10,7 / 13,3 / 14,8 | -661 | 735 | 74 |
| 03/2026 | 8.147 | 1.630 | 20,0% | 707 | 556 | 247 | 121 | 3.008 | 36,9% | 185% | 13,7 / 14,0 / 25,2 | -1.691 | 1.777 | 86 |
| 04/2026 | 7.620 | 453 | 5,9% | 230 | 65 | 0 | 158 | 749 | 9,8% | 165% | 9,2 / 14,4 / 27,3 | 2.360 | -2.259 | 102 |
| 05/2026 | 8.402 | 334 | 4,0% | 234 | 46 | 29 | 25 | 379 | 4,5% | 114% | 10,8 / 13,9 / 17,6 | 461 | -370 | 91 |
| 06/2026 | 8.284 | 224 | 2,7% | 189 | 35 | 0 | 0 | 88 | 1,1% | 39% | 13,4 / 13,7 / 24,0 | 439 | -291 | 147 |
| 07/2026 | 8.463 | 618 | 7,3% | 352 | 92 | 88 | 86 | 235 | 2,8% | 38% | – | -45 | 148 | 102 |
| 08/2026 | 9.260 | 565 | 6,1% | 233 | 82 | 76 | 174 | 299 | 3,2% | 53% | 26,8 / 28,4 / 30,7 | 62 | 63 | 126 |
| 09/2026 | 9.264 | 867 | 9,4% | 570 | 19 | 35 | 243 | 282 | 3,0% | 33% | 26,8 / 35,4 / 43,3 | 173 | -17 | 157 |
| 10/2026 | 8.831 | 871 | 9,9% | 389 | 197 | 12 | 272 | 691 | 7,8% | 79% | 26,9 / 27,0 / 27,0 | -275 | 409 | 134 |

Valores em R$ mil. Taxas como informadas na tabela IX (ver D20).

**O que é o ativo**

- **Fato.** CCBs. O trimestral de 09/2024 diz "apenas com créditos consignados com formalização através de controle pelo ente consignante e o originador". Os de 12/2024 a 06/2025 dizem "apenas um originador [...] que origina CCBs provenientes da relação de fornecedores de uma cadeia produtiva que atende um único grupo econômico".
- **Fato.** O regulamento vigente nomeia a Jaguafrangos (CNPJ 85.090.033/0001-22) como Agente de Recebimento, "na qualidade de correspondente bancária da instituição financeira responsável pela concessão de crédito aos seus clientes".
- **Fato.** Cedente único em todos os meses informados: CNPJ 34.337.707/0001-00, da BMP Sociedade de Crédito Direto S.A. O nome não aparece em nenhum documento do fundo; a identificação vem da ficha do Banco Central arquivada em `raw/bcb/bcb-bmp-34337707.html`.
- **Fato.** A FIDD descreve a operação assim nos trimestrais de 12/2024 a 06/2025: "veículo de financiamento para operações de crédito para fornecedores de insumos para um grupo econômico. As relações configuram o que tipicamente podemos chamar de operações “risco-sacado".
- **Leitura.** O devedor formal é o fornecedor que emite a CCB, não a Jaguafrangos: se ela fosse a sacada, a concentração por devedor seria de 100% em um nome, e o informe mostra o maior devedor com 10%. A Jaguafrangos retém a parcela do que deve ao fornecedor e repassa ao fundo. O risco é do tomador, com a Jaguafrangos no caminho do dinheiro. Se ela tem obrigação própria de pagar (aceite ou confirmação), só o contrato de cessão diz.

**Aging e PDD**

- **Fato.** Em 10/2026: carteira bruta R$ 8.831 mil; vencidos R$ 871 mil (9,9%); acima de 90 dias R$ 272 mil; PDD R$ 691 mil (7,8% da carteira, 79% dos vencidos).
- **Fato.** A vencer em 10/2026: 23% até 90 dias, 28% acima de 360 dias, R$ 78 mil acima de 1.080 dias. Em 12/2025 eram 38% e 11%. O prazo alongou.
- **Fato.** Dois picos de vencidos que se desfazem em um a dois meses: 08/2025 (R$ 1.298 mil, 17,8%, quase tudo na faixa de 1 a 30 dias, e R$ 194 mil no mês seguinte) e 02 a 03/2026 (R$ 924 mil e R$ 1.630 mil, voltando a R$ 453 mil em 04/2026).
- **Fato.** Em 03/2026 a PDD foi a R$ 3.008 mil, 36,9% da carteira e 1,8 vez os vencidos; em 04/2026 voltou a R$ 749 mil. No mesmo mês o fundo tinha R$ 1.145 mil em disponibilidades e R$ 1.163 mil em valores a pagar; em 04/2026 os valores a pagar caíram para R$ 119 mil.
- **Fato.** A DF de 2025 explica o passivo "DC recebidos a identificar" (R$ 121 mil em 12/2025) como "direitos creditórios liquidados, e [...] envio de recursos à Classe para recompra de direitos creditórios, pendentes de conciliação pelo administrador".
- **Leitura.** O episódio de 02 a 04/2026 é conciliação, não perda. O dinheiro chegou, ficou em passivo sem baixa dos títulos, os títulos seguiram como vencidos e foram provisionados com arrasto; a conciliação de abril desfez tudo. O pico de 08/2025 tem o mesmo desenho e sugere repasse atrasado do agente de recebimento. Confirmar com balancete e extrato.
- **Fato.** A metodologia de PDD não está em nenhum documento. O regulamento remete à política do administrador; o auditor de 2025 tratou a provisão como principal assunto de auditoria.

**Recompras e substituições**

- **Fato.** O informe mensal não registra nenhuma em 35 meses. O trimestral de 09/2024 diz que há "previsão de recompra, pelo originador, de créditos que apresentem algum inadimplemento" e que "as recompras, que são raras, são feitas no Valor Presente". A DF de 2025 cita recursos recebidos para recompra.
- **Fato.** Pré-pagamentos informados somam R$ 3.109 mil no período, com R$ 855 mil só em 06/2026.
- **Leitura.** Recompras existem e não são reportadas como tal. Volume **não verificado**.

**Concentração**

- **Fato.** Cedente: 100% em um CNPJ. O regulamento dispensa limite por cedente e por devedor.
- **Fato.** Devedores em 10/2026 (tabela VIII): maior 10,0% da carteira e do PL (R$ 884 mil); cinco maiores 28,6%; dez maiores 43,3%; 25 maiores 72,4%. Na DF de 2025: maior 15,43%, dez maiores 50,58%.
- **Fato.** Nenhum devedor é nomeado em qualquer documento público.

**Taxas contra o piso de 100% do DI**

- **Fato.** Piso: até 06/2026, "ao menos 100% do CDI, calculado de forma pré-fixada em base 252 dias úteis"; desde 07/2026, "taxa mínima de cessão de 100% (cem por cento) da Taxa DI". Não há teto.
- **Fato.** Taxa média da carteira nas DFs: 17,12% e 16,95% em 2024 (CDI do ano 10,88%); 17,32% e 21,55% em 2025 (CDI 14,32%). A periodicidade não é declarada.
- **Fato.** Rendimento de direitos creditórios sobre a carteira média: 16,6% em 2024 e 17,1% em 2025. Confirma que as taxas das DFs são anuais e que ficaram entre 120% e 155% do CDI.
- **Fato.** Sob a Finaxis (08 a 10/2026) a tabela IX informa média de 27,0% a 35,4% ao ano, perto de duas vezes o CDI de 13,7%.
- **Fato.** O auditor de 2024 escreveu que os critérios de elegibilidade "estão sendo atendidos em sua maioria", sem listar as exceções.
- **Leitura.** O piso foi cumprido na média. Os valores da tabela IX sob a FIDD não servem para testar operação a operação.

### d) Custo efetivo

| Exercício | Despesas do FIDC (R$ mil) | PL médio (R$ mil) | % do PL | Adm + gestão + custódia | Camada do FIF (R$ mil) | FIDC + FIF |
|---|---:|---:|---:|---:|---:|---:|
| 2024 | 280 | 1.949 | 14,37% | 248 | 61 | cerca de 17% |
| 2025 | 274 | 5.642 | 4,86% | 252 | 58 | cerca de 6% |

Fonte: DFs auditadas (`raw/fundosnet/documentos/FIDC/862759.pdf` e `1139125.pdf`; FIF em `documentos/FIF/`). Provisão fora da conta.

- **Fato.** Sob a FIDD, o que se pagou foi o piso: R$ 8 mil de administração, R$ 8 mil de custódia e R$ 4 mil de gestão por mês, R$ 240 mil por ano.
- **Fato.** Sob Finaxis e Petra: administração (com custódia, controladoria e escrituração) de 0,40% a.a. com piso de R$ 22 mil por mês a partir do 7º mês; gestão de 0,10% a.a. com piso de R$ 6 mil. São R$ 336 mil por ano, 3,8% do PL de 10/2026, corrigidos pelo IPCA. Sem taxa de performance.
- **Fato.** O percentual só supera o piso com PL acima de R$ 66 mi (administração) e R$ 72 mi (gestão). Até lá o custo é fixo e cai proporcionalmente se o fundo crescer.
- **Fato.** A camada do FIF acabou em 02/2026.
- **Leitura.** O informe mensal não tem linha de despesa. Para 2026 só é possível afirmar o piso; a despesa real aparecerá na DF de 31/08/2026, ainda não publicada.

**Consultoria (Prosperita Consultoria e Cobrança, CNPJ 57.938.381/0001-71)**

- **Fato.** Nomeada como consultora especializada e agente de cobrança na DF de 2025 e no regulamento de 07/2026, "contratada pela Gestora, em nome do Fundo". Sede em Londrina.
- **Fato.** Sócios-administradores: Paulo Sergio Botazzari e Sidnei Donizete Bottazzari, os mesmos da Jaguafrangos. Aberta em 01/11/2024. Fonte: QSA da Receita, `raw/qsa/receita-nov2026-qsa-linhas-originais.csv`.
- **Fato.** O regulamento veda adquirir créditos "originados ou cedidos" pela consultoria "ou por partes a qualquer um deles relacionadas" (10.6). A Jaguafrangos, que origina como correspondente da BMP, é parte relacionada da consultoria.
- **Fato.** Nenhum regulamento fixa a remuneração. O vigente a lista como encargo do fundo, fora das taxas de administração e gestão e sem teto.
- **Fato.** As DFs de 2024 e 2025 não têm linha de consultoria nem de cobrança. "Outras despesas" somam R$ 7 mil e R$ 8 mil.
- **Leitura.** Até 2025 a consultoria não foi paga pelo fundo. Ou é remunerada na origem (diferença entre a taxa cobrada do tomador e a taxa de cessão ao fundo), ou pelo grupo. Com taxa de cessão de 17% a 21% ao ano num crédito a fornecedor, há espaço para um spread retido antes do fundo, mas o valor não se infere de dado público. O risco para a compradora é o inverso: o regulamento novo permite passar a cobrar do fundo sem limite.

### e) O FIF é cotista do FIDC? Quem são os 2 cotistas

- **Fato.** Sim, e era o único. O CDA do FIF mostra cotas do FIDC em todos os 26 meses de 12/2023 a 01/2026, em quantidade igual ao total emitido pelo FIDC (950,00 em 12/2023; 3.654,78 em 12/2024; 8.558,78 em 01/2026). Representavam 95% a 100% do PL do FIF. Fonte: `dados/fif_mensal.csv`.
- **Fato.** Entre os fundos que entregam CDA à CVM, nenhum outro cita o CNPJ do FIDC e nenhum cita o do FIF (35 meses varridos). FIDCs e FIPs não entregam CDA e ficam fora desse teste.
- **Fato.** O FIF tinha 2 cotistas em todos os fechamentos de mês de 12/2023 a 01/2026 (informe diário completo, `dados/fif_diario_completo.csv`). Captou R$ 7.800 mil em onze aportes.
- **Fato.** Em 02/02/2026 o informe diário do FIF registra resgate de R$ 8.023.116,10 e zero cotistas. Público-alvo: "grupo reservado de Investidores Profissionais, unidos por vínculo societário/familiar ou vínculo por interesse único e indissociável".
- **Fato.** A AGE do FIF de 02/02/2026 aprovou a liquidação antecipada com "entrega de todos os ativos aos Cotistas, proporcionalmente à sua participação". O cadastro da CVM registra o FIF em liquidação em 02/02/2026 e cancelado em 08/06/2026.
- **Fato.** O informe mensal do FIDC passa de 1 cotista ("outros fundos") em 01/2026 para 2 cotistas pessoa física em 02/2026, sem captação nem resgate.
- **Leitura.** Os 2 cotistas atuais do FIDC são os 2 ex-cotistas do FIF, que receberam as cotas em espécie.
- **Não verificado.** Os nomes. Nenhuma fonte pública identifica cotistas; as atas falam em "o Cotista" e a lista de presença não é publicada. Depende do item 1 do `PEDIDOS.md`.
- **Não verificado.** A proporção entre os dois e se são da família Botazzari. O vínculo da família com o fundo está documentado só pela consultoria e pela Jaguafrangos; nenhum documento a liga às cotas.

### f) Histórico de prestadores

| Data | Evento | Fonte |
|---|---|---|
| 28/11/2023 | Constituição. FIDD DTVM (37.678.915/0001-60) administradora; FIDD Administração de Recursos (32.582.247/0001-50) gestora. Conselho Consultivo com presidente indicado pelo cotista e poder de veto | `lista_documentos/577715.pdf` |
| 28/12/2023 | 1ª emissão (até R$ 9,5 mi) e primeira integralização | `577718.pdf` |
| 09/01/2024 | Conselho Consultivo vira Conselho de Monitoramento e perde poder sobre investimentos. Remuneração retificada | `582059.pdf` |
| 24/04/2025 | Custodiante (a própria FIDD) passa a verificar lastro. Aprova DF de 2024 | `886006.pdf` |
| 02/02/2026 | AGE do **FIF** aprova a liquidação do FIF | `1113702.pdf` (imagem) |
| 07/04/2026 | AGE aprova transferência para Finaxis CTVM (03.317.692/0001-94), Banco Finaxis (11.758.741/0001-52) e Petra Capital (09.204.714/0001-96) a partir de 27/04/2026. Gestora substituída "sem justa causa". Quitação "ampla e rasa" à FIDD | `1155920.pdf` |
| 27/04/2026 | Transferência não ocorre | informe mensal segue com FIDD até 06/2026 |
| 29/04/2026 | FIDD renuncia como administradora e gestora | edital `1177292.pdf` |
| 11/05/2026 | AGC não instalada "em razão da ausência de manifestação e de comparecimento dos Cotistas". Segunda convocação para 25/05/2026 | `1187900.pdf`, `1188594.pdf` |
| 25/05/2026 | Resultado **não verificado** (sem documento) | – |
| 03/07/2026 | Nova AGE repete as deliberações com transferência em 27/07/2026 | `1244683.pdf` |
| 27/07/2026 | Regulamento novo. Informe de 07/2026 já sai pela Finaxis | `documentos/FIDC/1269608.pdf` |

O que mudou entre a ata de abril e a de julho:

- **Fato.** A FIDD deixou de ter de entregar "lista com as pendências de lastro" e "pendências de registro dos direitos creditórios". No lugar, declara que as CCBs "foram devidamente conciliadas junto à entidade registradora, sendo passíveis de revisão no momento da transferência", que "todas as Cédulas de Crédito Bancário são de propriedade do Fundo, independentemente da modalidade de cessão" e que "o Fundo possui o lastro de todos os ativos".
- **Fato.** A auditoria de transferência ficou devida em 90 dias a contar de 27/07/2026. Não há documento publicado.

O que o regulamento de 07/2026 mudou para o cotista:

- **Fato.** Responsabilidade: "A responsabilidade dos Cotistas será ilimitada". O fundo não tem "Responsabilidade Limitada" no nome.
- **Fato.** Alocação mínima em direitos creditórios caiu de 66,7% para 50% do PL.
- **Fato.** Condições de cessão suprimidas ("Não há condições de cessão aplicáveis"); antes exigiam operações entre empresas do mesmo grupo econômico.
- **Fato.** Recebimento admitido "em uma conta de livre movimentação de titularidade do respectivo Cedente e/ou de seu correspondente bancário". "Os Devedores não serão notificados da cessão". Sem conta vinculada.
- **Fato.** Conselho extinto. Assembleia decide por maioria das cotas presentes; voto de prestadores e partes relacionadas expressamente autorizado.
- **Fato.** Público deixou de ser "um único Investidor Profissional". O administrador perdeu o poder de recusar cessionário. Não há direito de preferência.
- **Fato.** Liquidação antecipada só por assembleia ou PL abaixo de R$ 1 mi por 90 dias. Nenhum gatilho de inadimplência, concentração ou evento do cedente.
- **Fato.** Exercício social passou a encerrar em agosto. A amortização remete a um "Apêndice" que não integra o texto.
- **Fato.** O texto tem remissões a itens inexistentes e um marcador "[•]" no Suplemento D.

Auditoria:

| Exercício | Auditor | Opinião | Observação |
|---|---|---|---|
| 2023 (4 dias) | – | não auditada | dispensa regulamentar |
| 2024 | NEXT Auditores Independentes (19.280.834/0001-26) | sem ressalva, com ênfase | ênfase sobre 2023 não auditado; elegibilidade atendida "em sua maioria" |
| 2025 | NEXT | sem ressalva, com ênfase | ênfase e nota 20 contraditórias (D10); provisão como principal assunto |
| 01/01 a 31/08/2026 | – | não publicada | primeira DF sob a Finaxis |

- **Fato.** Nenhuma ressalva, abstenção ou opinião adversa nas DFs do FIDC ou do FIF.
- **Fato.** Trimestral do 2T26 não foi publicado.

### g) Queda do PL de 09 para 10/2026

| Item | 30/09/2026 | 31/10/2026 | Variação |
|---|---:|---:|---:|
| Créditos a vencer | 8.397.451,78 | 7.960.469,83 | -436.981,95 |
| Créditos vencidos | 866.949,18 | 870.546,83 | +3.597,65 |
| Provisão (PDD) | -282.182,70 | -690.770,52 | **-408.587,82** |
| Direitos creditórios líquidos | 8.982.218,26 | 8.140.246,14 | -841.972,12 |
| Cotas de fundos de liquidez | 176.356,41 | 692.565,49 | +516.209,08 |
| Títulos públicos | 39.714,16 | 40.125,18 | +411,02 |
| Disponibilidades | 34.146,69 | -4,85 | -34.151,54 |
| Outros ativos | 4.344,21 | 4.024,52 | -319,69 |
| **Ativo** | 9.236.779,73 | 8.876.956,48 | -359.823,25 |
| Valores a pagar | 138.748,53 | 53.966,62 | -84.781,91 |
| **Patrimônio líquido** | 9.098.031,20 | 8.822.989,86 | **-275.041,34** |
| Cotas em circulação | 8.550,146536 | 8.550,146536 | 0 |
| Valor da cota | 1.064,08 | 1.031,91 | -3,02% |

- **Fato.** Não houve captação, amortização nem resgate. A quantidade de cotas não mudou. A queda é toda resultado.
- **Fato.** A provisão subiu R$ 408,6 mil (145%). Sem ela o mês teria rendido R$ 133,5 mil, 1,47% do PL, em linha com os meses anteriores.
- **Fato.** O total de vencidos ficou estável, mas envelheceu: de 1 a 30 dias caiu de R$ 570 mil para R$ 389 mil; de 31 a 60 dias subiu de R$ 19 mil para R$ 197 mil; acima de 120 dias subiu de R$ 168 mil para R$ 237 mil.
- **Fato.** A cobertura dos vencidos pela PDD passou de 33% para 79%.
- **Fato.** A carteira a vencer encolheu R$ 437 mil e o caixa subiu R$ 516 mil: as aquisições do mês (R$ 281 mil) não repuseram as liquidações.
- **Leitura.** Cerca de R$ 197 mil da safra de vencidos de setembro não curou e rolou para a faixa de 31 a 60 dias, e a política da Finaxis parece provisionar o saldo inteiro do devedor em atraso (arrasto), não só a parcela vencida. Isso explica a PDD subir muito mais do que os vencidos.
- **Fato.** A ANBIMA expediu carta de recomendação ao Grupo Finaxis, aceita em 20/04/2026, por não aplicar o efeito vagão "de forma tempestiva e abrangente" nos FIDCs que administra. A Finaxis se comprometeu a implantar nova metodologia de PDD, com prazo final de 165 dias, que cai em 02/10/2026. Fonte: `raw/processos/anbima_grupo_finaxis_CR_AGRT003_2026.pdf`.
- **Leitura.** A alta de outubro é compatível com a entrada em vigor dessa metodologia. Pode ser perda real ou critério mais conservador; os dados públicos não separam as duas coisas. Depende da memória de cálculo.

---

## 4. Outros achados relevantes para a compradora

- **Sucessão da Jaguafrangos no Grupo Pesqueiro.** Processo 1073997-19.2025.8.11.0041, TJMT. Decisão de 07/2026 reconheceu "sucessão empresarial de fato" da Jaguafrangos, com responsabilidade solidária pelos passivos da massa e possível extensão a outras sociedades do Grupo BTZ e a pessoas naturais. A de 10/2026 rejeitou integralmente os embargos da Jaguafrangos, esclareceu que isso "não equivale à decretação autônoma de sua falência" e manteve a ordem de individualizar "contas bancárias e demais ativos". Fonte: Diário de Justiça Eletrônico Nacional, `raw/processos/cnj_djen_jaguafrangos_tjmt_1073997.json`. Como a Jaguafrangos recebe os pagamentos do fundo em conta própria, uma constrição sobre as contas dela alcança o fluxo do FIDC.
- **Multa da Lei Anticorrupção.** TRF4, processo 5019968-85.2024.4.04.7001, 17/11/2026: restabelecida multa de R$ 19.850.025,41 aplicada à Jaguafrangos em processo de responsabilização do Ministério da Agricultura. Fonte: `raw/processos/cnj_djen_jaguafrangos_federal_5019968.json`.
- **Variação diária da cota.** O informe diário do FIF mostra quedas de 13% a 17% dentro do mês em 12/2025 e 01/2026, revertidas em um dia no fechamento. Detalhe em `ESTUDO.md`, seção 5.
- **FIDC Agro Paraná.** O informativo da Fomento Paraná de 11/2026 lista "Jaguafrangos: Fomento Paraná R$ 40 mi; Patrimônio do FIDC R$ 200 mi" na linha "aguardam assinatura". É um veículo para financiar integrados com cotista sênior público e taxa subsidiada. Pode disputar o mesmo lastro do Prosperità. Fonte: `raw/btz/fomento_pr_nov2026.pdf`, p. 10.
- **Homônimo novo.** "Consignado Prosperita FIDC – Responsabilidade Limitada" (CNPJ 68.543.762/0001-78), registrado em 12/08/2026, administrador Hemera DTVM, gestor Solis. Vínculo com a Prosperita Consultoria **não verificado**. Fonte: `raw/cadastro/registro_fundo_classe.zip`.
- **Correspondente bancário.** A consulta do Soul ao Banco Central por Jaguafrangos como correspondente voltou vazia (`raw/btz/bcb_jaguafrangos_*.json`), embora o regulamento a qualifique assim.

---

## 5. Pedidos de documentos

As listas por destinatário estão em `PEDIDOS_DE_DOCUMENTOS.md` (80 itens em oito listas, com prioridade e a dúvida que cada um resolve).

---

## 6. Como reproduzir

Com o hub clonado na branch da coleta:

```
RAW=<hub>/dossies/prosperita-fidc/raw
python3 -I scripts/extrai_fidc.py $RAW out/fidc
python3 -I scripts/confere_fidc.py out/fidc <hub>/dossies/prosperita-fidc/dados
python3 -I scripts/extrai_cda.py $RAW out/cda
python3 -I scripts/painel.py out/fidc $RAW out/dados
python3 -I scripts/fif.py out/cda/hits.csv out/dados out/dados/painel_mensal_fidc.csv
python3 -I scripts/tabelas_md.py out/dados/painel_mensal_fidc.csv out
```

| Arquivo | Conteúdo |
|---|---|
| `dados/painel_mensal_fidc.csv` | 35 meses, 64 colunas: PL, cota, CDI, alocação, aquisições, aging, PDD, resultado |
| `dados/fif_mensal.csv` | PL do FIF, cotas do FIDC detidas, cotistas, captação |
| `dados/fif_diario_completo.csv` | 530 dias de cota, PL, captação, resgate e cotistas do FIF |
| `dados/fidc_tab_viii_25_maiores.csv` | 25 maiores exposições por mês |
| `dados/fif_cda_demais_itens.csv` | disponibilidades e provisões de taxas do FIF |
| `dados/fif_linhas_brutas_cda_diario.tsv` | 872 linhas brutas do FIF nos zips da CVM |
| `dados/reextracao_informe_mensal/` | as 18 tabelas reextraídas, base da comparação com o Soul |

Leituras de PDF: regulamentos, DFs e trimestrais foram lidos por três agentes auxiliares com roteiro de extração; conferi por busca no texto todas as citações que entraram aqui. Os balanços das DFs de 2024 e 2025 são imagem no PDF; os valores vêm da leitura visual das páginas e batem com as notas em texto e com o informe mensal de dezembro.
