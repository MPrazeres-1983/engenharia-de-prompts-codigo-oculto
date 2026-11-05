# Validação da terceira edição

Atualização de 05-11-2026. O [registo de retoma](V3_ANCORAGEM.md) liga as verificações aos blocos e aos commits.

## Checkpoint J — entrada acessível, ensaios e fontes

| Verificação | Resultado observado |
|---|---|
| Compilação | 267 páginas físicas A4 na prova local. Dez partes, 50 capítulos, três apêndices, 74 laboratórios, 93 referências compostas e 70 entradas de glossário. Verificador de estrutura e log sem erros |
| Consulta | 23 remissões no guia. A nova abre o ponto de partida, nas páginas físicas 5 e 6 |
| Aritmética | 14 verificações de cálculo, com proporções, médias, matriz por vetor, atenção, perda e inclinações, temperatura, retorno, ruído, métricas e memória |
| Regressão | 76 testes Python, 12 regressões da Lavandaria, verificação de integridade e métricas dos 52 registos históricos e `compileall` passaram |
| Interoperabilidade | Dez verificações locais em duas execuções com o mesmo resumo. Descoberta, versão, autorização, retoma e artefacto. Zero chamadas a um LLM. [Registo e código](../experiencias/interoperabilidade/README.md) |
| Composição | Geometria verificada em todas as páginas. Inspeção do ponto de partida e de amostras das contas, das tabelas, dos dados setoriais e do comando de interoperabilidade |

O resultado do ensaio de protocolos é observável neste ambiente. As passagens de estudos, normas e relatórios foram confrontadas com os localizadores no [registo de fontes](V3_FONTES_E_EVIDENCIAS.md). O piloto com modelo local continua bloqueado antes da inferência. A leitura independente é a próxima forma de verificar se as explicações chegam ao leitor sem ajuda.

### Percursos para a leitura independente

| Percurso | Tarefa a entregar ao leitor | Evidência a recolher |
|---|---|---|
| Primeiro contacto | A partir do guia, encontrar a diferença entre 10 pontos percentuais e um aumento de 50%. Depois explicar o que significa dar mais peso ao valor 6 na conta simples de atenção | Página encontrada, conta ou explicação e primeiro termo que exigiu ajuda |
| Aplicação sem código | Seguir a passagem do grande laboratório que propõe quatro mensagens. Dizer o que fazer quando falta o número de reclamação | Resposta esperada e trecho em que a regra ficou clara ou ambígua |
| Experiência técnica | Encontrar o comando da receção e do arquivo, reproduzir o ensaio e explicar por que razão uma resposta 200 pode conter uma tarefa ainda em aberto | Resultado observado, versão, ambiente e ponto de fricção |

Regista as respostas dadas espontaneamente antes de explicar. Distingue dificuldade de encontrar a passagem, de compreender o termo e de executar a tarefa. Esta tabela é o protocolo de leitura. As verificações acima são editoriais e técnicas.

## Checkpoint I — fecho editorial e guia de consulta

| Verificação | Resultado observado |
|---|---|
| Compilação e estrutura | 264 páginas físicas A4 na prova local. Dez partes, 50 capítulos, três apêndices, 74 laboratórios, 93 entradas bibliográficas compostas e 58 termos. Quatro exemplos JSON e zero erros do verificador de estrutura e log |
| Navegação | 22 remissões clicáveis do guia conferidas no PDF. Cada uma abre o capítulo ou apêndice indicado |
| Regressão | 76 testes Python passaram, 12 de 12 regressões offline da Lavandaria passaram, `compileall` passou. Integridade e métricas dos 52 registos históricos reconferidas |
| Exemplos novos | SQLite 3.53.1 devolveu `(3,90,30)` com a junção e `(2,60)` com `EXISTS`. O caso adicional sem artigos e as quatro verificações da média em Python passaram |
| Comparação offline | Os três modos repetiram os mesmos dois acertos em quatro casos, com 4, 4 e 12 chamadas de componentes. Zero chamadas ao modelo |
| Inspeção tipográfica | Geometria conferida nas 264 páginas. Amostra do guia, dos três lotes, das tabelas e do código. Corrigidas duas páginas com linhas de fim de capítulo isoladas e reunidas as linhas de cada consulta SQL e do JSON do capítulo de dados |

O [registo de fontes](V3_FONTES_E_EVIDENCIAS.md) indica as passagens verificadas e o alcance da consulta. A validação dos capítulos de protocolos verificou a documentação e os exemplos offline. A interoperabilidade ponta a ponta, a adaptação de um LLM, o piloto de equipa com modelo e a leitura independente têm validações próprias pendentes. O [PR #2](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/2) liga a revisão exata e as verificações da CI.

## Checkpoint H — terceira retoma

| Verificação | Resultado observado |
|---|---|
| Compilação LaTeX e BibTeX | 292 páginas físicas A4 com pdfTeX 1.40.25 e padrões portugueses de hifenização |
| Estrutura e composição | Dez partes, 50 capítulos, 74 laboratórios, três apêndices, 90 entradas bibliográficas compostas e 58 entradas de glossário. Verificador de referências, JSON e log sem erros |
| Testes Python | 76 passaram, incluindo seis novos testes de operação. `compileall` passou |
| Lavandaria | 12 de 12 regressões offline passaram |
| Ensaio de cache | Execução atual igual ao registo versionado. Proposta v1 encaminhada sob v2 vigente e resposta de cinco dias úteis recuperada |
| Ateliê | Quatro entradas e três saídas conferidas pelos hashes. Exportações de uma página A4 e vídeo mudo H.264 de 15 s, 24 fps e 360 fotogramas. Revistos cartaz, guião e fotogramas de início e fim de cada plano |
| Registos históricos | 52 inferências reconferidas quanto a integridade e métricas. O piloto novo tem zero chamadas |
| Inspeção visual | Folhas de contacto, localização dos materiais novos e revisão ampliada de páginas selecionadas. Verificação geométrica sem blocos de texto fora das páginas |

A prova ampliada está indexada pelas páginas físicas 1, 2, 3, 39, 49, 76, 81, 102, 155, 156, 213, 218, 226, 227, 246, 291. A inspeção encontrou espaçamento irregular no primeiro guião, corrigido com fontes incorporadas, e problemas de composição na nota e no laboratório de cache. A nota cabe numa página, o laboratório ficou reunido e o comando pode ser copiado numa linha.

A primeira compilação local parou porque faltava a definição portuguesa do Babel. A configuração passou a importar o locale incluído. Para a prova final, a compilação local usou um formato pdfLaTeX privado com os padrões portugueses oficiais, confirmados por hash antes de gerar o formato. [Padrões 1.4](https://github.com/hyphenation/tex-hyphen/blob/master/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-pt.tex) e [carregador](https://github.com/hyphenation/tex-hyphen/blob/master/hyph-utf8/tex/generic/hyph-utf8/loadhyph/loadhyph-pt.tex).

A inspeção tipográfica e os testes cobrem a composição e os exemplos descritos. A leitura integral, a validação independente e o piloto com LLM permanecem na ordem de retoma. A folha de rosto identifica a revisão do PDF. O [PR #2](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/2) liga as execuções da CI do HEAD.

## Checkpoint G — segundo ciclo, progressão e narrativa

Retoma verificada a partir de `e990b891`. Foram revistos 16 capítulos e a nota editorial, com novos casos, mecanismos e aprofundamentos. A estrutura mantém dez partes, 50 capítulos, três apêndices e 73 laboratórios. **A composição desse checkpoint tinha 299 páginas e 87 entradas bibliográficas. Os 70 testes passaram.** O trabalho continua Draft e não está aprovado para publicação ou merge.

| Verificação executada neste ciclo | Resultado |
|---|---|
| Compilação LaTeX/BibTeX | 299 páginas; recompilação limpa bem-sucedida |
| Estrutura e log | 50 capítulos, 73 labs, 87 referências, quatro JSON de exemplos; zero erros do verificador |
| `unittest discover` | 70 passaram: 30 de Lavandaria, 12 de fundamentos, seis de skills, oito de equipa, nove de decisão e cinco de adaptação |
| `compileall` | Passou para exemplos, scripts, testes e experiências |
| XOR, retorno e Q | Tabela e contas executadas; não se declarou treino de uma política RL |
| Decisão, tempo e energia | Frações e unidades conferidas em cenários sintéticos; sem dados clínicos ou telemetria elétrica |
| Adaptador linear | Base 2×2 preservada; gradientes conferidos por diferenças finitas; alvo representável com MSE abaixo de 1e-12 |
| Limite de capacidade | No segundo alvo, perda de 0,5 para 0,25, compatível com limite demonstrado para o conjunto construído |
| Resultado da adaptação | Dados, configuração e pesos guardados; SHA-256 do código conferido com o ficheiro executado |
| Bibliografia composta e glossário | 87 `bibitem` e 58 entradas de glossário |

O resultado do adaptador está em `experiencias/adaptacao_linear/resultado-2026-11-04.json`; requisitos e limites no README adjacente. É treino de fatores de uma transformação linear, não LoRA/QLoRA de um LLM. Os três casos reservados são construídos a partir de uma relação exatamente representável, sem pretensão de validade externa.

### Inspeção visual e falha incremental resolvida

As 299 páginas foram inspecionadas em cinco folhas de contacto e verificadas geometricamente, sem blocos de texto fora da página. Foram também vistas ampliadas 23 páginas físicas: 2, 3, 15, 20, 21, 26, 30, 41, 42, 199, 201, 202, 205, 238, 244, 245, 247, 252, 253, 258, 259, 262 e 295. A amostra inclui aberturas, máscara e softmax, XOR, LoRA e prova de limite, tabelas de prevalência/aprendizagem, memória, energia e referências. Não foram identificados cortes, sobreposições ou fórmulas/tabelas ilegíveis. O texto das páginas alteradas na última revisão tipográfica foi novamente visto.

Uma compilação incremental local falhou ao ler um `.aux` com 4096 bytes, terminado a meio de `\\@writefile`. A origem do truncamento não foi determinada. A limpeza dos ficheiros gerados com `latexmk -c -cd src/livro.tex`, seguida de recompilação, produziu o PDF completo; o `.aux` final tem 87775 bytes e termina com o total de páginas. O verificador do log passou depois da recuperação. Não foi necessário retirar conteúdo ou contornar uma validação.

Esta inspeção é tipográfica e amostral; não demonstra prazer de leitura ou substitui revisão científica/editorial integral. Os casos ficcionais e os cálculos próprios foram separados dos resultados publicados. As 14 fontes adicionadas têm o alcance registado, sem alegação de leitura integral de todos os estudos.

### CI e bloqueios atuais

Na revisão de conteúdo `2e0a2e26983d658fb97c013e310aacf80a11a2c1`, passaram [o push 41930823603](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41930823603) e [o PR 41930831649](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41930831649). O checkpoint final acrescenta documentação, clarificação de proveniência na nota e agrupamento tipográfico de números; aciona nova CI, cujo estado do HEAD fica no PR. O workflow executa também `decisoes` e `adaptacao` e guarda as saídas nos artefactos.

O novo piloto LLM continua com zero inferências: a segunda tentativa de ligação ao modelo oficial terminou em timeout sem bytes recebidos. Os 52 registos reais históricos permanecem separados e íntegros. Não há estudo com participantes, treino de LLM, medição de hardware ou produção multimédia novos para apresentar como concluídos. O treino linear e os 70 testes não preenchem essas lacunas.

## Histórico da primeira entrega V3

As verificações seguintes conservam a base e o primeiro ciclo: os seus números de páginas, referências e testes são históricos. Os checkpoints posteriores estão acima.

## Base, antes de alterações ao manuscrito

| Verificação executada | Resultado |
|---|---|
| Árvore local vs `main@975ade8` | `13de7f25f76d803ed5f68878b6cab804727fd985`, idêntica |
| `python3 -m unittest discover -s tests -v` | 30 testes passaram |
| `python3 scripts/verificar_livro.py` | 29 capítulos, 47 laboratórios, 41 referências, zero erros |
| `python3 experiencias/llm_local/verificar_registo.py` | 52 registos, hashes e métricas consistentes |

Não foi necessária nova execução das 52 inferências históricas. A segunda edição tem evidência de CI no PR #1; essa evidência não valida alterações V3 ainda não produzidas.

## Primeiro ciclo V3 — verificação executada

Revisão de conteúdo no GitHub: `29364b6558ce40426f5e682058ad97f698bc40b7`. A atualização posterior de README e checkpoints não altera o manuscrito ou o código. O PDF identifica a revisão da branch usada para o compor; na CI o checkout e a identificação usam o HEAD real do PR, não o commit de merge sintético do GitHub.

| Verificação | Resultado observado |
|---|---|
| `latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -file-line-error src/livro.tex` | PDF composto com pdfLaTeX/BibTeX: 268 páginas físicas |
| `python3 scripts/verificar_livro.py --log src/livro.log` | Dez partes, 50 capítulos, três apêndices, 73 labs, 73 referências e quatro JSON; zero erros |
| `python3 -m unittest discover -s tests -v` | 52 testes passaram: 30 herdados, oito de fundamentos, seis de skill e oito de equipa |
| `python3 -m exemplos.lavandaria.avaliar` | 12 de 12 casos de regressão passaram; software determinístico, sem LLM |
| `python3 experiencias/llm_local/verificar_registo.py` | 52 inferências históricas com hashes e métricas consistentes; não repetidas |
| `python3 -m exemplos.laboratorio.fundamentos` | Regressão, atenção, quantização didática e estimativa de memória executadas |
| `python3 -m exemplos.laboratorio.skills` | Pacote e ficha demonstrativa estruturalmente válidos; integridade dos recursos confirmada |
| `python3 -m exemplos.laboratorio.equipas` | Três modos executados com stub; contratos, chamadas e encaminhamento verificáveis |
| `python3 experiencias/equipas/offline.py --verificar` | Registo reproduzido: quatro casos × três modos, dois acertos por modo, zero inferências LLM |
| `python3 -m compileall -q exemplos scripts tests experiencias` | Passou localmente e na CI |
| Glossário | 58 entradas, revista a terminologia e a ordenação |

O controlo do log rejeita, entre outros, referências/citações indefinidas, labels duplicados, overfulls, caracteres em falta e erros de compilação. Os underfulls residuais não impedem a composição; os pontos visuais relevantes foram inspecionados. A instalação local precisou de completar o suporte de português do TeX Live porque o pacote em cache estava incompleto; nenhuma dependência foi substituída por comandos no manuscrito. A CI compila separadamente com a distribuição do `latex-action`.

## Inspeção do PDF

As 268 páginas foram vistas em quatro folhas de contacto. Vinte páginas foram também inspecionadas em tamanho ampliado: 2, 3, 22, 23, 25, 173, 176, 177, 186, 187, 189, 222, 223, 238, 240, 244, 247, 249, 258 e 263 (posição física no PDF). A amostra cobre folha de rosto, nota editorial, equações, tabelas, diagrama de equipa, laboratório, glossário e bibliografia. Não foram identificados cortes, sobreposição de elementos ou tabelas ilegíveis nessa inspeção.

Foi ainda verificada a caixa de todos os blocos de texto do PDF, sem blocos fora da página. Esse controlo geométrico não deteta todos os problemas de leitura. A leitura científica/editorial integral da versão composta continua necessária; inspecionar miniaturas não equivale a ler todos os parágrafos.

## GitHub Actions

| Evento / revisão | Execução | Resultado |
|---|---|---|
| PR #2 / `29364b65` | [41922570704](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41922570704) | `completed / success` |
| Push / `29364b65` | [41922563663](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41922563663) | `completed / success` |

No job do PR foram confirmados o sucesso dos exemplos offline, da compilação, da validação do log e do upload de artefactos. Os artefactos incluem PDF, log, BBL, revisão, saídas dos verificadores e resultados históricos. O checkpoint final de documentação aciona novas execuções, cujo estado fica visível no PR e no histórico de Actions. Uma execução anterior cancelada por um commit mais recente não é apresentada como falha de conteúdo.

## Ensaio com modelo novo: bloqueio antes da inferência

O protocolo do piloto define quatro casos e duas seeds; agente único faz uma chamada por caso/seed e equipa faz três: 32 chamadas planeadas. **Zero chamadas executadas nesta sessão.** O ficheiro GGUF disponível tem 255381504 bytes, SHA-256 `7e5fb2f526ad52876a3417b1f61931ee6405aab6deea974777c84b8f5311b62d`, diferente do SHA-256 de referência `74a4da8c9fdbcd15bd1f6d01d621410d31c6fc00986f5eb687824e7b93d7a9db`. O runtime recusou o tensor `blk.1.ffn_down.weight` fora dos limites do ficheiro. A tentativa de ligação à distribuição oficial falhou por timeout do proxy.

O runner recusa hashes incorretos e pastas de resultados já preenchidas. Não foi removida essa verificação para produzir números. O registo histórico da segunda edição mantém-se íntegro; o estado atual de uma cópia local do modelo não prova um problema nas inferências históricas já guardadas.

## Limites da evidência

O ensaio offline novo usa o mesmo stub nos papéis e não mede qualidade de modelos, tempos de utilizadores ou vantagem de multiagentes. O controlador é pedagógico, não implementação MCP/A2A ou servidor de produção. O validador da skill aceita um subconjunto declarado do frontmatter; não é um parser YAML universal, verificador de verdade ou prova de ativação num agente. A memória calculada não inclui todos os buffers, overheads ou comportamento de um runtime real.

Não foram executados treino LoRA/QLoRA, projetos multimédia ou estudo com participantes. As leituras de fontes e os estudos publicados têm o alcance declarado em `V3_FONTES_E_EVIDENCIAS.md`; não se alegam reprodução experimental ou revisão integral de todos os artigos. Não existem resultados simulados apresentados como medições.

## Critérios editoriais de aceitação

As dez áreas precisam de conteúdo real, progressão, exemplos e fontes. A matriz inicial identifica lacunas; a matriz final deve indicar o que foi efetivamente resolvido e o que precisa de aprofundamento. O manuscrito só se declara pronto para revisão integral quando essas condições forem confrontadas com o texto produzido. A revisão humana e a decisão de publicação mantêm-se separadas da verificação automatizada.
