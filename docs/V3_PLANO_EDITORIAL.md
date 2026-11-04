# Terceira edição: plano editorial e mapa de migração

Data de início: 04-11-2026. Base verificada: `main@975ade89632700918786603dc23722e74f8610f7`, PR #1 integrado em 03-11-2026. Árvore de base: `13de7f25f76d803ed5f68878b6cab804727fd985`. A cópia de trabalho foi confrontada por hashes de blobs com a árvore do GitHub. Branch: `terceira-edicao-ia-referencia-2026`. Sem merge, tag, release ou publicação nesta execução.

## Identidade e títulos para decisão do autor

1. **O Código Oculto da Inteligência Artificial — Compreender, Criar e Construir.** Recomendado e usado provisoriamente: conserva a identidade anterior e descreve a nova amplitude sem prometer uma enciclopédia definitiva.
2. **Inteligência Artificial por Dentro e por Fora — Da Primeira Conversa aos Sistemas Autónomos.** Mais explícito para leitores novos, mas perde a ligação imediata ao título anterior.
3. **Viver, Criar e Trabalhar com Inteligência Artificial — O Código Oculto.** Privilegia aplicações e sociedade; torna menos visível a profundidade de engenharia.

A capa ilustrada original fica preservada como imagem histórica; a folha de rosto identifica a terceira edição e o título provisório. Não se redesenha nem se simula aprovação comercial do novo título. Autoria, proveniência e CC BY-NC-SA 4.0 mantidas.

## Princípios de produção

Na retoma de 04-11-2026, o autor reforçou a progressão do básico à especialização e uma leitura com curiosidade, investigação e humor pontual. A aplicação está documentada em `V3_LINHA_NARRATIVA.md`. Casos e diálogos originais podem envolver o leitor; não substituem fontes, medições ou declarações de incerteza. O livro mantém a arquitetura de dez partes e apresenta aprofundamentos matemáticos opcionais na primeira leitura.

Ler o manuscrito existente antes de o mover; conservar explicações corretas e dados experimentais. Números nos nomes dos ficheiros são identificadores históricos, não a ordem final dos capítulos. `src/livro.tex` determina a ordem, e labels determinam as referências. Não renomear caminhos só por estética.

Introduzir progressivamente os conceitos; oferecer um percurso rápido que leve à primeira conversa antes da matemática. Usar o corpo principal para explicação e os laboratórios para experimentação. Não acrescentar páginas por formatação, capítulos vazios ou listas de ferramentas. O intervalo 450–600 páginas é indicativo, nunca um teste de aceitação automatizado.

## Dez partes e objetivos

| Parte | Objetivo verificável do leitor | Conteúdo migrado | Produção prevista |
|---|---|---|---|
| I. A Revolução da Inteligência Artificial | Distinguir IA, modelo e aplicação; situar marcos e limites das alegações | 01 | 30: história, inteligência, ANI/AGI/ASI e mitos |
| II. Compreender a Máquina | Explicar treino, generalização, reforço e geração, incluindo exemplos calculáveis | 06, 07, 08, 09 | 31: ML; 32: RL; 33: arquiteturas generativas |
| III. Conversar e Pensar com IA | Formular uma tarefa e verificar estrutura, evidência e incerteza | 02–05, 10–11, 17 | 34: engenharia de contexto e memória |
| IV. Criar, Trabalhar e Brincar com IA | Concluir pequenos projetos pessoais, criativos e profissionais com critérios | 12–16, 18–19 | 35: imagem/design; 36: audiovisual; 37: jogos e experiências sem código |
| V. Construir Sistemas Inteligentes | Escolher entre fluxo, agente e equipa; manter autorização e contratos | 20–24 | 38: skills; 39: multiagentes; 40: interoperabilidade/A2A |
| VI. Treinar, Adaptar e Executar Modelos | Escolher técnica de adaptação e estimar recursos sem confundir pesos e memória total | nenhum capítulo autónomo | 41: fine-tuning/LoRA/QLoRA/distilação; 42: execução local/quantização |
| VII. Testar, Proteger e Operar IA | Criar avaliação, limites de ação e resposta a incidentes | 25–28 | Complementos de skills e multiagentes, oráculos e falhas parciais |
| VIII. A IA e a Transformação da Sociedade | Distinguir exposição, efeito observado, causalidade e cenário | apenas fragmentos de 29 | 43: trabalho; 44: ciência/mundo físico; 45: informação/poder; 46: relações/cognição; 47: energia/geopolítica |
| IX. O Futuro da Inteligência | Comparar cenários por pressupostos e sinais que os podem contrariar | 29, revisto para competências e decisões | 48: robótica, modelos do mundo, consciência, AGI e cenários |
| X. O Grande Laboratório de IA | Executar projetos e apresentar evidência com limites explícitos | 47 Prompt Labs existentes e experiências reais preservados | 49: projetos integrados; 50: comparação de arquiteturas e protocolo humano/IA |

Os três apêndices mantêm padrões, glossário e leitura de fontes. O glossário será ampliado e revisto para eliminar generalizações que o corpo já evita.

## Dependências e validação

1. Fechar auditoria e inventário inicial; guardar checkpoint A.
2. Verificar fontes primárias e escrever capítulos com remissões que resolvam redundâncias.
3. Implementar exemplos offline: treino mínimo, cálculo de atenção, estimador de memória, validação da skill demonstrativa e controlador com falhas parciais.
4. Separar testes de código de medições com LLM e de ensaios com pessoas. Não converter stubs determinísticos em benchmark de inteligência.
5. Substituir contagens fixas da segunda edição por um manifesto explícito e verificado; compilar e inspecionar páginas.
6. Guardar commits lógicos e criar PR Draft. Descrever o estado real, incluindo aprofundamentos que continuem pendentes.

## Limites de revisão

Esta execução pode produzir e rever um manuscrito substancial, mas não substitui pareceres independentes de ciência, direito, pedagogia e edição. Ausência de erro LaTeX não encerra essas revisões. Resultados publicados só são atribuídos à população, versão e desenho estudados. Onde não se obteve o texto integral, fica registado o alcance efetivo da consulta.
