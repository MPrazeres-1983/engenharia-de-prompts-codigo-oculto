# Ancoragem e retoma da terceira edição

Retoma de 5 de novembro de 2026. O autor pediu um ponto de situação e trabalho dividido em blocos, com informação suficiente para retomar cada um. O registo de execução abaixo é o primeiro sítio a consultar antes de escrever, alterar ou testar.

## Base confirmada

| Elemento | Evidência |
|---|---|
| Branch | `terceira-edicao-ia-referencia-2026` |
| Última revisão validada antes da retoma | `4b6a9480fae2c73fbc5e4e2aa629dc94924fa04b` |
| Árvore local e remota nessa revisão | `e26f1a84598bbbcedc9f3d568c654c8043dda19c` |
| Revisão da base `main` | `975ade89632700918786603dc23722e74f8610f7` |
| Entrega | [PR #2 aberto em Draft](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/2), 15 commits antes da retoma |
| Manuscrito e verificação anterior | 299 páginas, dez partes, 50 capítulos, 73 laboratórios, 87 referências, 58 termos e 70 testes aprovados |
| CI anterior | [Push 41932168522](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41932168522) e [PR 41932176820](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41932176820), sucesso |
| PDF recebido nesta retoma | 299 páginas, revisão `4b6a9480` na folha de rosto. Texto extraído e dimensões coincidem nas 299 páginas com a saída local do checkpoint G |

SHA-256 do PDF recebido `c74ef5680dfcd2f2bf0e7c15e798bef5846cd3c59f2c17d10fa01a070161f5a4`. SHA-256 da saída local anterior `04726d7e5379b3c20524e0f3812751993c35836158b3d5f54686b8b9a490135b`. Os dois hashes identificam ficheiros diferentes. A comparação acima é de conteúdo textual e dimensões.

O plano, a matriz, a linha narrativa, as fontes e a validação dos ciclos anteriores continuam em `docs/`. O checkpoint G documenta os 16 capítulos revistos no segundo ciclo. A obra mantém o título provisório, a autoria e a licença do projeto. A decisão de publicação e o merge dependem do autor.

## Blocos de execução

| Bloco | Estado inicial | Entrega concreta | Evidência para fechar |
|---|---|---|---|
| H0. Ancoragem | Base conferida | Este registo, referência ao PDF e dependências | Commit na branch e PR identificável |
| H1. Projeto criativo | Em curso, conceito e ambiente avaliados | Cena original da Lavandaria, ilustração, cartaz editável, guião visual e curta de quinze segundos | Ficheiros exportados, origem e condições de uso, verificação de duração, legibilidade e continuidade |
| H2. Serviço público | Fontes oficiais identificadas | Caso SyRI com finalidade, dados, intervenção, decisão judicial e limites, separado de exercícios fictícios | Localizadores no acórdão e na fonte institucional, referências e redação conferidas |
| H3. Incidente | Hipótese de reprodução definida | Exercício local de cache com política desatualizada, deteção, encaminhamento e recuperação | Registo executado, teste de regressão e critérios de recuperação |
| H4. Progressão e estilo | 34 capítulos fora da revisão narrativa do ciclo G | Revisão por lotes abaixo, com ligação a H1–H3 quando pertinente | Capítulos revistos e alterações verificáveis por lote |
| H5. Integração | Pendente | Manuscrito e PDF com a revisão composta | Compilação limpa, testes aplicáveis, amostra visual, CI do HEAD e PR atualizado |

## Lotes de revisão

Os números são prefixos dos ficheiros, de acordo com `V3_ESTRUTURA.json`. A revisão mede clareza, progressão, consistência e suporte factual. Os lotes dão uma ordem de trabalho e deixam visível o que falta em cada retoma.

| Lote | Ficheiros | Foco |
|---|---|---|
| A | 02, 03, 04, 05, 10, 11, 17, 34 | Conversa, especificação, contexto e revisão |
| B | 12, 13, 14, 15, 16, 18, 19, 35, 36, 37 | Escrita, aprendizagem, criação e prática. Integra H1 |
| C | 06, 08, 09 | Mecanismo, unidades e modalidades |
| D | 20, 21, 22, 23, 24, 40 | Construção, fontes, autoridade e interoperabilidade |
| E | 25, 26, 27, 28 | Avaliação, segurança e operação. Integra H3 |
| F | 29, 48, 50 | Futuros e comparação, com medidas e limites explícitos |

## Regras de registo

- Cada bloco guarda os ficheiros, as decisões tomadas, os resultados efetivamente verificados e o passo seguinte. O commit é a referência de retoma.
- Uma falha técnica fica com o comando ou operação, resultado observado e ação seguinte. A atualização seguinte distingue correção, limitação e trabalho pendente.
- Os resultados históricos conservam data e origem. O estado atual do PDF e da CI liga a revisão exata que foi verificada.
- Para retomar, comparar o HEAD remoto com a árvore local, ler o último registo e abrir o bloco seguinte. Repetir verificações cujo conteúdo ou ambiente mudou.

## Registo de execução

| Bloco | Evidência ou decisão registada | Próximo passo |
|---|---|---|
| H0 | HEAD e PR confirmados, comparação do PDF feita, árvore local limpa | Guardar a ancoragem no GitHub |
| H1 | Ficção original da Lavandaria. Conceito de uma ilustração reutilizada em três enquadramentos. FFmpeg disponível. CLI HyperFrames ausente da cache local | Gerar a imagem, verificar pistas e composição, montar e exportar o cartaz e a curta |
| H2 | Identificados o acórdão SyRI e o comunicado oficial do tribunal | Conferir fundamentos e dispositivo, escrever o caso com alcance delimitado |
| H3 | Caso sintético de duas versões de uma política e uma cache indexada apenas pelo documento | Implementar a reprodução e validar a contenção e recuperação |

## Dependências pendentes de outros ensaios

O piloto de equipa depende de uma cópia íntegra do GGUF na revisão fixada. As duas tentativas anteriores terminaram por timeout e há zero inferências novas nesse piloto. O próximo passo desse ensaio é validar o SHA-256 e o runtime quando existir uma cópia íntegra. Estudos com participantes e ajuste de um LLM têm os seus próprios requisitos. Os blocos H0–H5 avançam com os recursos do manuscrito e experiências locais.
