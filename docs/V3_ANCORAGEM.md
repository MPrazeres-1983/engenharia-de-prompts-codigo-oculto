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
| A | 02, 03, 04, 05, 10, 11, 17, 34 | Revisto. Entrada com um pedido, comparação com as mesmas fontes, casos reservados, autoridade, cálculo verificável e descodificação JSON |
| B | 12, 13, 14, 15, 16, 18, 19, 35, 36, 37 | 35 e 36 revistos em H1. Faltam os oito restantes, de escrita, aprendizagem, criação e prática |
| C | 06, 08, 09 | Revisto. Probabilidades condicionais, tokenização e temperatura, entrada multimodal e verificação por fonte |
| D | 20, 21, 22, 23, 24, 40 | Pendente. Construção, fontes, autoridade e interoperabilidade |
| E | 25, 26, 27, 28 | Revisto. Métricas por decisão, autorização no executor, operação e supervisão. Integra H3 |
| F | 29, 48, 50 | Pendente. Futuros e comparação, com medidas e limites explícitos |

## Regras de registo

- Cada bloco guarda os ficheiros, as decisões tomadas, os resultados efetivamente verificados e o passo seguinte. O commit é a referência de retoma.
- Uma falha técnica fica com o comando ou operação, resultado observado e ação seguinte. A atualização seguinte distingue correção, limitação e trabalho pendente.
- Os resultados históricos conservam data e origem. O estado atual do PDF e da CI liga a revisão exata que foi verificada.
- Para retomar, comparar o HEAD remoto com a árvore local, ler o último registo e abrir o bloco seguinte. Repetir verificações cujo conteúdo ou ambiente mudou.

## Registo de execução

| Bloco | Evidência ou decisão registada | Próximo passo |
|---|---|---|
| H0 | Ancoragem publicada em `24d7057af22f06630892d8d7699cc4482786a9ad`. Base e PDF conferidos | Consultar o último bloco validado |
| H1 · `ad64b10d` | Entregue em `exemplos/atelier` e integrado nos capítulos 35, 36 e 49. Cartaz e guião A4, curta muda H.264 de 15 s com 360 fotogramas. Três amostras e seis fotogramas de fronteira revistos. Espaçamento do guião corrigido com fontes incorporadas. A montagem usa FFmpeg e uma ilustração original gerada | Ver a prova de H5. A comparação com espectadores é uma extensão |
| H2 · `70803be9` | Caso SyRI escrito no capítulo 45. Decisão de 05-02-2020, parágrafos verificados, referência `syri2020` e comunicado identificados no registo de fontes | Citações compostas em H5. O texto distingue sinalização de sanção e aplica perguntas de desenho a um cenário próprio |
| H3 · `28135e59` | Ensaio executado em `experiencias/operacao` e laboratório no capítulo 27. Com v2 vigente, v1 passa a forma, é encaminhada sem prazo e a cache por versão recupera v2. Seis testes específicos aprovados | Suíte completa e laboratório conferidos em H5 |
| H4-A · `b03cab45` | Oito capítulos revistos, de 02 a 34 pelos prefixos do lote A. Retomada a reclamação dos seis pares para ligar instrução, testes, evidência e estrutura. Corrigidos os exemplos de avaliação e de JSON | Continuar a partir do primeiro lote ainda aberto |
| H4-E · `8e638a30` | Quatro capítulos revistos. Distinção entre lançamento canário, sonda e avaliação A/B, custos de encaminhar, segurança na ferramenta e responsáveis pela contenção e revisão. Datas do artigo 113 reconfirmadas | Consolidar e validar a composição em H5 |
| H4-C · `dc67d734` | Três capítulos revistos. Corrigida a sequência de leitura em 06 e a remissão sobre cache KV. Contas de geração e exemplos Unicode conferidos localmente. O caso histórico de entrada de imagem e texto foi verificado no relatório técnico de 2023 | Consolidar em H5 |
| H5 | Prova A4 de 292 páginas, 74 laboratórios, 90 referências, 76 testes aprovados e geometria conferida. O locale português e os padrões de hifenização foram usados na composição final | Retomar em `12-escrita.tex`. O PR liga a CI da revisão identificada na folha de rosto |

## Dependências pendentes de outros ensaios

O piloto de equipa depende de uma cópia íntegra do GGUF na revisão fixada. As duas tentativas anteriores terminaram por timeout e há zero inferências novas nesse piloto. O próximo passo desse ensaio é validar o SHA-256 e o runtime quando existir uma cópia íntegra. Estudos com participantes e ajuste de um LLM têm os seus próprios requisitos. Estas dependências têm registos próprios e a retoma editorial pode avançar em paralelo.

## Próximas iterações

Estimativa de três iterações para uma versão candidata à aprovação do autor. Uma quarta serve para alterações da leitura independente ou para correr separadamente um ensaio que só fique disponível mais tarde. A conclusão depende dos resultados e dos recursos de cada bloco.

| Iteração | Primeiro passo e âmbito | Evidência de fecho |
|---|---|---|
| 1. Fecho editorial | Começar em `src/capitulos/12-escrita.tex`. Acabar B (12, 13, 14, 15, 16, 18, 19, 37), depois D (20, 21, 22, 23, 24, 40) e F (29, 48, 50). Cruzar o resultado com a matriz para identificar aprofundamentos setoriais prioritários | 17 ficheiros revistos com alterações e fontes localizáveis. Percursos introdutório, prático e técnico com remissões verificadas. Um commit por lote |
| 2. Ensaios e fontes | Retomar o protocolo do piloto em `experiencias/equipas` se houver GGUF íntegro. Conferir fontes e versões das afirmações sensíveis. Decidir que experiências de adaptação, interoperabilidade e leitura podem ser efetivamente executadas e documentar as que ficam como propostas | Registos de entradas, configuração, resultados e falhas para os ensaios feitos. Alcance e estado por fonte e por experiência |
| 3. Candidata a publicação | Leitura integral, revisão independente, correções, prova A4 e critérios de aceitação. Levar título, capa e aprovação ao autor | PDF identificado com a revisão, fontes conferidas, validação local e CI do HEAD. Registo de decisões para aprovação |
| 4. Se necessária | Corrigir observações da leitura independente ou fechar um ensaio desbloqueado depois da candidata | Diferenças, nova prova e validação do conteúdo afetado |

Para retomar, começa pelo primeiro ficheiro indicado, confirma o HEAD no PR #2 e lê os últimos registos deste documento. O histórico permite ligar cada decisão ao ficheiro, à fonte ou ao ensaio que a sustenta.
