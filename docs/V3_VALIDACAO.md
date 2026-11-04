# Validação da terceira edição

Data: 04-11-2026. Este ficheiro distingue a base existente das alterações V3.

## Base, antes de alterações ao manuscrito

| Verificação executada | Resultado |
|---|---|
| Árvore local vs `main@975ade8` | `13de7f25f76d803ed5f68878b6cab804727fd985`, idêntica |
| `python3 -m unittest discover -s tests -v` | 30 testes passaram |
| `python3 scripts/verificar_livro.py` | 29 capítulos, 47 laboratórios, 41 referências, zero erros |
| `python3 experiencias/llm_local/verificar_registo.py` | 52 registos, hashes e métricas consistentes |

Não foi necessária nova execução das 52 inferências históricas. A segunda edição tem evidência de CI no PR #1; essa evidência não valida alterações V3 ainda não produzidas.

## V3 — verificação executada

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
