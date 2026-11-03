# Fontes e alcance da verificação

Data de corte: **3 de novembro de 2026**. As 41 entradas em `src/referencias.bib` têm títulos e ligações concretas. Esta é uma revisão dirigida das afirmações e lacunas do manuscrito, não uma revisão sistemática exaustiva de toda a investigação publicada até essa data. Os resultados dos artigos pertencem às condições estudadas; o texto evita transportar percentagens para modelos ou tarefas não avaliados.

**Alcance:** nos artigos, foram confirmados metadados e resumos originais; foram consultadas secções específicas quando indicadas abaixo. Não se afirma ter reproduzido os estudos ou auditado integralmente todos os papers. Os exemplos numéricos são separados dos resultados publicados. As fontes de fornecedor descrevem interfaces e orientações, não constituem comparação independente entre produtos.

| Chave BibTeX | Fonte primária e localização | O que suporta / limite |
|---|---|---|
| `goodfellow2016` | [Deep Learning](https://www.deeplearningbook.org/), capítulo 5 | Treino, parâmetros, generalização e distinção de avaliação; consulta de secções de fundamentos. |
| `jurafsky` | [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) | Livro de aprofundamento; edição em linha em evolução, sem lhe atribuir uma data de publicação inventada. |
| `vaswani2017` | [Artigo original, v7](https://arxiv.org/html/1706.03762v7), secção 3 | Atenção escalada, máscara causal, arquitetura encoder–decoder, posições e feed-forward. A figura do livro é uma simplificação própria. |
| `brown2020` | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | Demonstrações em contexto sem atualização de pesos; resultados não generalizados a todos os sistemas. |
| `mikolov2013` | [Word representations](https://arxiv.org/abs/1301.3781) | Embeddings estáticos e regularidades aproximadas; não são uma álgebra universal de significado. |
| `ouyang2022` | [InstructGPT/RLHF](https://arxiv.org/abs/2203.02155) | Pós-treino e preferências humanas; não uma receita obrigatória para todos os fornecedores. |
| `bai2022` | [Constitutional AI](https://arxiv.org/abs/2212.08073) | Exemplo de treino com feedback de IA. |
| `rafailov2023` | [DPO](https://arxiv.org/abs/2305.18290) | Alternativa à sequência explícita recompensa + RL; não equivalência de todos os métodos. |
| `liu2024` | [Lost in the Middle](https://arxiv.org/abs/2307.03172) | Efeito experimental da posição em tarefas/modelos identificados, sem lei universal de atenção. |
| `holtzman2020` | [Neural Text Degeneration](https://arxiv.org/abs/1904.09751) | Nucleus sampling; o livro distingue amostragem, estilo e correção. |
| `wei2022` | [Chain-of-Thought v6](https://arxiv.org/html/2201.11903v6), secções 2–3 e apêndice A.3 | Demonstrações de resolução e ganhos dependentes de escala, tarefa e prompt; métodos e limites consultados, sem reprodução do benchmark. |
| `kojima2022` | [Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) | Técnica histórica de instrução de resolução sem demonstrações. |
| `wang2023` | [Self-Consistency v4](https://arxiv.org/html/2203.11171v4), secção 2 | Método de amostragem de percursos diversos e agregação das respostas finais; não cinco soluções consecutivas na mesma mensagem. |
| `yao2023tot` | [Tree of Thoughts v2](https://arxiv.org/html/2305.10601v2), secção 3 | Estados intermédios, geração, avaliação e procura com BFS/DFS; comparação de propostas não implementa o algoritmo. |
| `turpin2023` | [Unfaithful explanations](https://arxiv.org/abs/2305.04388) | Explicações podem omitir influências da decisão. Não prova que todas as explicações sejam inúteis. |
| `huang2024` | [Self-correction v2](https://arxiv.org/html/2310.01798v2), secções 2 e 3.1–3.2 | Distingue feedback intrínseco de rótulos-oráculo; modelos de 2023, benchmarks e redução de desempenho nas condições testadas. Não prova impossibilidade de correção futura. |
| `deepseek2025` | [DeepSeek-R1](https://arxiv.org/abs/2501.12948), revisão de 2026 | Exemplo documentado de pós-treino orientado a raciocínio. Não revela arquiteturas privadas de outros modelos. |
| `lewis2020` | [RAG](https://arxiv.org/abs/2005.11401) | Trabalho original de recuperação + geração; padrões práticos posteriores são identificados como arquitetura de engenharia. |
| `robertson2009` | [BM25 and Beyond](https://doi.org/10.1561/1500000019) | Metadados/descrição primária do enquadramento probabilístico; não se afirma leitura integral da monografia paga. |
| `cormack2009` | [Reciprocal Rank Fusion](https://doi.org/10.1145/1571941.1572114) | Metadados e descrição original; fórmula usada como definição, sem importar ganhos para o exemplo. |
| `yao2023react` | [ReAct](https://arxiv.org/abs/2210.03629) | Intercalar ações e resolução em ambientes estudados. Não prova superioridade de multiagentes em geral. |
| `gpt4report2023` | [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) | Exemplo histórico de modelo com entradas multimodais; não especificação de todos os modelos atuais. |
| `sadasivan2023` | [AI text detection](https://arxiv.org/abs/2303.11156), v4 | Limites de robustez de detetores; não é guia para ocultar autoria. |
| `zheng2023` | [LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) | Enviesamentos do juiz e necessidade de controlo experimental. |
| `wilson1927` | [Artigo original](https://doi.org/10.1080/01621459.1927.10502953) | Metadados confirmados no editor; cálculo implementado e comparado com valores numéricos de referência. Não se estima fiabilidade de produção com os casos de regressão. |
| `jsonschema2020` | [Validação JSON Schema, draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation) | Sintaxe, estrutura e semântica são verificações distintas. O validador local aplica apenas o contrato concreto. |
| `modelspec2026` | [Model Spec 2026-10-29](https://model-spec.openai.com/2026-10-29.html), chain of command | Hierarquia específica de uma plataforma, não semântica universal das mensagens. |
| `functioncalling2026` | [Function calling](https://developers.openai.com/api/docs/guides/function-calling), fluxo de chamada | Modelo propõe; aplicação executa e devolve resultado. |
| `structured2026` | [Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | Capacidade de fornecedor com limitações de esquema/estado; não garantia de factos verdadeiros. |
| `reasoning2026` | [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices), prompting | Pedidos diretos e cautela com instruções de CoT nos modelos abrangidos. |
| `mcp2026` | [MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) | Host, cliente, servidor, recursos, prompts e ferramentas; versão fixada. |
| `mcpchanges2026` | [Changelog 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) | Pedidos sem sessão de protocolo, metadados por pedido, `server/discover` e remoção de handshake anterior. |
| `mcpauth2026` | [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) | Requisitos de autorização e destinatário dos tokens. Não há servidor MCP implementado no exemplo. |
| `owasp2025` | [OWASP LLM Top 10, 2025](https://genai.owasp.org/llm-top-10/) | Taxonomia versionada de riscos, orientação e não certificação. |
| `nist2024` | [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) | Quadro voluntário de gestão de riscos de IA generativa. |
| `rgpd2016` | [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj), considerando 26 e artigos 5, 6, 9, 22 e 35 | Confirmados princípios, fundamentos, pseudonimização, âmbito/exceções de decisões automatizadas e avaliação de impacto nas disposições oficiais indexadas. Abertura direta bloqueada por verificação anti-robot; não se declara auditoria jurídica integral. |
| `aiact2024` | [AI Act consolidado em 27-07-2026](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX%3A02024R1689-20260727), artigo 113 | Confirmada aplicação geral em 02-08-2026, exceções e ato modificador no texto oficial indexado. Não se declara leitura integral da consolidação. |
| `aiomnibus2026` | [Regulamento (UE) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj), artigo 1, ponto 40, e artigo 4 | Publicado em 24-07 e em vigor em 27-07-2026. Capítulo III, secções 1–3, exceto artigo 6(5): 02-12-2027 para artigo 6(2)/anexo III e 02-08-2028 para artigo 6(1)/anexo I. Disposições oficiais indexadas consultadas; acesso direto continua limitado. |
| `qwengguf` | [Modelo oficial Qwen](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/tree/9217f5db79a29953eb74d5343926648285ec7e67) | Modelo de 0.5B, licença Apache-2.0; ficheiro Q4_K_M descarregado da revisão fixada e SHA-256 verificado. Descrição do fornecedor não usada como resultado independente. |
| `llamacpp` | [Servidor llama.cpp b11960](https://github.com/ggml-org/llama.cpp/blob/b11960/tools/server/README.md) | Documentação da API, seed, amostragem e response_format com esquema. Build oficial descarregado, digest SHA-256 confrontado com metadados da release; executado localmente em CPU. |
| `conselho2026` | [Cronologia do Conselho](https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/timeline-artificial-intelligence/), entradas de 29-06 e 02-08-2026 | Confirma alterações de calendário e aplicação de regras. Na divergência com um resumo institucional sobre sandboxes, essa data foi omitida do livro; confirmar o ato aplicável. |

## Experiências e limitações

- Foram efetuadas 52 inferências reais, sem serviços pagos, com um Qwen local quantizado. Casos, variantes, configurações e respostas estão em `experiencias/llm_local`. Não se apresenta esta amostra como avaliação de todos os modelos ou dos 47 laboratórios.
- O caso offline e os testes verificam código, contratos, acesso e regressões conhecidas. Os resultados constam do relatório de validação; não são um benchmark de IA.
- A fórmula de atenção foi corrigida e o exemplo `[0, ln(3)]` com valores `[2, 6]` dá `5`. A amostragem e o cálculo de Wilson são apresentados com hipóteses explícitas.
- As afirmações jurídicas concretas do capítulo 28 foram confrontadas com as disposições oficiais acima. Não houve parecer de advogado nem decisão de conformidade de um produto; essas atividades dependem de um caso concreto e não se inferem desta revisão documental.
- Para uma futura atualização, rever primeiro protocolos, APIs, legislação e relatórios de modelos; as referências históricas mantêm-se quando explicam a origem de uma técnica.
