# Prosperità FIDC: estudo para a aquisição

> Substituído pelo relatório final em `relatorio/RELATORIO_FINAL.md` (PDF na mesma pasta), que corrige três pontos deste estudo: há bloqueio de R$ 2,24 mi em contas da Jaguafrangos na execução trabalhista do TRT-12; a operação da Polícia Federal atingiu a BMP SCMEPP, não a BMP SCD cedente; e o Consignado Prosperita FIDC não tem vínculo com o grupo.

Data: 26/11/2026. CNPJ do fundo: 53.033.766/0001-39.

Este estudo consolida a conferência dos dados públicos (detalhe em `RELATORIO.md`), o complemento da coleta do Soul (PR #91 do hub, commit `770cb10`) e a pesquisa em fontes abertas feita nesta sessão. As listas do que pedir a cada parte estão em `PEDIDOS_DE_DOCUMENTOS.md`.

| Marca | Significado |
|---|---|
| **Fato** | consta em arquivo bruto do hub; conferido por mim |
| **Busca web** | resumo de resultado de busca; a página não abriu neste ambiente |
| **Leitura** | inferência minha; precisa de confirmação |
| **Não verificado** | sem fonte que eu tenha aberto |

---

## 1. Conclusão

O Prosperità é um fundo de R$ 8,8 mi que financia fornecedores do Grupo BTZ por meio de CCBs emitidas na BMP e cobradas por retenção na Jaguafrangos. A carteira rende perto de 17% ao ano antes de provisão. O cotista ficou com 3,94% em 35 meses, contra 41,70% do CDI, porque o custo fixo e a provisão comeram a diferença.

O que a compradora compra não é uma carteira independente. O grupo vendedor origina o crédito, recebe o pagamento em conta própria, cobra os atrasos e presta a consultoria. A empresa de consultoria e cobrança tem os mesmos dois sócios-administradores da Jaguafrangos. O regulamento vigente não tem limite de concentração, conta vinculada, gatilho de inadimplência nem conselho, e a responsabilidade do cotista é ilimitada.

Cinco perguntas decidem a operação:

1. **O dinheiro chega ao fundo sem passar pelo risco da Jaguafrangos?** Hoje não. E a Jaguafrangos foi declarada sucessora de fato do Grupo Pesqueiro, falido, com responsabilidade solidária pelos passivos.
2. **Quanto da provisão de R$ 691 mil é perda e quanto é critério?** A Finaxis mudou a metodologia em 2026 por recomendação da ANBIMA.
3. **Os episódios de 08/2025, 12/2025, 01/2026 e 02 a 04/2026 foram só conciliação?** A cota diária chegou a cair de 9% a 11% dentro do mês e a subir de 13% a 17% em um dia, no fechamento.
4. **Quem são os dois cotistas e o que a família controla depois da venda?** Se ela fica com participação e mantém origem e cobrança, o desenho de cotas precisa refletir isso.
5. **O regulamento pode ser reescrito antes da entrada?** Responsabilidade limitada, conta do fundo, limites, gatilhos e teto para a consultoria.

---

## 2. Quem é quem

| Papel | Quem | CNPJ | Controle | Fonte |
|---|---|---|---|---|
| Cotistas | 2 pessoas físicas, não identificadas | – | – | informe mensal, 02/2026 em diante |
| Cotista anterior | Prosperità FIF MM CP, liquidado em 02/2026 | 53.071.764/0001-34 | 2 cotistas "unidos por vínculo societário/familiar" | CDA, informe diário, DF do FIF |
| Cedente | BMP Sociedade de Crédito Direto S.A. | 34.337.707/0001-00 | – | informe mensal (23 competências); ficha do Banco Central em `raw/bcb/bcb-bmp-34337707.html` |
| Agente de recebimento e correspondente | Jaguafrangos Indústria e Comércio de Alimentos Ltda. | 85.090.033/0001-22 | Paulo Sergio Botazzari e Sidnei Donizete Bottazzari, sócios-administradores desde 1997; quatro sócios novos em 24/11/2025 | regulamento de 07/2026; QSA da Receita |
| Consultoria e cobrança | Prosperita Consultoria e Cobrança Ltda. | 57.938.381/0001-71 | os mesmos dois sócios-administradores; aberta em 01/11/2024, capital de R$ 10 mil, Londrina | QSA da Receita; cadastro |
| Holding da família | S&PB Administração de Bens Ltda. | 38.660.087/0001-04 | os mesmos dois; capital de R$ 39,7 mi, Jaguapitã | QSA da Receita; cadastro |
| Administradora | Finaxis CTVM S.A. | 03.317.692/0001-94 | grupo Finaxis | regulamento; cadastro CVM |
| Custodiante | Banco Finaxis S.A. | 11.758.741/0001-52 | grupo Finaxis | idem |
| Gestora | Petra Capital Gestão de Investimentos Ltda. | 09.204.714/0001-96 | sócios e diretores em comum com a Finaxis | QSA da Receita |
| Auditor | NEXT Auditores Independentes | 19.280.834/0001-26 | – | cadastro CVM; DFs |
| Administradora e gestora até 07/2026 | FIDD DTVM e FIDD Administração de Recursos | 37.678.915/0001-60 e 32.582.247/0001-50 | – | atas; informe mensal |
| Devedores | fornecedores do grupo, não nomeados | – | – | trimestrais; DFs |

- **Fato.** O QSA da Receita não traz percentual de participação. As linhas originais estão em `raw/qsa/receita-nov2026-qsa-linhas-originais.csv`.
- **Fato.** O cadastro de capital, endereço e data de abertura vem de espelho (OpenCNPJ), não de cartão oficial. Os cartões em PDF não foram obtidos.
- **Leitura.** Os dois cotistas são provavelmente os dois sócios-administradores ou pessoas da família. Nenhum documento público confirma.
- **Leitura.** Origem, recebimento, cobrança, consultoria e, provavelmente, as cotas estão no mesmo grupo. Administração, custódia e gestão estão em outro grupo único. Os únicos terceiros de fato são o auditor e a registradora, que não é nomeada.

---

## 3. Como o dinheiro circula

1. Um fornecedor do grupo toma crédito emitindo uma CCB na BMP. A Jaguafrangos atua como correspondente bancária da BMP.
2. A BMP cede a CCB ao fundo, sem coobrigação, por taxa de no mínimo 100% do DI.
3. A Jaguafrangos retém a parcela do que deve ao fornecedor.
4. O valor entra "em uma conta de livre movimentação de titularidade do respectivo Cedente e/ou de seu correspondente bancário, para posterior transferência à conta de titularidade do Fundo" (regulamento, 13.1).
5. O fundo baixa a parcela quando identifica o recebimento. Enquanto não identifica, o título conta como vencido e é provisionado.
6. Em atraso, a Prosperita Consultoria cobra. Recompra pelo originador existe na prática, sem regra no regulamento.

- **Fato.** Passos 1, 2, 4 e 6 constam do regulamento, dos trimestrais e das DFs. "Os Devedores não serão notificados da cessão" (14.31).
- **Fato.** A consulta do Soul ao Banco Central por correspondentes com a raiz da Jaguafrangos voltou vazia.
- **Leitura.** O passo 3 é a minha reconstrução do que os trimestrais chamam de crédito "com formalização através de controle pelo ente consignante" e de operação "risco-sacado". Se a Jaguafrangos assume obrigação própria de pagar, só o contrato diz.
- **Leitura.** Entre os passos 4 e 5 o dinheiro do fundo fica em conta de terceiro. É o ponto mais frágil da estrutura.

---

## 4. O que os números mostram

Detalhe mês a mês em `RELATORIO.md`, seção 3, e em `dados/painel_mensal_fidc.csv`.

| Indicador | Valor | Fonte |
|---|---|---|
| PL em 31/10/2026 | R$ 8.823 mil | informe mensal |
| Captado desde 12/2023 | R$ 7.730 mil no FIDC; R$ 7.800 mil no FIF | informe mensal; informe diário |
| Rentabilidade da cota em 35 meses | 3,94% | informe mensal, encadeada |
| CDI no período | 41,70% | Banco Central, série 12 |
| TIR do cotista no FIDC | 8,3% a.a. | fluxos mensais |
| Resultado antes de provisão desde o início | R$ 1.884 mil | painel |
| Resultado antes de provisão em 2026 | 16,7% a.a. sobre o PL médio | painel |
| Saldo de PDD | R$ 691 mil, 7,8% da carteira | informe mensal |
| Despesas sobre PL médio | 14,4% em 2024; 4,9% em 2025 | DFs auditadas |
| Piso de taxas sob a Finaxis | R$ 336 mil por ano, 3,8% do PL | regulamento |
| Vencidos em 10/2026 | R$ 871 mil, 9,9% da carteira; R$ 272 mil acima de 90 dias | informe mensal |
| Maior devedor | R$ 884 mil, 10% do PL | informe mensal, tabela VIII |
| 25 maiores devedores | 72% da carteira | idem |
| Prazo médio a vencer | perto de 290 dias; 28% acima de 360 dias | informe mensal, tabela V |
| Alocação em direitos creditórios | 94% do PL de 04 a 10/2026 | painel |
| Aquisições em 2026 | R$ 758 mil por mês em média | informe mensal, tabela VII |

- **Leitura.** A máquina funciona: taxa de 120% a 155% do CDI, alocação alta, originação recorrente. O que falta é escala para diluir R$ 336 mil de custo fixo e disciplina de recebimento para parar de provisionar o que foi pago.
- **Leitura.** Com o PL atual, o custo fixo consome cerca de um quinto do rendimento bruto. A R$ 30 mi cairia para perto de 1,1% do PL.

---

## 5. Os episódios de marcação

O informe mensal mostra a cota só no fechamento. O informe diário do FIF, que tinha de 95% a 100% do patrimônio em cotas do FIDC, mostra o que aconteceu dentro do mês. Fonte: `dados/fif_diario_completo.csv` (530 dias, 28/12/2023 a 11/02/2026).

| Mês | Cota no início | Mínima no mês | Cota no fim | Maior alta em um dia |
|---|---:|---:|---:|---|
| 09/2025 | 854,99 | 825,78 | 898,46 | +4,47% em 29/09 |
| 11/2025 | 867,89 | 843,03 | 863,00 | +5,62% em 14/11 |
| 12/2025 | 849,70 | 782,49 | 904,31 | +16,85% em 23/12 |
| 01/2026 | 901,06 | 804,49 | 911,25 | +13,27% em 30/01 |

- **Fato.** Até 08/2025 a maior variação diária foi de cerca de 2%. De 09/2025 em diante a cota passou a cair ao longo do mês e a recuperar tudo em um dia.
- **Fato.** Em 30/01/2026, último dia útil do mês, a cota subiu 13,27%. Em 02/02/2026 o FIF foi liquidado e resgatou R$ 8.023.116,10 a essa cota.
- **Fato.** Em 02 e 03/2026 a recuperação não veio no fechamento: a cota do FIDC caiu 8,26% e 23,04%, com PDD de R$ 3,0 mi, disponibilidades de R$ 1,1 mi e valores a pagar de R$ 1,2 mi. Em 04/2026 subiu 41,80%.
- **Fato.** A DF de 2025 descreve o passivo "DC recebidos a identificar" como recebimentos e recompras "pendentes de conciliação pelo administrador".
- **Leitura.** O fundo provisiona diariamente títulos cujo pagamento já saiu do devedor e ainda não foi identificado. Quando o repasse é conciliado, a provisão reverte de uma vez. Em 02 e 03/2026 a conciliação atrasou dois meses.
- **Busca web.** Em 25/02/2026 a Polícia Federal fez buscas na sede da BMP (Operação Cliente Fantasma), por suspeita de facilitar lavagem de dinheiro. A BMP declarou que as operações seguiram normais. As matérias citam a entidade "Money Plus SCMEPP"; se a BMP SCD, cedente do fundo, foi alcançada, **não verifiquei**.
- **Leitura.** A coincidência de datas entre a operação na BMP e o atraso de conciliação de 02 a 03/2026 merece pergunta direta. Não há evidência de relação.
- **Fato.** A FIDD renunciou em 29/04/2026, dois dias depois de falhar a primeira data de transferência.

**A provisão de 10/2026**

- **Fato.** A PDD subiu R$ 409 mil com vencidos estáveis; a cobertura dos vencidos foi de 33% para 79%.
- **Fato.** A ANBIMA expediu carta de recomendação ao Grupo Finaxis, aceita em 20/04/2026, por "não demonstrar aplicar o efeito vagão de forma tempestiva e abrangente sobre todo o fluxo de caixa esperado de um mesmo devedor" e por concentrar a análise de risco no cedente em fundos sem coobrigação. A Finaxis se comprometeu a implantar nova metodologia de PDD em até 120 dias e a cumprir tudo em até 165 dias. Fonte: `raw/processos/anbima_grupo_finaxis_CR_AGRT003_2026.pdf`.
- **Leitura.** 165 dias depois de 20/04/2026 é 02/10/2026. A alta de outubro é compatível com a entrada em vigor da metodologia nova, que provisiona o saldo inteiro do devedor em atraso. Num fundo com 25 devedores somando 72% da carteira, o efeito vagão pesa muito: um devedor grande com uma parcela atrasada arrasta o saldo todo.
- **Leitura.** A provisão vai continuar volátil enquanto o recebimento passar por conta de terceiro.

---

## 6. Riscos, por ordem de peso

### 6.1 Jaguafrangos no caminho do dinheiro

- **Fato.** Falência do Grupo Pesqueiro, processo 1073997-19.2025.8.11.0041, 1ª Vara Cível Especializada de Cuiabá. Decisão publicada em 09/07/2026 reconheceu "sucessão empresarial de fato" da Jaguafrangos, "com responsabilidade solidária pelos passivos vinculados à massa falida, sem prejuízo da apuração posterior, em incidente próprio, da extensão subjetiva a outras sociedades do Grupo BTZ e a pessoas naturais eventualmente beneficia[das]". Fonte: Diário de Justiça Eletrônico Nacional, `raw/processos/cnj_djen_jaguafrangos_tjmt_1073997.json`.
- **Fato.** A mesma decisão cita entradas e saídas de R$ 7.353.012,96 "absorvidos pela Jaguafrangos", contrato de locação de 10/07/2019 das plantas das falidas, uso das marcas Unibon e Satiare, e sucessão já reconhecida pela Justiça do Trabalho nos autos 0001363-25.2019.5.12.0025.
- **Fato.** Decisão publicada em 01/10/2026 rejeitou integralmente os embargos da Jaguafrangos. Esclareceu que a sucessão "não equivale à decretação autônoma de sua falência" e manteve a ordem para a Administradora Judicial individualizar "contas bancárias e demais ativos" ligados à sucessão. Um credor, a Travessia Securitizadora, declara crédito de cerca de R$ 17,5 mi.
- **Busca web.** O valor da causa passa de R$ 200 mi.
- **Fato.** Não há registro de bloqueio de contas nas decisões lidas.
- **Fato.** TRF4, processo 5019968-85.2024.4.04.7001, julgamento de 17/11/2026: a 12ª Turma, por unanimidade, deu provimento à apelação da União e restabeleceu multa de R$ 19.850.025,41 e publicação extraordinária da condenação, em processo de responsabilização do Ministério da Agricultura com base na Lei Anticorrupção. A ementa fala em "doação de mercadorias a pedido de fiscal agropecuário". A Jaguafrangos é a parte intimada. Fonte: `raw/processos/cnj_djen_jaguafrangos_federal_5019968.json`.
- **Fato.** Ações civis públicas do Ministério Público do Trabalho: acordo homologado nos autos 0001209-69.2025.5.09.4199, com R$ 3.065.878,05 de ressarcimento ao INSS divulgados; segunda ação, por explosão de reator, pede ao menos R$ 10 mi.
- **Leitura.** O risco não é o fornecedor deixar de pagar. É a Jaguafrangos reter e não repassar, por decisão própria ou por ordem judicial sobre as contas dela. A individualização de contas em curso no TJMT é o gatilho a acompanhar.

### 6.2 Partes relacionadas

- **Fato.** A consultora e agente de cobrança do fundo tem os mesmos sócios-administradores do agente de recebimento. Foi aberta em 01/11/2024, onze meses depois da constituição do fundo.
- **Fato.** O regulamento veda adquirir direitos creditórios "originados ou cedidos pela Administradora, pela Gestora, pelo Custodiante, pela Consultoria Especializada, pela Entidade Registradora ou por partes a qualquer um deles relacionadas" (10.6).
- **Fato.** O regulamento autoriza expressamente o voto de prestadores e partes relacionadas em assembleia (22.5.2), extinguiu o conselho e permite vender créditos a cedentes e partes relacionadas (10.8).
- **Fato.** A consultoria pode ser subcontratada para verificar lastro (11.2.2.1). Sua remuneração não tem valor nem teto no regulamento, e as DFs de 2024 e 2025 não têm linha de despesa para ela.
- **Leitura.** A cláusula 10.6 precisa de parecer. O cedente formal é a BMP, mas quem origina na prática é a Jaguafrangos, parte relacionada da consultoria. Se a leitura for a restritiva, toda a carteira está em desacordo com o regulamento.

### 6.3 O cedente

- **Fato.** A BMP cede sem coobrigação. O fundo depende dela para a formalização e o registro das CCBs.
- **Busca web.** Além da operação da Polícia Federal em 02/2026, as matérias citam inspeção do Banco Central homologada em 31/12/2024, com 25 não conformidades em prevenção à lavagem, e o ataque de 07/2025 às contas de liquidação por meio da C&M Software.
- **Fato.** A ata de 03/07/2026 traz declaração da FIDD de que as CCBs "foram devidamente conciliadas junto à entidade registradora, sendo passíveis de revisão no momento da transferência". A versão de abril exigia entregar lista de pendências de lastro e de registro; a de julho retirou a exigência.
- **Leitura.** Vale testar o registro de cada CCB e a titularidade do fundo na registradora, não por amostra.

### 6.4 Responsabilidade do cotista

- **Fato.** "A responsabilidade dos Cotistas será ilimitada" (15.1.1.2). O fundo não tem "Responsabilidade Limitada" na denominação.
- **Leitura.** Com a Jaguafrangos em disputa de sucessão e o cedente sob investigação, a compradora não deve entrar antes de o fundo adotar responsabilidade limitada.

### 6.5 Concentração e prazo

- **Fato.** Sem limite por cedente ou devedor no regulamento. Maior devedor com 10% do PL. Fatia a vencer acima de 360 dias subiu de 11% para 28% em dez meses.
- **Leitura.** O fundo está migrando de capital de giro para financiamento de prazo longo dos fornecedores. Com efeito vagão, cada devedor grande em atraso custa vários pontos de cota.

### 6.6 Custo

- **Fato.** Piso de R$ 28 mil por mês para administração e gestão, corrigido pelo IPCA. Consultoria e cobrança são encargo do fundo sem teto.
- **Leitura.** Abaixo de R$ 20 mi de PL o custo fixo sozinho tira 1,7 ponto de retorno ou mais.

### 6.7 Qualidade de informação

- **Fato.** A DF de 31/12/2025 se contradiz sobre a assembleia de 02/02/2026. O auditor de 2024 registrou critérios de elegibilidade atendidos "em sua maioria". Trimestrais de 2025 negam cessões que o informe mensal registra. O trimestral do 2T26, a auditoria de transferência e a DF de 31/08/2026 não estão publicados.
- **Busca web.** A FIDD Administração de Recursos recebeu carta de recomendação da ANBIMA em 19/01/2026, relativa à administração de FIPs. O documento não foi aberto.
- **Fato.** Finaxis e Petra têm histórico em autorregulação e na CVM: termo de compromisso da Petra com a ANBIMA em 06/10/2025 por controles de enquadramento e de aquisição de crédito privado; processos da CVM de 2016 sobre custódia e verificação de lastro de FIDC envolvendo o então Banco Petra, hoje Banco Finaxis. Fonte: `raw/processos/`.
- **Leitura.** O período FIDD precisa de auditoria própria da compradora. A quitação "ampla e rasa" dada pelos cotistas limita o que se pode cobrar depois.

### 6.8 Concorrência pelo mesmo lastro

- **Fato.** O informativo da Fomento Paraná de 11/2026 lista a Jaguafrangos em "aguardam assinatura": R$ 40 mi da Fomento num FIDC de R$ 200 mi.
- **Busca web.** No programa, a Fomento é a única cotista sênior e o proponente aporta a subordinada. A Jaguafrangos aparece na priorização do edital, publicada em 11/2025, com nota 86,96. Os fundos financiam aviários e instalações de integrados com juro subsidiado.
- **Leitura.** Se sair, o grupo terá um veículo de R$ 200 mi, com dinheiro público barato, para o mesmo público do Prosperità, e terá de aportar a cota subordinada. Perguntar ao grupo o que sobra para o Prosperità.
- **Fato.** Há um "Consignado Prosperita FIDC" (CNPJ 68.543.762/0001-78), registrado em 12/08/2026, com outro administrador e outro gestor. Vínculo **não verificado**.

---

## 7. O que muda na operação

Tudo nesta seção é **leitura**, para discutir com a cliente e com o jurídico.

**Preço**

- O PL de R$ 8,82 mi já desconta R$ 691 mil de provisão. Se parte for critério e não perda, há valor escondido; se os vencidos acima de 90 dias (R$ 272 mil) e o maior devedor estiverem piores do que parecem, há perda escondida. A resposta está na memória de cálculo e na posição por devedor.
- Ajustes a verificar antes de fechar preço: recebimentos a identificar, recompras pendentes, despesas não provisionadas (auditoria de transferência, DF de agosto, eventual consultoria retroativa).
- Data-base: a cota de fechamento de mês tem sido melhor que a de meio de mês. Fixar preço por cota de fim de mês conciliado, com ajuste posterior.

**Forma de entrada**

- Comprar cotas dos atuais cotistas põe o dinheiro no bolso da família e não aumenta o fundo. Subscrever cotas novas aumenta o fundo e dilui o custo fixo. O regulamento não dá direito de preferência aos atuais.
- A classe é única e o regulamento veda subordinação. Se a família fica e continua controlando origem e cobrança, o desenho coerente é ela ficar em cota subordinada e a compradora em sênior. Exige reforma do regulamento.
- Risco sacado e risco cedente no mesmo veículo pedem critérios separados de elegibilidade, de concentração e de provisão. O regulamento atual não distingue.

**Condições a negociar antes de entrar**

1. Fundo com responsabilidade limitada.
2. Recebimento em conta do fundo ou em conta vinculada, com notificação aos devedores ou cessão fiduciária dos pagamentos da Jaguafrangos aos fornecedores.
3. Contrato de consultoria e cobrança com preço, teto, metas e possibilidade de troca sem o voto das partes relacionadas.
4. Limites de concentração por devedor e gatilhos de avaliação por inadimplência, atraso de repasse e evento na Jaguafrangos.
5. Regra escrita de recompra e de substituição.
6. Verificação integral de lastro e de registro das CCBs antes do fechamento.
7. Declarações e garantias dos vendedores sobre o período FIDD e sobre o processo do Grupo Pesqueiro.
8. Parecer sobre a cláusula 10.6.
9. Assento em comitê ou direito de veto sobre elegibilidade e troca de prestadores.

---

## 8. O que continua aberto

| Pergunta | Onde está a resposta |
|---|---|
| Quem são os dois cotistas e em que proporção | lista de cotistas |
| A Jaguafrangos tem obrigação própria de pagar | contrato de cessão e convênio com a BMP |
| Prazo real de repasse, mês a mês | extratos da conta de recebimento |
| Quanto da PDD é perda | memória de cálculo e posição por devedor |
| O que houve de 02 a 04/2026 | balancetes e conciliação |
| Por que a FIDD renunciou | carta de renúncia; ata de 25/05/2026 |
| Quem paga a consultoria e quanto | contrato |
| Volume de recompras | relatório por mês |
| A BMP SCD foi alcançada pela operação da Polícia Federal | BMP; gestora |
| Estado do processo do Grupo Pesqueiro e risco de constrição | autos; advogado do grupo |
| Faturamento, dívida e covenants do grupo | DFs auditadas do Grupo BTZ |
| O FIDC com a Fomento Paraná vai sair e o que financia | grupo; Fomento |

---

## 9. Fontes abertas consultadas nesta sessão

Este ambiente não abre páginas de notícia nem os portais da CVM e do Banco Central; as buscas voltaram só com resumo. Os fatos centrais da seção 6.1 não dependem delas: foram conferidos no Diário de Justiça Eletrônico Nacional arquivado no hub.

- Sucessão no Grupo Pesqueiro: [Compre Rural](https://comprerural.com/justica-reconhece-sucessao-empresarial-e-inclui-jaguafrangos-na-falencia-do-grupo-pesqueiro/)
- Operação Cliente Fantasma e BMP: [Finsiders](https://finsidersbrasil.com.br/noticias-sobre-fintechs/pf-faz-buscas-na-bmp-o-banco-do-futuro-por-suspeita-de-facilitar-lavagem-de-r-25-bi-de-faccoes/), [Money Times](https://www.moneytimes.com.br/pf-faz-buscas-em-banco-em-sp-sob-suspeita-de-facilitar-lavagem-de-r-25-bilhoes-de-faccoes/), [Gazeta do Povo](https://www.gazetadopovo.com.br/brasil/pf-investiga-banco-suspeito-movimentar-25-bilhoes-organizacoes-criminosas/), [Convergência Digital](https://convergenciadigital.com.br/mercado/alvo-do-maior-ataque-hacker-financeiro-do-pais-bmp-e-investigada-por-suspeita-de-facilitar-lavagem-de-mais-de-r-25-bilhoes/), [comunicado da BMP](https://uploads.finsidersbrasil.com.br/2026/02/Comunicado-Oficial-BMP.pdf)
- FIDC Agro Paraná: [priorização do edital, Fomento Paraná](https://www.fomento.pr.gov.br/sites/default/arquivos_restritos/files/documento/2025-11/resultado_inicial_da_priorizacao_-_edital_fidc_0.pdf), [chamada pública](https://www.fomento.pr.gov.br/sites/default/arquivos_restritos/files/documento/2025-06/ed_2025-01-chamada_publica_fidcs_agro.pdf), [Forbes Agro](https://forbes.com.br/forbes-agro/2026/02/mbrf-aporta-r-300-milhoes-em-fidc-para-aves-e-suinos-com-participacao-da-fomento-parana/)
- FIDD: [carta de recomendação da ANBIMA, 19/01/2026](https://www.anbima.com.br/data/files/09/21/1F/F9/73F0C91052FACFB9F82BA2A8/19.01.2026%20-%20CR%20-%20AGRT%20-%20FIDD%20Administracao%20De%20Recursos%20Ltda.pdf)
- Menestys Gestora de Recursos (assina trimestrais do fundo de 09/2025 a 03/2026): [Mais Retorno](https://maisretorno.com/gestores/fidd), [TradeMap](https://trademap.com.br/fundos/gestoras/50543106000100). A busca não achou vínculo com a FIDD.

Buscas sem resultado útil: faturamento e dívida do Grupo BTZ; Prosperita Consultoria; Consignado Prosperita FIDC; motivo da renúncia da FIDD.
