# Fontes e evidências V3

Data de corte e consulta: **04-11-2026**. A bibliografia herdada e o seu alcance de consulta permanecem em `FONTES_VERIFICADAS.md`. Não se transforma esse registo histórico numa alegação de nova leitura integral. Este registo acrescenta fontes efetivamente consultadas na terceira edição.

Uma página oficial suporta a descrição da própria interface; não demonstra superioridade comercial. Um resumo confirma assunto e resultados nele declarados; detalhes metodológicos exigem leitura da secção correspondente. Resultados alheios não foram reproduzidos nesta execução. Exemplos matemáticos e software próprios têm validação separada.

## Verificações iniciais

| Fonte primária | Versão / localizador | Suporte e limites |
|---|---|---|
| [Agent Skills](https://agentskills.io/specification) | Especificação consultada, secções de frontmatter, nome e divulgação progressiva | Estrutura de pacote e campos. Não define instalação universal, seleção infalível ou barreira de execução. |
| [MCP](https://modelcontextprotocol.io/specification/2026-07-28) | 2026-07-28, visão geral | A versão já citada na segunda edição continua identificada; não é necessário repetir a migração anterior. |
| [A2A](https://a2a-protocol.org/v1.0.0/specification/) | 1.0.0, visão geral e modelo de dados | Agent Card, mensagens, tarefas e artefactos. Não confundir `AgentSkill` do catálogo A2A com o pacote `SKILL.md`. |
| [AutoGen](https://arxiv.org/abs/2308.08155) | v2, 03-10-2023, metadados e resumo | Framework de conversação entre agentes; não é prova universal de vantagem de uma equipa. |
| [Dartmouth](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html) | Proposta de 31-08-1955 para o verão de 1956 | Origem documental do programa e do nome; não nascimento de todas as ideias de IA. |
| [Generative AI at Work](https://doi.org/10.1093/qje/qjae044) | Artigo QJE 140(2), 2025, pp. 889–942 | Adoção faseada em apoio ao cliente, produtividade e heterogeneidade. Usar o artigo final, não misturar amostras/percentagens de versões preliminares. |
| [OIT, índice de exposição](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) | Working Paper 140, 2025 | Exposição ocupacional baseada em tarefas, não previsão de despedimentos. |
| [IEA, Energy and AI](https://www.iea.org/reports/energy-and-ai) | 10-04-2025, procura de eletricidade | Estimativa de centros de dados, não contagem exclusiva de IA; cenários são projeções. Procurar atualização de 2026 antes de apresentar como estado mais recente. |
| [LoRA](https://arxiv.org/abs/2106.09685) | Artigo original, metadados e resumo | Congelar pesos base e aprender atualização de baixo posto; resultados dependem da configuração. |
| [QLoRA](https://arxiv.org/abs/2305.14314) | NeurIPS 2023, metadados e resumo | Treinar adaptadores através de base quantizada; não reduz todos os requisitos ao tamanho do ficheiro. |
| [DDPM](https://arxiv.org/abs/2006.11239) | 2020, metadados e resumo | Família generativa por difusão; não descreve todos os sistemas de imagem atuais. |
| [Distilação](https://arxiv.org/abs/1503.02531) | Hinton, Vinyals e Dean, 2015 | Transferência de comportamento para outro modelo; herda limites e requer dados de avaliação. |
| [Aprendizagem com tutores](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/) | PNAS 2025, resumo, resultados e especificação de avaliação | Desempenho com ferramenta e aprendizagem sem ferramenta diferem; não concluir que toda a IA prejudica toda a aprendizagem. |
| [Efeitos psicossociais](https://www.media.mit.edu/publications/how-ai-and-human-behaviors-shape-psychosocial-effects-of-chatbot-use-a-longitudinal-controlled-study/) | Página dos autores, resumo revisto | Condições aleatorizadas sem efeitos significativos reportados; maior uso voluntário associado a piores indicadores. Distinguir essa associação de causalidade do tempo de uso. Resumos antigos diferem. |
| [Criatividade e diversidade](https://doi.org/10.1126/sciadv.adn5290) | Doshi e Hauser, Science Advances 2024 | Tarefa de histórias curtas; qualidade individual e diversidade coletiva são medidas diferentes. |
| [AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) | Nature 2021, resumo e descrição de CASP14 | Avaliação cega de estruturas, não demonstração de eficácia terapêutica. |
| [Regulamento 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj) | Ato oficial, metadados | Confirma existência do ato já usado na edição anterior. Não substitui análise jurídica de produto. |

## Integridade do trabalho anterior

Foram executados o verificador dos registos e os 30 testes da base. As 52 inferências de 03-11-2026 continuam históricas: não foram repetidas nem convertidas em resultados da V3. O livro distingue testes determinísticos, execução real com modelo e protocolos ainda não executados com leitores ou utilizadores.

## Índice das 32 entradas acrescentadas à bibliografia

As 41 entradas históricas mantêm o registo anterior. As 32 novas perfazem 73. Foram verificados títulos, autoria identificada, datas/versões e ligações primárias ou registos primários. DOI é incluído quando identificado, sem inventar um DOI para cada página. Nos estudos, a leitura foi dirigida ao resumo e às secções indicadas; não equivale a reprodução ou revisão integral de todos os artigos.

| Chave | Fonte / versão | Consulta e alcance |
|---|---|---|
| `turing1950` | [Mind, 1950](https://academic.oup.com/mind/article/LIX/236/433/986238), DOI 10.1093/mind/LIX.236.433 | Metadados e abertura no editor indexado; abertura direta do DOI bloqueada. Jogo de imitação, sem teste universal de consciência. |
| `dartmouth1955` | [Proposta original](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html), 31-08-1955 | Proposta para o verão de 1956; origem documental do programa. |
| `sutton2018` | [MIT Press, 2.ª edição](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) | Metadados de referência; definições e cálculos didáticos próprios, sem alegar reprodução experimental do livro. |
| `ho2020` | [DDPM v2](https://arxiv.org/abs/2006.11239v2) | Metadados e resumo; descrição da família, sem importar resultados de benchmark. |
| `rombach2022` | [CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) | Metadados/resumo original, difusão em representação latente e condicionamento; sem reimplementação. |
| `kingma2014` | [VAE](https://arxiv.org/abs/1312.6114), preprint 2013, ICLR 2014 | Metadados e resumo; descrição breve, sem números de desempenho. |
| `gan2014` | [GAN](https://arxiv.org/abs/1406.2661), 2014 | Metadados e resumo; título de conferência difere do título atual no arXiv, registado no BibTeX. |
| `radford2021clip` | [PMLR 139, 8748–8763](https://proceedings.mlr.press/v139/radford21a.html) | Metadados e resumo original; representação texto/imagem, sem universalizar capacidades. |
| `doshi2024` | [Science Advances](https://doi.org/10.1126/sciadv.adn5290) | Título, autores, DOI e resultado no âmbito de histórias curtas; não prova sobre todos os meios criativos. |
| `c2pa22` | [C2PA 2.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html) | Definições de proveniência, autenticidade e content credentials; versão explícita, sem a declarar a mais recente. |
| `unesco2023` | [UNESCO](https://doi.org/10.54675/EWZM9535), 2023 | Metadados e orientação institucional sobre educação; não lei universal nem estudo causal. |
| `agentskills2026` | [Agent Skills Specification](https://agentskills.io/specification), consulta 04-11-2026 | Formato, frontmatter, limites e divulgação progressiva. Não há instalação universal nem ativação garantida. |
| `autogen2023` | [AutoGen v2](https://arxiv.org/abs/2308.08155v2), DOI 10.48550/arXiv.2308.08155 | Metadados e resumo; padrão de arquitetura, não superioridade geral de equipas. |
| `a2a2026` | [A2A 1.0.0](https://a2a-protocol.org/v1.0.0/specification/) | Visão geral, estado de tarefa, `AgentSkill` e descoberta. Confirmado `/.well-known/agent-card.json`. |
| `hu2022lora` | [LoRA v2](https://arxiv.org/abs/2106.09685v2), preprint 2021 / ICLR 2022 | Metadados e resumo; fórmula/contagens didáticas independentes, sem atribuir redução de parâmetros a memória total. |
| `dettmers2023` | [QLoRA, NeurIPS 2023](https://arxiv.org/abs/2305.14314) | Metadados e resumo com base congelada e adaptadores; não se importam percentagens comerciais de benchmark. |
| `hinton2015` | [Distilling the Knowledge](https://arxiv.org/abs/1503.02531), 2015 | Metadados e resumo; mecanismo de distilação, sem ganhos garantidos. |
| `brynjolfsson2025` | [QJE 140(2)](https://doi.org/10.1093/qje/qjae044), 889–942 | Abstract e IV.C (estratégia empírica). Artigo final: 5172 agentes e 15%; não misturar versões preliminares nem anunciar ensaio aleatório global. |
| `ilo2025` | [OIT WP 140](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) | Resumo metodológico e estimativa de exposição; tarefas, entrada de especialistas e modelos, sem previsão de despedimentos. |
| `bastani2025` | [PNAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/), DOI 10.1073/pnas.2422633122 | Resumo, resultados e descrição da avaliação sem ferramenta; autoria reconfirmada no registo PubMed. Não se afirma dano universal. |
| `jumper2021` | [Nature 596, 583–589](https://www.nature.com/articles/s41586-021-03819-2) | Resumo e desenho CASP14, avaliação cega; estrutura prevista não demonstra eficácia terapêutica. |
| `who2024` | [Lançamento oficial OMS, 18-01-2024](https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models) | Benefícios/riscos e orientação. A página do catálogo ISBN apresenta 25-03-2025; a referência foi ajustada para citar explicitamente a notícia de lançamento de 2024, sem confundir as datas. |
| `fang2025` | [Página dos autores MIT](https://www.media.mit.edu/publications/how-ai-and-human-behaviors-shape-psychosocial-effects-of-chatbot-use-a-longitudinal-controlled-study/) | Resumo revisto: condições experimentais sem efeitos significativos reportados; associação com uso voluntário não aleatorizado. Resumos antigos diferem; não foram fundidos. |
| `iea2025` | [IEA Energy and AI](https://www.iea.org/reports/energy-and-ai), 10-04-2025 | Procura de eletricidade, estimativa de 2024; âmbito inclui centros de dados, não apenas IA. |
| `iea2026` | [IEA Key Questions](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary), 16-04-2026 | Resumo executivo; crescimento de 2025, projeção central 2030 e limites físicos. Separados histórico e cenário. |
| `ha2018` | [World Models v4](https://arxiv.org/abs/1803.10122v4) | Metadados e resumo; representação e controlo em ambientes estudados. |
| `hafner2025` | [Nature / cópia primária em PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/), DOI 10.1038/s41586-025-08744-2 | Metadados/autoria e resumo; abertura direta de Nature limitada por redirecionamento. Sem percentagens de generalidade inventadas. |
| `butlin2023` | [Consciousness in AI v3](https://arxiv.org/abs/2308.08708v3) | Metadados e resumo; indicadores dependem de teorias. Conclusão de 2023 não é avaliação de todos os sistemas de 2026. |
| `metr2025` | [Relatório original METR](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf), julho de 2025 | Abstract e metodologia na página dos autores: 16 programadores, 246 tarefas, atribuição por tarefa e 19% de aumento do tempo. Não generalizar para todo o software ou modelos posteriores. |
| `graphcast2023` | [Science](https://doi.org/10.1126/science.adi2336) | Metadados e resumo; previsão meteorológica de médio prazo, sem concluir validade climática geral. |
| `rt22023` | [RT-2](https://arxiv.org/abs/2307.15818), 2023 | Metadados e resumo original; visão/linguagem/ação em avaliação delimitada. |
| `gu2023` | [Mamba v2](https://arxiv.org/abs/2312.00752v2) | Metadados/resumo, preprint de 2023 revisto em 2024; alternativa de arquitetura, sem proclamar substituição universal de Transformers. |

## Reconfirmação dirigida do enquadramento jurídico

Em 04-11-2026 foram reconfirmados no texto oficial indexado do EUR-Lex o ato 2026/1744, considerando 40, alteração do artigo 113 e artigo 4, e a consolidação do AI Act de 27-07-2026. Mantêm-se os marcos de 02-12-2027 e 02-08-2028 nos âmbitos delimitados no capítulo. Isto não é leitura integral de toda a legislação ou parecer de conformidade. O capítulo preserva a data e a proveniência da verificação de 03-11, agora acompanhadas desta reconfirmação.

## Segundo ciclo — narrativa, fundamentos e casos setoriais

Retoma em 04-11-2026 a partir de `e990b891`. Acrescentadas 14 entradas: a bibliografia passa de 73 para 87. A consulta abaixo foi dirigida aos elementos indicados; não se declara leitura integral ou reprodução experimental destes trabalhos. Os cálculos novos são próprios e sintéticos.

| Chave | Fonte primária e localizador | Alcance efetivamente verificado |
|---|---|---|
| `alpac1966` | [National Academies, DOI 10.17226/9547](https://www.nationalacademies.org/publications/9547), metadados e índice | Título, data, secções sobre custos, qualidade e tradução assistida. Recomendações completas não recuperadas; sem alegação de causalidade única sobre financiamento. |
| `rumelhart1986` | [Nature 323, 533–536](https://www.nature.com/articles/323533a0), metadados/resumo | Autoria, data, retropropagação e representações. Não reivindicar invenção sem antecedentes. |
| `krizhevsky2012` | [NeurIPS 25](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html), página e PDF original indexado | Arquitetura, treino e GPU. Resumo da página e PDF divergem em números; o texto não usa essas percentagens ou contagens. |
| `silver2016` | [Nature 529, 484–489](https://www.nature.com/articles/nature16961), resumo/metadados | Redes, aprendizagem, procura e vitória sobre campeão europeu; não confundir com encontro posterior de Lee Sedol. |
| `weizenbaum1966` | [ACM, DOI 10.1145/365153.365168](https://dl.acm.org/doi/10.1145/365153.365168), resumo/metadados | Palavras-chave e regras de decomposição/recomposição. Frase didática do livro é original, não transcrição histórica. |
| `mohanty2016` | [Frontiers, resumo e Results](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2016.01419/full) | 99,35% no conjunto controlado; 31,40% e 31,69% em pequenos conjuntos externos de 121 e 119 imagens. Não é estimativa de todas as explorações agrícolas. |
| `bergmann2019` | [CVPR 2019, 9592–9600](https://openaccess.thecvf.com/content_CVPR_2019/html/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.html), resumo/metadados | Treino com imagens sem defeito, teste com anomalias e anotações. Dataset de inspeção visual, não ensaio de manutenção temporal. |
| `eisemann2025` | [PRAIM, artigo em PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11922743/), resumo, desenho e competing interests | 463094 participantes; adoção voluntária, observacional. 6,7 vs 5,7 deteções por mil; financiamento e participação da Vara declarados. Sem conclusão de mortalidade. |
| `obermeyer2019` | [Science, DOI 10.1126/science.aax2342](https://doi.org/10.1126/science.aax2342), artigo primário disponibilizado por Berkeley | Resumo e descrição do alvo: custo como proxy de necessidade. Não se reproduz a análise. |
| `kestin2025` | [Scientific Reports 15, 17458, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/), Introduction/Results/Discussion | Curso com 194 alunos, duas aulas, condições alternadas e avaliação próxima. Registos por aula não são participantes independentes; não demonstra retenção universal. |
| `salvi2025` | [Nature Human Behaviour, DOI 10.1038/s41562-025-02194-6](https://www.nature.com/articles/s41562-025-02194-6), texto primário indexado | Desenho e Discussion: 900 participantes, debate estruturado; comparação direta de duas condições IA não significativa (p=0,07). Sem inferência sobre resultado eleitoral. |
| `chouldechova2017` | [arXiv 1703.00056](https://arxiv.org/abs/1703.00056), resumo/metadados | Conflito de critérios de equidade sob diferenças de prevalência; sem escolha normativa automática. |
| `unctad2025` | [Relatório oficial](https://unctad.org/publication/technology-and-innovation-report-2025), página e registo DOI 10.18356/9789211068016 | Estrutura e orientação de política para capacidades/acesso; não evidência causal de cada recomendação. |
| `henderson2020` | [JMLR 21(248), 1–43](https://www.jmlr.org/papers/v21/20-312.html), resumo, secções 3.1, 4.3 e limitações no PDF | Contabilização, PUE e fronteiras de telemetria. Exemplo numérico do livro é construído, sem medição elétrica real. |

## Terceiro ciclo — serviço público e formatos de dados

Em 05-11-2026, o caso SyRI foi verificado no texto da decisão de 5 de fevereiro de 2020. A página oficial do original neerlandês foi consultada por indexação. Para ler os parágrafos numerados, usou-se uma reprodução do texto da tradução do tribunal.

| Chave | Fonte primária e localizador | Alcance efetivamente verificado |
|---|---|---|
| `syri2020` | [Decisão neerlandesa ECLI:NL:RBDHA:2020:865](https://uitspraken.rechtspraak.nl/details?id=ECLI%3ANL%3ARBDHA%3A2020%3A865), [texto inglês ECLI:NL:RBDHA:2020:1878](https://www.uitspraken.nl/uitspraak/rechtbank-den-haag/civiel-recht/civiel-recht-overig/bodemzaak/ecli-nl-rbdha-2020-1878) e [comunicado do tribunal](https://www.rechtspraak.nl/organisatie-en-contact/organisatie/rechtbanken/rechtbank-den-haag/nieuws/2020/02/syri-wetgeving-in-strijd-met-het-europees-verdrag-voor-de-rechten-voor-de-mens) | §§ 4.27–4.29 e 6.62, cruzamento e análise. §§ 6.49, 6.54–6.60, 6.80 e 6.106, transparência, relatório de risco e proporcionalidade. § 7.2, dispositivo e alcance. O capítulo distingue a sinalização da decisão sancionatória e a questão do artigo 22.º do RGPD do fundamento decidido. |
| `rfc8259` | [IETF RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html), §§ 3, 4 e 6 | Literais JSON, recomendação de nomes únicos e exclusão de NaN e infinitos. |
| `pythonjson312` | [Documentação Python 3.12](https://docs.python.org/3.12/library/json.html#standard-compliance-and-interoperability), conformidade e opções de descodificação | Comportamento por omissão de NaN e repetição de nomes. Verificado localmente em Python 3.12.14 que a chave repetida conserva o último valor e que `json.loads('NaN')` devolve NaN. |

O terceiro ciclo reconfirmou em 05-11-2026 o [Regulamento (UE) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj), considerando 40, alteração do artigo 113 e artigo 4. Os marcos de dezembro de 2027 e agosto de 2028 mantêm o âmbito descrito no capítulo de governação. A revisão de segurança consultou [OWASP LLM01](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) e [LLM07](https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/) para origem das instruções, credenciais e autorização no executor.

No lote de mecanismos, reconfirmou-se no [resumo do relatório técnico GPT-4 de 2023](https://arxiv.org/abs/2303.08774) a entrada de imagem e texto com saída de texto. A descrição refere-se à versão documentada. As contas de probabilidades condicionais, temperatura e comprimento Unicode são exemplos construídos e conferidos em Python.

## Quarto ciclo — escrita, aprendizagem e verificação de dados

Consulta de 05-11-2026. Os resultados sintéticos e as consultas executadas abaixo servem para explicar o método.

| Chave | Fonte primária e localizador | Alcance conferido |
|---|---|---|
| `sadasivan2023` | [Preprint v4, resumo e revisão](https://arxiv.org/abs/2303.11156v4) | Parafrasear os trechos do estudo reduziu a deteção em vários esquemas. A afirmação refere-se aos detetores e textos avaliados. |
| `roedigerkarpicke2006` | [Resumo do artigo no PubMed](https://pubmed.ncbi.nlm.nih.gov/16507066/), resultados a 5 min e com atraso | Dois ensaios com textos em prosa. A releitura teve vantagem imediata e os testes de evocação favoreceram retenção nos prazos mais longos estudados. |
| `bastani2025` | [Artigo PNAS](https://doi.org/10.1073/pnas.2422633122), resumo e resultados do exame sem assistência | Cerca de 17% de diferença relativa para GPT Base face ao controlo. O desenho do tutor mitigou a diferença. A [correção](https://pmc.ncbi.nlm.nih.gov/articles/PMC12403119/) foi publicada para uma afiliação. |
| `doshi2024` | [Artigo Science Advances](https://doi.org/10.1126/sciadv.adn5290), método e figuras 2 e 4 | 293 participantes escreveram histórias curtas. Avaliações de novidade e proximidade à média das outras histórias dentro da condição são medidas distintas. |
| `prisma2020` | [Artigo BMJ](https://www.bmj.com/content/372/bmj.n71), resumo e finalidade | Orientação para reportar revisões sistemáticas. |
| `sqliteagregados2026` | [Agregados](https://sqlite.org/lang_aggfunc.html) e [EXISTS](https://sqlite.org/lang_expr.html#the_exists_operator), SQLite | Execução da listagem do livro em SQLite 3.53.1. A junção produz 3 linhas, soma 90 e soma distinta 30. A consulta por pedido com existência de artigo produz 2 pedidos e soma 60. |

O exemplo da média do capítulo de programação executou as quatro verificações, incluindo a preservação do zero. As contas de percentagens e tempo da aprendizagem e de proporção entre respondentes também foram verificadas localmente.

### Construção e interoperabilidade

- [MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) e [versionamento](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning) consultados em 05-11-2026. Reconfirmados metadados por pedido e remoção do handshake anterior. A [autorização](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) distingue destinatário do token e serviços a montante.
- [A2A 1.0.0](https://a2a-protocol.org/v1.0.0/specification/), secções 4.2.3, 4.4.1, 4.4.5 e 8.2. Confirmados campo «skills», tipo «AgentSkill», estado de pedido de informação e caminho de descoberta. Verificar artefacto e titularidade é um critério do exemplo de negócio.
- [ReAct, resumo do preprint dos autores](https://arxiv.org/abs/2210.03629). Intercalação de passos de raciocínio textual e ações. O capítulo apresenta a escolha de arquitetura como hipótese de projeto.
- Executadas quatro consultas locais da Lavandaria e os 30 testes desse módulo. Verificados os resultados de A e B, a equivalência das duas recusas e as contas didáticas de RRF e recall@2. Os resultados são do núcleo offline. Conformidade MCP e A2A pede uma integração própria.

### Futuros e comparação

- [Ha e Schmidhuber, World Models v4](https://arxiv.org/abs/1803.10122v4) e [Hafner et al., Dreamer](https://www.nature.com/articles/s41586-025-08744-2), resumo e figura 1. Confirmadas representações aprendidas e, em Dreamer, trajetórias previstas pelo modelo para aprendizagem do agente. As dez tentativas do robô são um exemplo sintético de denominadores, não medições dos artigos.
- [Butlin et al., v3](https://arxiv.org/abs/2308.08708v3), resumo e âmbito. Indicadores computacionais derivados das teorias discutidas. A conclusão não foi estendida a sistemas posteriores.
- Registo offline de 04-11-2026 repetido com o comando do livro. Os três modos falharam E1 e E2 e acertaram E3 e E4. A métrica derivada de chamadas de componentes por acerto deu 2, 2 e 6. O ramo de fluxo offline usa o mesmo stub e ramo de chamada única. O piloto com LLM mantém zero inferências novas.

## Recursos e licenças

Texto novo, diagrama de equipa, tabelas, dados sintéticos e scripts foram produzidos para esta revisão sob as condições da obra. Capa original preservada byte a byte. Não se copiaram figuras dos estudos ou modelos; os artigos são citados e resumidos com alcance limitado. Os laboratórios de software usam a biblioteca padrão de Python. A montagem do ateliê usa também Pillow, ReportLab, Inkscape e FFmpeg. A origem da ilustração, o pedido utilizado e as licenças tipográficas estão em `exemplos/atelier`. Modelos e runtime mantêm as licenças indicadas no registo histórico; os pesos não são redistribuídos. O pacote SKILL.md não recebe uma licença comercial diferente da obra.
