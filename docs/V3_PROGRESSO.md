# Progresso da terceira edição

Atualização de 05-11-2026. Branch `terceira-edicao-ia-referencia-2026`, [PR #2 em Draft](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/2).

## Checkpoint K — edição final

A sequência dos 50 capítulos foi revista a partir dos objetivos, exemplos e transições. A primeira conversa passou para o capítulo 2. O leitor pode experimentar tarefas em papel antes de abrir treino, atenção e geração. Dados, código e especificação formam uma passagem para a construção de sistemas.

A reserva da biblioteca foi escolhida para a entrada depois de comparar três casos. A ficha separa o que chegou, o que está confirmado e o que a pessoa pode fazer a seguir. A Lavandaria tem um percurso próprio para os laboratórios com consultas, regras de acesso, cache e resultados reproduzíveis.

O título está alinhado na capa, na folha de rosto e nos metadados. Os capítulos, os 74 laboratórios, as 93 referências e os 70 termos constam da edição compilada. A [ancoragem](V3_ANCORAGEM.md) liga a revisão aos blocos e a [validação](V3_VALIDACAO.md) regista os resultados e o alcance da leitura.

## Checkpoint J — explicações de base e ensaios

O ponto de partida explica proporções, médias, letras, unidades, programas e pedidos entre serviços. Foram revistos os capítulos 01, 06–08, 13, 21–22, 25, 28, 31–33, 40–42, 44, 47 e 49 pelos prefixos dos ficheiros. As fórmulas preservam o detalhe técnico e passam a ter uma conta comentada ou um percurso acessível antes da notação. O glossário tem 70 termos.

- **Fontes.** Confirmados o alcance dos estudos de rastreio e aprendizagem, os marcos de aplicação da alteração ao AI Act e a distinção entre estimativa histórica e projeção no relatório energético. [Fontes e passagens](V3_FONTES_E_EVIDENCIAS.md)
- **Ensaio.** Dez verificações numa troca local A2A e MCP, incluindo retoma da mesma tarefa e recusa por identidade. [Comando e resultado](../experiencias/interoperabilidade/README.md)
- **Retoma.** O checkpoint K fechou a edição e os percursos editoriais. A avaliação independente e o piloto com LLM têm registos próprios. [Ancoragem](V3_ANCORAGEM.md)

## Checkpoint I — fecho editorial e consulta

Os 17 capítulos em falta foram revistos em três lotes. O [registo de retoma](V3_ANCORAGEM.md) identifica os ficheiros e a [validação](V3_VALIDACAO.md) descreve os resultados. A passagem editorial abrange agora os 50 capítulos. A edição conserva 74 laboratórios, tem 93 referências compostas e ganhou um guia de consulta de uma página.

- **Entrada.** O leitor pode escolher uma tarefa, começar por um exercício acessível e seguir as remissões quando precisar do mecanismo. Há caminhos para escrever e aprender, criar sem código, compreender modelos, construir e operar.
- **Verificação.** As consultas SQL e a função Python foram executadas. A Lavandaria demonstrou a diferença entre conhecer um identificador e ter autorização. As três abordagens do laboratório comparativo tiveram 2 acertos em 4, com diferentes chamadas de componentes e zero chamadas a um LLM.
- **Fontes.** Foram acrescentadas três referências e conferidas as afirmações revistas nos trechos indicados no [registo](V3_FONTES_E_EVIDENCIAS.md). A revisão delimita o alcance dos estudos e identifica os exemplos de ficção e os cálculos construídos.

A [matriz](V3_MATRIZ_COBERTURA.md) separa as prioridades de validação e aprofundamento. O bloco seguinte foi executado em J e o piloto de equipa conservou a dependência de um GGUF íntegro.

## Checkpoint H — projeto criativo, caso público e operação

O manuscrito está em desenvolvimento. Tem 50 capítulos em dez partes, três apêndices, 74 laboratórios, 90 referências e 58 termos. Os 76 testes passaram. A prova e o âmbito da inspeção estão em [V3_VALIDACAO.md](V3_VALIDACAO.md).

- **Projeto criativo.** Produzidos a ilustração, o cartaz editável, o guião visual e a curta muda de quinze segundos de [A Meia Testemunha](../exemplos/atelier/README.md). Os ficheiros incluem o pedido de imagem, os enquadramentos, as exportações e as verificações.
- **Serviço público.** Acrescentado o caso SyRI com os parágrafos da decisão e distinção entre relatório de risco, investigação e sanção. O [registo de fontes](V3_FONTES_E_EVIDENCIAS.md) guarda o alcance da leitura.
- **Operação.** Executado o [incidente da cache](../experiencias/operacao/README.md). A resposta desatualizada passa a forma, é encaminhada sem prazo e a versão vigente é recuperada. Seis testes acrescentados.
- **Progressão.** Revistos A, C, E e dois capítulos de B, 17 dos 34 que estavam por rever. Foram reduzidas repetições e acrescentados exemplos que se podem verificar. Faltam 17 capítulos em B, D e F.

A [ancoragem](V3_ANCORAGEM.md) identifica os commits, os ficheiros e as dependências. O checkpoint I retomou em `src/capitulos/12-escrita.tex` e fechou os três lotes pendentes.

## Checkpoint G — progressão, narrativa e aprofundamento

A retoma de 05-11-2026 tem a sua base, divisão de trabalho e registo em [V3_ANCORAGEM.md](V3_ANCORAGEM.md). Os resultados do checkpoint G abaixo são a base validada dessa retoma.

O autor autorizou continuar em 04-11-2026, com progressão do básico à especialização, rigor factual, humor e leitura envolvente. Base da retoma confirmada `e990b891`; `main` continua em `975ade8`. A orientação encontra-se em `V3_LINHA_NARRATIVA.md` e não envolve imitação de personagens, enredos ou prosa de outros autores.

Concluído neste ciclo:

- Revistos os ficheiros 01, 07, 30–33, 38–39, 41–47 e 49: 16 capítulos. Aberturas e transições aproximam problema, mecanismo, experiência e consequência. Há percursos de intuição e aprofundamentos opcionais, sem pressupor que o leitor já domina a notação.
- A Lavandaria ganhou uma investigação recorrente sobre informação ausente e custo de revisão. História, saúde, persuasão, aprendizagem e energia usam entradas diferentes. Ficção, exemplos sintéticos e estudos publicados estão identificados; a curiosidade narrativa não altera o alcance das conclusões.
- Corrigida a promessa errada de que a primeira conversa surgia logo após o primeiro capítulo. Clarificadas transformações afins, máscaras causais, multicabeça, alinhamento e as diferenças entre métricas condicionais e consequências.
- Desenvolvidos os cinco capítulos de sociedade com estudos e decisões: PRAIM, proxy de custos em saúde, generalização de imagens agrícolas, inspeção industrial, persuasão, tutor de física e contabilização de recursos. As 14 fontes adicionais e os limites de consulta estão no registo; a bibliografia composta tem 87 entradas.
- Executados novos exemplos de XOR e reforço, contas de decisão, produtividade e energia, e treino de um adaptador linear de posto um. Dados, configuração, resultado e hash do código do treino estão em `experiencias/adaptacao_linear`. O exemplo distingue um alvo representável de outro cujo mínimo de perda é 0,25. Não é treino de LLM.
- **70 testes passaram**, mais 18 que no ciclo anterior. Compilação, estrutura, remissões, citações e sintaxe Python passaram. A composição final e a inspeção visual estão descritas em `V3_VALIDACAO.md`.

O piloto de equipa com LLM continua bloqueado. A nova tentativa de ligação ao modelo oficial terminou por timeout, sem bytes recebidos. Não foram executados participantes humanos, produção multimédia ou fine-tuning de LLM. O adaptador linear não preenche essas linhas de resultado.

### Próximo passo registado no fim do segundo ciclo

1. Confirmar o HEAD, ler este checkpoint e continuar na mesma branch e no PR #2. Não recomeçar a auditoria nem reescrever os 21 capítulos novos como se estivessem ausentes.
2. Desenvolver e executar um projeto criativo completo da Parte IV, com materiais próprios ou autorizados, caminho sem código, ficheiros finais e critérios de continuidade, legibilidade e direitos. Integrar resultados observados e manter os restantes projetos como propostas até à execução.
3. Acrescentar um caso empírico pormenorizado de justiça/serviço público com fonte primária e um caso de operação/incidente. A discussão normativa e as contas sintéticas atuais não são estudos desses serviços.
4. Prosseguir a revisão de progressão e estilo nos restantes capítulos, por conjuntos coerentes, sem transformar cada abertura num diálogo ou cada fecho numa promessa. Submeter percursos de leitura a leitores quando houver participantes reais.
5. Se houver uma cópia íntegra do modelo, confirmar hash e runtime e executar o piloto fechado numa pasta nova. Se o bloqueio persistir, conservar esse estado e continuar o trabalho editorial independente dele. Não substituir o ensaio por um stub.
6. Reavaliar profundidade, evidência e critérios de aceitação antes de retirar o estado de desenvolvimento. Título comercial, revisão humana, publicação e merge continuam reservados ao autor.

## Histórico do primeiro ciclo

As secções A–F abaixo preservam o diagnóstico e a primeira entrega. Os seus valores de 268 páginas, 73 referências e 52 testes são históricos e foram superados pelo checkpoint G.

## Checkpoint A — diagnóstico e arquitetura

- Concluído: estado real do GitHub, PR #1 integrado, inexistência inicial da branch V3, criação da branch a partir de `975ade8`.
- Concluído: cópia local com a mesma árvore Git da base; leitura integral dos 29 capítulos e três apêndices; inspeção de bibliografia, validação estática, workflow e demonstração.
- Concluído: 30 testes existentes executados; 29 capítulos, 47 laboratórios e 41 referências verificados; integridade dos 52 registos reais de 03-11-2026 reavaliada, sem nova inferência.
- Concluído: matriz de cobertura e arquitetura em dez partes; três títulos com recomendação provisória.
- Este checkpoint inicial está preservado como diagnóstico. A produção posterior está registada abaixo; o antigo próximo passo já foi executado.

## Checkpoint B — arquitetura integrada

Concluídos o mapa de migração, a sequência em dez partes e a integração em `src/livro.tex`. Os nomes dos ficheiros conservam os identificadores históricos; não correspondem à numeração impressa. `V3_ESTRUTURA.json` verifica a ordem exata dos 50 capítulos e dos três apêndices. O percurso de leitura permite chegar às primeiras aplicações sem exigir a leitura prévia da matemática.

## Checkpoint C — produção e revisão

| Área | Produzido e integrado | Profundidade ainda por completar |
|---|---|---|
| I. Revolução | História, definições operacionais, ANI/AGI/ASI e limites de demonstrações; ficheiros 01 e 30 | Ampliar os ciclos históricos com casos documentados e revisão especializada |
| II. Máquina | ML, generalização, RL, arquiteturas generativas; cálculos de regressão, atenção e memória; revisão de 06–09 | Exercícios mais desenvolvidos de redes, otimização, avaliação fora da distribuição e multimodalidade |
| III. Conversar | Revisão dos fundamentos de prompts e raciocínio; contexto, memória e compressão; geração estruturada | Ensaios de seleção/compressão de contexto com modelos e diferentes tarefas |
| IV. Criar | Aplicações existentes revistas; novos projetos de imagem, audiovisual, música, voz, jogos e atividades sem código | Executar os projetos multimédia, guardar resultados autorizados e validar instruções com leitores não técnicos |
| V. Construir | Skills, pacote demonstrativo, supervisor, paralelismo, contratos, falhas e A2A; segurança e limites | Validar ativação numa aplicação de agentes e implementar uma integração MCP/A2A real, se mantida no âmbito dos laboratórios |
| VI. Adaptar | Fine-tuning, LoRA, QLoRA, distilação, quantização e estimativa de memória | Um treino real documentado e medições comparáveis de execução local; não realizados nesta sessão |
| VII. Operar | Núcleo de avaliação, autorização, segurança, observabilidade e governação preservado e complementado | Ensaio integrado de incidente e recuperação de equipa com modelo real |
| VIII. Sociedade | Cinco capítulos com estudos, métodos, populações, resultados e limites; trabalho, ciência, poder, relações e energia | Aprofundar educação, biotecnologia, agricultura, indústria, justiça e serviços públicos com casos próprios e mais fontes primárias |
| IX. Futuro | Modelos do mundo, robótica, consciência e cenários com evidência contrária; revisão do percurso profissional | Revisão científica independente e maior desenvolvimento dos paradigmas alternativos e consequências económicas |
| X. Laboratório | Seis projetos integrados, comparação offline executada e protocolo humano/IA separado das medições | Piloto com LLM bloqueado; estudo com participantes e restantes projetos não executados |

Foram corrigidas generalizações sobre recência de contexto, few-shot, unimodalidade, RLHF, alinhamento, criatividade e aprendizagem. A revisão distingue estilos de raciocínio de acesso a processos internos e separa resultados de estudos de recomendações. O glossário foi ampliado, ordenado e harmonizado. Fontes e alcance da consulta constam de `V3_FONTES_E_EVIDENCIAS.md`.

## Checkpoint D — exemplos executados e limites

- Executados: fundamentos matemáticos e estimativas; validador de pacote de skill e fichas; controlador com orçamento, dois especialistas paralelos e síntese; testes de falhas parciais e contratos. Os novos módulos acrescentam 22 testes aos 30 existentes: **52 passaram**.
- Executados: 12 regressões da Lavandaria; revalidação da integridade dos 52 registos reais históricos; ensaio determinístico novo em quatro casos e três modos. No ensaio novo, cada modo acerta dois de quatro; fluxo e único gastam quatro chamadas de componentes, equipa gasta doze, **zero chamadas LLM**. Isto não é um benchmark de inteligência ou uma comparação humana.
- Implementado, mas bloqueado antes da primeira inferência: piloto local novo com 32 chamadas de modelo planeadas. O runtime recusou a cópia incompleta do modelo; a tentativa de obter outra cópia falhou por ligação indisponível. Tamanho, hashes, erro e protocolo estão em `experiencias/equipas/README.md`. Nenhum resultado foi preenchido por simulação.
- Propostos, sem alegação de execução: treino LoRA/QLoRA, estudo com pessoas, produção multimédia e instalação/ativação real da skill. Os exemplos offline não precisam de API paga.

## Checkpoints E e F — integração e primeira entrega de trabalho

Compilação LaTeX/BibTeX, validação estrutural, citações, referências cruzadas e verificações do log passaram. Inspeção das 268 páginas em quatro folhas de contacto, revisão ampliada de 20 páginas e verificação geométrica de todos os blocos de texto não identificaram cortes ou extravasamentos. Não substituem revisão científica ou leitura editorial integral da edição composta.

O GitHub Actions passou no push e no PR para a revisão de conteúdo `29364b6558ce40426f5e682058ad97f698bc40b7`: [execução do PR](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41922570704), [execução do push](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41922563663). A atualização final de documentação volta a acionar a CI; o estado do HEAD está no PR.

O PR continua Draft porque a cobertura inicial de todas as áreas não demonstra profundidade final. `main@975ade8`, a licença, a capa e os resultados históricos foram preservados. Não foi feito merge, tag, release ou publicação.

## Commits persistentes de produção

SHAs abaixo são do GitHub, não da cópia local usada para preparar as alterações.

| Commit | Conteúdo |
|---|---|
| `b737f239` | Auditoria dos 29 capítulos, matriz, plano e checkpoint inicial |
| `be8e1f50` | Fundamentos e criação; cálculos e testes |
| `8175b32e` | Pacote de skill e controlador de equipa com testes |
| `cc9baa4a` | Capítulos de skills, multiagentes e interoperabilidade |
| `a23420da` | Adaptação e execução local |
| `1c2bf631` | Sociedade, evidência de impacto e cenários |
| `deed918a` | Integração em dez partes, revisão de capítulos, 73 labs e CI |
| `29364b65` | Correções tipográficas após composição |
| `e990b891` | Checkpoint da primeira entrega, fontes e pendências |
| `7bf38ddb` | Contas de XOR, reforço, decisão e custos com testes |
| `9c48cbbd` | Progressão narrativa, fundamentos e fontes adicionais |
| `ddea97f6` | Aprofundamento de trabalho, ciência, informação, relações e energia |
| `5d4ec49b` | Treino linear de baixo posto e resultado reproduzível |
| `2e0a2e26` | Pontes da intuição à especialização e laboratório integrado |

O checkpoint final de documentação sucede a estes commits; o SHA pode ser obtido no HEAD da branch e na folha de rosto do PDF correspondente.

## Próximo passo registado no primeiro ciclo

1. Verificar o HEAD e este checkpoint; continuar nesta branch e neste PR. Não reproduzir a auditoria nem reescrever os 21 capítulos como se não existissem.
2. Obter uma cópia íntegra do modelo indicado, confirmar o SHA-256 e a revisão do runtime, iniciar o servidor local e executar o piloto descrito em `experiencias/equipas/README.md` numa pasta nova. Se continuar bloqueado, conservar esse estado; não substituir inferências por stubs.
3. Registar pedidos, respostas, tokens disponíveis, tempos e falhas; validar o manifesto. Só então atualizar o capítulo de comparação com resultados efetivamente observados e limites da pequena amostra.
4. Aprofundar prioritariamente os cinco capítulos da Parte VIII: cada setor precisa de problema, mecanismo, estudo primário, efeitos demonstrados, limitações e caso de decisão. Expandir depois os exercícios de fundamentos, adaptação e criação de acordo com a tabela anterior.
5. Executar os projetos criativos e o treino que forem mantidos como demonstrações da edição final; para a comparação humana, definir protocolo, consentimento, participantes e avaliação antes de recolher dados. Não bloquear a investigação editorial independente destes ensaios.
6. Reavaliar a matriz, a progressão e os critérios de aceitação do pedido. Só quando a profundidade e a evidência forem adequadas se poderá retirar o estado de desenvolvimento; manter o PR Draft até essa decisão explícita.

## Regras para retoma

Ler este ficheiro, `V3_VALIDACAO.md` e o histórico da branch no GitHub. Confrontar o HEAD remoto com o último checkpoint. Não recriar branch nem repetir a segunda edição. Não fazer merge. Não confundir itens previstos com capítulos produzidos.

## Decisões reservadas ao autor

Título comercial definitivo; revisão independente; suficiência da profundidade e da extensão; capa final; publicação e merge. Nenhuma dessas decisões é implicitamente aprovada por um build verde.
