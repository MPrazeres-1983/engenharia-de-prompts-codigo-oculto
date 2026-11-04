# Matriz de cobertura editorial V3

Auditoria inicial de 04-11-2026, sobre a segunda edição integrada. Leitura integral dos 29 capítulos e três apêndices. Os identificadores são os prefixos dos ficheiros, não a numeração após a migração. Estado inicial não significa defeito crítico: uma introdução pode ser correta e insuficiente para a nova amplitude.

Estados utilizados: **Suficientemente coberto**, **Necessita aprofundamento**, **Necessita atualização**, **Necessita reorganização**, **Tema ausente**, **Conteúdo redundante**. Os dez eixos pedidos estão distribuídos nas duas tabelas com o mesmo ID.

## Rigor, atualidade, clareza, profundidade e exemplos

| ID | Estado inicial | Rigor | Atualidade | Clareza | Profundidade | Exemplos |
|---|---|---|---|---|---|---|
| 01 | Suficientemente coberto | Correto no âmbito introdutório | Conceitos estáveis | Boa entrada pela Lavandaria | Introdução, não história geral | Um exercício de escolha de ferramenta |
| 02 | Suficientemente coberto | Distingue ilustração e medição | Sem dependência de produto | Pedido progressivo e verificável | Adequado a iniciantes | Variações e critérios explícitos |
| 03 | Necessita reorganização | Analogia código com limite declarado | Retirar marca de segunda edição | Muitas listas; reduzir absolutos | Método prático suficiente | Desenvolvimento/teste separados |
| 04 | Necessita aprofundamento | ICL distinto de ajuste de pesos | Não fixar 2–10 como regra | Exemplos claros; qualificações necessárias | Context engineering breve | Boas comparações controladas |
| 05 | Necessita atualização | Recência tratada como regra excessiva | Papéis dependem da API | Bom contraexemplo de persona | Mecanismo não se infere de tom | Debate não independente bem assinalado |
| 06 | Necessita reorganização | Autoregressão bem delimitada | Evitar universalizar Transformers | Boa fórmula com leitura em palavras | Sobrepõe fundamentos de 01/07 | Probabilidades identificadas como inventadas |
| 07 | Necessita atualização | Atenção, máscara e dimensões corretas | Receita RLHF omite SFT na enumeração | Matemática com exemplo calculável | Aprofundamento opcional útil | Atenção didática não é medição |
| 08 | Suficientemente coberto | Temperatura/top-p corretos e delimitados | Parâmetros variam por serviço | Explica limites sem pseudociência | Boa ponte para operação | Contagens pedem tokenizador concreto |
| 09 | Necessita aprofundamento | Definição unimodal erradamente restrita a texto | Capacidades dependem da versão | Exemplos práticos legíveis | Visão e ASR; pouco vídeo/música | OCR com validação contra original |
| 10 | Suficientemente coberto | CoT/ToT/procura bem distintos | Métodos históricos contextualizados | Explicação acessível | Adequado ao prompting | Oráculos e condições definidos |
| 11 | Necessita reorganização | Crítica não equivale a verificação | Interfaces de ferramentas versionadas | Excesso de enumerações | Bom método com sinal externo | Código executado fora do chat |
| 12 | Necessita atualização | Detetores corretamente limitados | Sem alegação universal de deteção | Tom humano; alguns absolutos | Conselhos editoriais suficientes | Revisão sem mudar factos |
| 13 | Necessita aprofundamento | Afirmações de perda cognitiva sem estudo | Adicionar evidência experimental | Direto mas por vezes paternalista | Falta distinguir apoio/aprendizagem | Exercícios com teste sem ajuda |
| 14 | Necessita reorganização | Regras de compromisso bem separadas | Políticas de fornecedor a verificar | Aplicável ao quotidiano | Adequado ao público geral | Email não enviado automaticamente |
| 15 | Necessita atualização | Generalizações de ficção sem medição | Criatividade não implica autoria legal | Voz e humor preserváveis | Estrutura narrativa útil | Comparações aceitam empate |
| 16 | Suficientemente coberto | Ficha de evidência e alcance corretos | Versões de fontes a conservar | Método claro | Adequado à investigação inicial | Comparações de métodos verificáveis |
| 17 | Suficientemente coberto | Sintaxe/estrutura/semântica separados | Confirmar API; não copiar limites | Exemplos JSON válidos | Boa profundidade de contrato | Parsing e negativos explícitos |
| 18 | Necessita atualização | Causas narradas precisam de fonte | SQL depende do dialeto | Algumas certezas excessivas | Método de análise adequado | Cardinalidade e fronteiras relevantes |
| 19 | Suficientemente coberto | Testes precisam de oráculo independente | Docs de bibliotecas por versão | Adequado a quem programa | Boa ponte para Spec-First | Execução isolada explícita |
| 20 | Suficientemente coberto | Critérios positivos e negativos claros | Sem promover formato proprietário | Bom caso de QA | Adequado ao projeto integrado | CA-01 a CA-06 executáveis |
| 21 | Suficientemente coberto | Pesquisa/proveniência/autoridade separados | Métodos estáveis; fontes versionadas | Explicação e figura claras | Boa base; não promete verdade | Distingue offline de LLM |
| 22 | Suficientemente coberto | MCP 2026-07-28 já atualizado | Confirmado na especificação oficial | Fronteira de confiança bem explicada | Falta relação com A2A/skills | Executor não se anuncia servidor MCP |
| 23 | Necessita aprofundamento | Agente definido no âmbito LLM | Sem superioridade geral demonstrada | Distinção de fluxo útil | Multiagente só referido | Falta controlador de equipa |
| 24 | Suficientemente coberto | Limites da demonstração honestos | Dependências mínimas | Caso integrado claro | Não é serviço de produção | 30 testes e 12 regressões existentes |
| 25 | Necessita aprofundamento | Métricas e amostras bem limitadas | Dados reais preservados | Mais listas do que necessário | Benchmarks/contaminação pouco desenvolvidos | 52 inferências com resultados negativos |
| 26 | Necessita atualização | Prompt não é firewall; correto | OWASP2025 explícito | Advertências excessivas | Falta cadeia de skills e agentes | Negativos de autorização existentes |
| 27 | Suficientemente coberto | Custo por tarefa e cache corretos | Preços não fixados | Muitas listas; núcleo sólido | Boa operação introdutória | Falta ensaio de recuperação distribuída |
| 28 | Suficientemente coberto | Âmbito legal e voluntário separados | Calendário 2026 já documentado | Claro e delimitado | Não é parecer jurídico | Ficha e responsáveis verificáveis |
| 29 | Necessita reorganização | Cenários misturam previsão e conselho | Tendências precisam de data/fonte | Excesso de máximas profissionais | Sociedade/futuros muito comprimidos | Plano pessoal útil |

## Fontes, terminologia, redundâncias, lacunas e relevância

| ID | Fontes | Terminologia | Redundâncias | Lacuna / ação | Relevância e destino |
|---|---|---|---|---|---|
| 01 | Goodfellow; reforçar origem histórica | Distingue modelo/aplicação | Treino repetido em 06/07 | História e ANI/AGI/ASI | Entrada da Parte I |
| 02 | Método editorial; sem alegações universais | Uniformizar rascunho/ação | Regras retomadas em 03 | Remissão para percurso rápido | Entrada prática da Parte III |
| 03 | Falta base de método para algumas máximas | Reduzir inglês dispensável | Checklist repete apêndice A | Remeter contexto/skills | Conservar na Parte III |
| 04 | Brown; falta memória e posição | Distinguir demonstração de treino | Janela repetida em 05/07 | Compaction, memória, proveniência | Base para novo capítulo 34 |
| 05 | Model Spec versionado | Metacognição/persona não são pessoas | Resumo repetitivo | Corrigir deriva monotónica | Conservar; separar persona de agente |
| 06 | Brown/Ouyang/Vaswani | Previsão não é verificação | Treino e história linguística repetidos | Fundamentos ML anteriores | Conservar como ponte técnica |
| 07 | Fontes primárias relevantes | Alinhamento não equivale a cortesia | Janela repetida em 04 | Corrigir receita e definição | Núcleo técnico da Parte II |
| 08 | Holtzman e documentação específica | Não equiparar instrução a temperatura | Contagem repete advertências | Referenciar estimador de recursos | Conservar na Parte II |
| 09 | Relatório de modelo não cobre toda a área | Raster/vetor separados | Privacidade repete 28 | Novos capítulos criativos e difusão | Ponte entre mecanismo e uso |
| 10 | Artigos originais; limites explícitos | Explicação não é transcrição interna | Recursão retomada em 11 | Ligar controlador executável | Conservar na Parte III |
| 11 | Huang e function calling | Corrigir recursivo para iterativo | Loop e ferramenta repetidos em 23 | Remeter arquitetura em vez de repetir | Conservar e limpar termos |
| 12 | Sadasivan; estilo como preferência | Retirar afirmação jurídica vaga sobre mortos | Comunicação repete 14 | Qualificar melhoria garantida | Conservar na Parte IV |
| 13 | Adicionar Bastani e UNESCO | Evitar diagnóstico por uso de IA | Avisos repetidos | Evidência de aprendizagem e limites | Conservar; ligar a 46 |
| 14 | Não atribuir rankings a fornecedores | Uniformizar restrições/âmbito | Email repete 12 | Remeter inventário de autorização | Conservar na Parte IV |
| 15 | Adicionar Doshi/Hauser com alcance | Limitar metáforas de sala de escritores | Estilo repete 12 | Criatividade individual/diversidade | Conservar com qualificação |
| 16 | Fontes existentes não bastam; bem explicado | Distingue ausência de suporte/falsidade | Revisão estilística repete 12 | Ligar ciência aplicada a 44 | Conservar na Parte IV |
| 17 | JSON Schema e documentação | Eliminar bagunça/pular | Contrato retomado em 24 | Remeter schema em skill/agente | Mover para Parte III |
| 18 | Reforçar análise causal em 43 | Uniformizar determinístico | Dados/narrativa retomados | Não afirmar invenção inevitável | Conservar na Parte IV |
| 19 | Método de engenharia; não benchmark | Uniformizar par e revisão | Spec repetida brevemente | Ligar avaliações de produtividade | Conservar com remissões |
| 20 | Boa prática; sem superioridade inventada | Observado/decisão/dúvida consistentes | Referências úteis a 24 | Ampliar critérios a skills/equipa | Abrir Parte V |
| 21 | Lewis/BM25/RRF | RAG não é base vetorial | Contexto longo repetido em 34 | Migração de índice como extensão | Conservar na Parte V |
| 22 | Versões e changelog explícitos | Descoberta não é autorização | Contrato repete 11/24 | Novo capítulo 40 | Conservar sem reescrever história |
| 23 | ReAct; acrescentar AutoGen | Não universalizar agente=LLM | Padrões reaparecem em 39 | Estado, falhas, delegação, custo | Base para 39 |
| 24 | Ensaio real guardado separadamente | CLI não autentica | Exemplifica capítulos anteriores | Retomar no laboratório final | Preservar implementação e dados |
| 25 | Wilson, Zheng e registos | Não confundir pass com fiabilidade | Critérios retomados em labs | Ablation, testes de skills/equipa | Conservar na Parte VII |
| 26 | OWASP; não certificação | Precisar jailbreak/injeção | Muitas listas repetem a fronteira | Supply chain e autoridade delegada | Conservar e complementar |
| 27 | RGPD para pseudonimização | Logs não equivalem a anonimização | Governança repetida em 28 | Exercício de incidente de equipa | Conservar na Parte VII |
| 28 | Atos oficiais; alcance declarado | Consentimento não é fundamento único | Repetir menos em sociedade | Propriedade intelectual e esfera pública | Conservar e remeter |
| 29 | Fontes de impacto em falta | Metáfora colega não é pessoa | Sociedade repete 28 | Separar partes VIII e IX | Encurtar; conservar percurso profissional |

## Apêndices e temas sem capítulo próprio

| Conteúdo | Estado inicial | Decisão e razão |
|---|---|---|
| A: padrões | Conteúdo redundante | Conservar para consulta, substituir repetições teóricas por remissões; não recomendar revisão infinita. |
| B: glossário | Necessita atualização | LLM não se limita a previsão autoregressiva; unimodal não é só texto; janela depende da interface; ampliar termos novos. |
| C: leitura de fontes | Suficientemente coberto | Preservar protocolo e ligar ao novo registo, mantendo o histórico da segunda edição. |
| História, ANI/AGI/ASI | Tema ausente | Criar 30; fontes originais, definições operacionais e ausência de datas prometidas. |
| ML supervisionado/não supervisionado, generalização | Necessita aprofundamento | Criar 31; separação treino/teste, exemplos calculáveis e baseline. |
| Reinforcement learning | Tema ausente | Criar 32; retorno, exploração, simulador e limites do feedback. |
| Difusão e outras arquiteturas | Tema ausente | Criar 33; não chamar Transformer a toda a IA generativa. |
| Engenharia de contexto e memória | Necessita aprofundamento | Criar 34 com seleção, compressão e controlo de origem. |
| Imagem, vídeo, música, voz, animação e jogos | Necessita aprofundamento | Criar 35–37; projetos sem código com critérios de continuidade, consentimento e direitos. |
| Agent Skills e SKILL.md | Tema ausente | Criar 38 e pacote demonstrativo auditável, sem instalar no ambiente do leitor automaticamente. |
| Sistemas multiagente | Necessita aprofundamento | Criar 39; comparar com fluxo fixo; comunicação, estado, falhas e orçamento. |
| A2A e interoperabilidade | Tema ausente | Criar 40; distinguir capacidades declaradas de execução e de autorização. |
| Fine-tuning, LoRA, QLoRA, distilação | Tema ausente | Criar 41; critérios e limites; não inventar treino executado. |
| Modelos locais, quantização, CPU/GPU | Necessita aprofundamento | Criar 42; memória de pesos não é memória total; cálculo verificado. |
| Trabalho, educação, ciência e setores | Necessita aprofundamento | Criar 43–44; estudos com desenho, população e limites. |
| Informação, poder, justiça e cultura | Necessita aprofundamento | Criar 45; distinguir norma, evidência e posição editorial. |
| Antropomorfização, relações e cognição | Tema ausente | Criar 46; separar correlação de atribuição aleatória e não generalizar efeitos clínicos. |
| Energia, semicondutores e geopolítica | Tema ausente | Criar 47; limites de sistema, projeções, concentração e dependências. |
| Modelos do mundo, robótica, consciência e AGI | Necessita aprofundamento | Criar 48 com cenários e indicadores que os podem contrariar. |
| Laboratórios integrados e comparações | Necessita aprofundamento | Criar 49–50; resultado esperado não é medição; ensaio humano fica pendente até existir. |

## Balanço inicial

O núcleo de engenharia deve ser preservado. As maiores mudanças são de amplitude e de profundidade, com correções dirigidas de afirmações excessivas. O estado final por tema e as limitações de produção constarão de `V3_PROGRESSO.md`; esta auditoria inicial não será reescrita como se as lacunas nunca tivessem existido.
