# Auditoria editorial e técnica — segunda edição

Data da leitura integral: **3 de novembro de 2026**. Base: `main` em `f63d417fb655c6af013569c5381235625e0567d1` (19-02-2026). Foram lidos os oito ficheiros do repositório: manuscrito, capa, README, licença, configuração de compilação, exclusões Git e dois scripts. O manuscrito tem 6934 linhas, 23 capítulos, dois apêndices e 39 Prompt Labs. A contagem bruta de 30084 palavras inclui comandos LaTeX e código; não é uma contagem editorial de prosa.

## Diagnóstico

A voz direta, o humor seco, os exemplos profissionais e a distinção entre modelo e sistema constituem a identidade que vale a pena conservar. A cobertura de aplicações é ampla. A principal fragilidade não é a dimensão: é a distância entre a segurança do tom e a evidência apresentada. A matemática surge antes de uma primeira experiência acessível; algumas analogias são apresentadas como mecanismos; faltam referências verificáveis junto das afirmações.

Prioridades: **P0** = erro técnico ou exemplo enganador; **P1** = lacuna relevante, segurança ou progressão; **P2** = composição, linguagem e manutenção. Estas prioridades descrevem a versão original. A execução e as verificações finais estão no changelog e no relatório de validação.

## Avaliação integral por capítulo original

| Original | Intervenção | Prioridade | Diagnóstico e decisão |
|---|---|---|---|
| 1. Desligar a Magia | Corrigir, Mover | P0 | Boa abertura de tom, inadequada como primeiro contacto. «Não sabe coisas» e «apenas soa bem» confundem objetivo de treino com capacidades; negar qualquer treino de abstinência é incorreto. Explicitar escopo autoregressivo, conhecimento paramétrico, pré-treino e pós-treino; probabilidades do rato são ilustrativas. Colocar depois dos primeiros exercícios. |
| 2. Dentro da Máquina | Corrigir, Expandir, Mover | P0 | Vetor e fórmula de atenção estão em texto simples e matematicamente ilegíveis. Falta máscara causal, posições, feed-forward e distinção entre embedding inicial e representação contextual. O exercício de ordem não demonstra um mecanismo interno. Inserir fórmula correta, dimensões, exemplo numérico e diagrama editável. |
| 3. Tokens e Temperatura | Corrigir, Atualizar | P0 | Bom foco em limitações. «Equivalente a baixar temperatura» é falso; T=0 não garante reprodução integral de um serviço. Defaults numéricos não são universais. Explicar logits e amostragem; distinguir pedido estilístico, limite de geração e contagem validada. |
| 4. Mentalidade | Manter, Corrigir, Mover | P1 | Ciclo de teste útil e claro. A metáfora prompt=código precisa de limites: não existe semântica determinística garantida. Cortar promessas de superioridade, corrigir «refino/standardização» e apresentar como fundamento antes da álgebra. |
| 5. Personas | Manter, Corrigir | P1 | Exemplos reutilizáveis. Papéis e hierarquias variam por plataforma; persona não concede competência nem autoridade. Vozes simuladas não são especialistas independentes. Acrescentar fronteira de confiança e referência à documentação oficial. |
| 6. Contexto e Exemplos | Manter, Corrigir, Mover | P1 | Introdução prática forte. «Fine-tuning temporário» é uma analogia enganadora: os pesos ficam fixos. Ensaio de contexto estruturado mistura organização e indicação da resposta; separar variáveis e impedir contaminação dos conjuntos de avaliação. |
| 7. CoT e Família | Corrigir, Atualizar, Expandir | P0 | Não é demonstração de raciocínio interno fiel nem simples mudança de prompt em todos os modelos. Pedir três abordagens não implementa ToT; cinco soluções na mesma resposta não são amostras independentes. Reescrever com estudos originais, pós-treino de raciocínio, procura externa, custo e verificadores. |
| 8. Autocorreção | Manter, Corrigir | P1 | Protocolos úteis, mas sem evidência externa a revisão pode piorar. Distinguir crítica de redação, verificação factual e execução. «run_sql_query» demasiado amplo para exemplo de ferramenta. Introduzir validação no executor e limites impostos por código. |
| 9. Escrever Como um Humano | Manter, Corrigir | P0 | Conselhos de ritmo aproveitáveis. Perplexidade depende do modelo avaliador; burstiness não é certificado de autoria. Retirar diagnóstico estatístico de «texto IA», percentagens arbitrárias de reescrita e generalizações sobre detetores. |
| 10. Vibe Coding | Manter, Expandir | P1 | Bons padrões de leitura e revisão. Título não define vibe coding; faltam isolamento, versões e teste independente do código proposto. Acrescentar ponte para um capítulo Spec-First com critérios e rastreabilidade executáveis. |
| 11. Texto → Dados | Corrigir, Expandir | P0 | Esquema antes do prompt é uma boa base. Blocos apresentados como JSON usam `true/false` e intervalos inválidos; confiança declarada não é probabilidade calibrada. Distinguir JSON, JSON Schema, descodificação condicionada e validade semântica. |
| 12. Análise de Dados | Manter, Corrigir | P1 | Separação entre interpretação e cálculo é boa. Normalizar cabeçalhos por regras fixas contradiz a recomendação de código determinístico. Acrescentar controlo de acesso SQL, proteção contra duplicação em joins e definição do período temporal. |
| 13. Aprender com IA | Manter, Corrigir | P2 | Aplicações e exercícios acessíveis. 80/20 é heurística, não cobertura comprovada nem garantia de nota. Retirar «se nunca dói» como afirmação pedagógica, explicar recuperação ativa e validar respostas com materiais do curso. |
| 14. Negócios | Manter, Corrigir | P1 | Prompts concretos úteis. Evitar usar detetores como prova de autoria; distinguir rascunho de envio/compromisso externo. Base legal não se reduz a consentimento. Remeter para governação. |
| 15. Escrita Criativa | Manter, Corrigir | P2 | Material com identidade e valor prático. «Média de textos», 80/20 e «B ganha por KO» não são resultados demonstrados. Apresentar estratégias editoriais como hipóteses a comparar, sem percentagens fabricadas. |
| 16. Investigação | Manter, Expandir | P1 | Disciplina de fontes é boa. Abstracts não bastam para inferir desenho, robustez e limitações de um estudo. Acrescentar ficha de evidência com localizador, população/modelo, método, resultado e limite de generalização. |
| 17. Cadeias e Agentes | Manter, Corrigir, Expandir | P1 | Distingue fluxo fixo de escolha dinâmica. Falta RAG completo, memória persistente e efeitos de falhas parciais. Percentagem «10–20% da história» sem base. Remeter teoria RAG para capítulo próprio; acrescentar estado, orçamento e idempotência. |
| 18. Avaliação | Manter, Expandir | P1 | Golden sets e regressão são pontos fortes. Faltam separação desenvolvimento/teste, repetição, incerteza estatística, métricas de abstinência e enviesamentos do juiz. Inserir fórmulas, exemplo verificável e pipeline. |
| 19. LLMOps | Manter, Corrigir, Expandir | P1 | Boa cobertura operacional. Logs brutos e pseudonimização requerem distinção; consentimento não é sempre o fundamento. Cache deve respeitar autorização e versão dos documentos. Acrescentar custo por tarefa bem-sucedida e incidentes reproduzíveis. |
| 20. Segurança | Manter, Atualizar, Expandir | P1 | Identifica ameaças reais. Sanitização não remove garantidamente instruções maliciosas. Falta OWASP versionado, separação entre jailbreak e injeção indireta, autorização no servidor e teste negativo observável. |
| 21. Multimodal | Manter, Corrigir, Mover | P1 | Exemplos úteis; conceitos fundamentais chegam demasiado tarde. Arquitetura ASR→LLM→TTS é uma opção, não definição universal. Imagem raster «vectorial» e gráficos inventados precisam de enquadramento. Rever formulações legais de gravação. |
| 22. Futuro | Manter, Corrigir | P2 | Foco em fundamentos profissionais é útil. Afirmações sobre empregos, proximidade entre modelos e adoção são tendências/opiniões, sem garantia individual. Separar observação, cenário e escolha profissional; remeter direito para capítulo próprio. |
| 23. Biblioteca de Padrões | Manter, Corrigir, Mover | P2 | Boa referência de consulta, mas repete teoria. Mover para apêndice; corrigir modelos de JSON e remeter para capítulos em vez de reapresentar argumentos. |
| A. Glossário | Manter, Atualizar, Expandir | P1 | Faltam treino/inferência, MCP, Spec-First, grounding, calibração, memória e idempotência. Corrigir RAG como garantia de restrição a fontes. |
| B. Referências | Fundir, Atualizar | P1 | Autores genéricos e leituras sem identificadores não sustentam o texto. Converter em bibliografia BibTeX com títulos, anos e ligações; preservar a orientação de leitura num apêndice curto. |

## LaTeX e repositório

- Um único ficheiro com todo o conteúdo dificulta revisão por capítulo. Modularizar, preservando `src/livro.tex` como entrada.
- Identidade: classe `book`, A4, Latin Modern, caixas monocromáticas e capa original. Manter estes elementos; a imagem não deve ser redesenhada.
- Dependências originais: pdfLaTeX, Babel português, AMS, microtype, geometry, listings, csquotes, tcolorbox e cleveref. Acrescentar TikZ, tabelas e BibTeX/natbib; não introduzir Biber.
- A compilação local original parou inicialmente por ausência de `portuguese.ldf` no ambiente. Isto é uma dependência local, não prova de defeito no repositório. Depois de resolvida, guardar o diagnóstico separado dos erros do manuscrito.
- Muitos prompts estão em `verbatim`, sem quebra automática de linhas; migrar para listagens com acentos e quebras. Rever avisos de largura e inspecionar páginas.
- A data `\today` não identifica uma edição. Introduzir data editorial fixa e identificador de revisão no PDF de trabalho.
- Actions compila apenas em `push`. Acrescentar `pull_request`, testes offline, validação de referências e upload de log/PDF. Não criar tags nem publicar releases nesta tarefa.

## Scripts e demonstrações

`analise_sentimento_rag.py` faz pesquisa de palavras, não RAG nem inferência com LLM; os valores de confiança são constantes inventadas. `demo_extracao.py` devolve sempre o mesmo objeto. Conservar a intenção didática, identificar as simulações, remover confiança enganadora e fornecer uma implementação local com contrato, pesquisa lexical, permissões e testes. Nenhum resultado offline deve ser apresentado como avaliação de um LLM.

## Lacunas a preencher

Dois capítulos de entrada; RAG com pesquisa lexical/vetorial/híbrida, autorização, reranking e avaliação separada; ferramentas e MCP com versão; Spec-First e testes; caso transversal executável; AI Act/RGPD com data de verificação e distinção entre lei, norma voluntária e boa prática. Atualizar até à informação verificável em **03-11-2026**, sem presumir acontecimentos do resto do mês.
