# Fontes e alcance da verificação

Data de corte: **3 de novembro de 2026**. As 38 entradas em `src/referencias.bib` têm títulos e ligações concretas. Esta é uma revisão dirigida das afirmações e lacunas do manuscrito, não uma revisão sistemática exaustiva de toda a investigação publicada até essa data. Os resultados dos artigos pertencem às condições estudadas; o texto evita transportar percentagens para modelos ou tarefas não avaliados.

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
| `wei2022` | [Chain-of-Thought](https://arxiv.org/abs/2201.11903) | Exemplos de resolução e ganhos experimentais delimitados. |
| `kojima2022` | [Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) | Técnica histórica de instrução de resolução sem demonstrações. |
| `wang2023` | [Self-Consistency](https://arxiv.org/abs/2203.11171) | Amostrar percursos e agregar respostas; não cinco soluções consecutivas na mesma mensagem. |
| `yao2023tot` | [Tree of Thoughts](https://arxiv.org/abs/2305.10601) | Procura em estados intermédios; comparação de propostas não é implementação do algoritmo. |
| `turpin2023` | [Unfaithful explanations](https://arxiv.org/abs/2305.04388) | Explicações podem omitir influências da decisão. Não prova que todas as explicações sejam inúteis. |
| `huang2024` | [Self-correction](https://arxiv.org/abs/2310.01798) | Limites da autocorreção intrínseca nas tarefas testadas, sem generalizar a impossibilidade de correção futura. |
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
| `rgpd2016` | [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Texto oficial identificado; excertos indexados de artigos 6 e 22 consultados. A abertura direta devolveu verificação anti-robot. Revisão jurídica integral pendente. |
| `aiact2024` | [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689) | Referência oficial identificada; acesso direto à consolidação 2026-07-27 bloqueado por verificação anti-robot. Não se declara auditoria jurídica do texto integral. |
| `conselho2026` | [Cronologia do Conselho](https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/timeline-artificial-intelligence/), entradas de 29-06 e 02-08-2026 | Confirma alterações de calendário e aplicação de regras. Na divergência com um resumo institucional sobre sandboxes, essa data foi omitida do livro; confirmar o ato aplicável. |

## Experiências e limitações

- Nenhuma chamada paga nem execução de um LLM real foi efetuada para atribuir desempenho a um modelo.
- O caso offline e os testes verificam código, contratos, acesso e regressões conhecidas. Os resultados constam do relatório de validação; não são um benchmark de IA.
- A fórmula de atenção foi corrigida e o exemplo `[0, ln(3)]` com valores `[2, 6]` dá `5`. A amostragem e o cálculo de Wilson são apresentados com hipóteses explícitas.
- Toda a matéria jurídica continua sujeita a confirmação humana no texto em vigor antes de publicação; não se infere conformidade de um produto a partir deste livro.
- Para uma futura atualização, rever primeiro protocolos, APIs, legislação e relatórios de modelos; as referências históricas mantêm-se quando explicam a origem de uma técnica.
