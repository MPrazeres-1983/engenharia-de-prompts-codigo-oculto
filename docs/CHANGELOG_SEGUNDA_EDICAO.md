# Registo de alterações — segunda edição

## 2026-11-03 — Auditoria

- Leitura integral do repositório e identificação da base `f63d417fb655c6af013569c5381235625e0567d1`.
- Branch independente `segunda-edicao-2026` criada a partir dessa base.
- Auditoria dos 23 capítulos, dois apêndices, 39 laboratórios e dois scripts.
- Plano de progressão, guia editorial e critérios de aceitação registados antes da intervenção no manuscrito.
- Mantida a capa original, a autoria e a licença CC BY-NC-SA 4.0.

## 2026-11-03 — Implementação editorial

`src/livro.tex` passou a coordenar o preâmbulo e capítulos separados. Mantêm-se classe book, A4, fontes Latin Modern, caixas monocromáticas, capa original, autoria e licença. A capa foi preservada byte a byte. A data editorial é fixa; a revisão compilada pode receber o SHA do commit por `src/revisao.tex`, gerado e ignorado pelo Git.

| Capítulo novo | Origem | Alteração efetiva |
|---|---|---|
| 1. IA, Aprendizagem e Modelos | Novo | Introdução sem programação; IA/ML/deep learning, treino/inferência e aplicação/modelo. |
| 2. A Primeira Conversa | Novo | Prompt progressivo, critérios e primeira etapa fictícia da Lavandaria. |
| 3. Mentalidade | Original 4 | Contrato imperfeito, ciclo de teste e remoção de promessas retóricas de superioridade. |
| 4. Contexto | Original 6 | Pesos fixos, exemplos reservados e comparação sem indicar a resposta numa condição. |
| 5. Personas | Original 5 | Hierarquia por plataforma, autoridade e limites de vozes simuladas. |
| 6. Desligar a Magia | Original 1 | Escopo autoregressivo, conhecimento paramétrico e pós-treino; alucinações sem explicação reducionista. |
| 7. Transformer | Original 2 | Vetores, atenção escalada/máscara/dimensões, exemplo numérico, treino/geração e diagrama TikZ. |
| 8. Tokens | Original 3 | Logits, softmax/temperatura, top-p e ausência de garantia de determinismo; estilo não é parâmetro. |
| 9. Multimodalidade | Original 21 | Antecipado; modalidades não exigem pipeline textual; maquete raster não é gráfico de dados. |
| 10. Raciocínio | Original 7 | Reescrita científica de CoT/ToT/self-consistency e modelos de raciocínio; três labs equivalentes conservados. |
| 11. Autocorreção | Original 8 | Feedback externo, ferramenta estreita, execução e paragem fora do prompt. |
| 12. Escrita | Original 9 | Ritmo editorial sem certificado de autoria por perplexidade/burstiness. |
| 13. Estudo | Original 13 | Heurística 80/20 sem garantia de nota; aprendizagem sem equiparar desconforto a progresso. |
| 14. Negócios | Original 14 | Rascunho/envio, compromissos e responsabilidade; detetores não provam autoria. |
| 15. Criatividade | Original 15 | Restrições e comparação como práticas, sem percentagens ou vitórias universais inventadas. |
| 16. Investigação | Original 16 | Ficha de evidência e limite de leitura de abstracts. |
| 17. Texto→dados | Original 11 | Instâncias JSON válidas, esquema separado, confiança não calibrada, três níveis de validação. |
| 18. Análise | Original 12 | SQL autorizado, período/join/nulos e normalização determinística por código. |
| 19. Software | Original 10 | Vibe coding enquadrado, isolamento, diff e testes com oráculo independente. |
| 20. Spec-First | Novo | Especificação, CA-01…06 e rastreabilidade de implementação/testes. |
| 21. RAG | Novo | Indexação, chunks, lexical/vetorial/híbrida, RRF, permissões, abstinência e avaliação separada. |
| 22. Ferramentas/MCP | Novo | Contrato/executor, versão 2026-07-28 e fronteiras de confiança; exemplo não finge ser servidor. |
| 23. Agentes | Original 17 | Sem percentagens retóricas; estado, memória, orçamento e idempotência. |
| 24. Lavandaria | Novo | Sistema executável offline com limites e substituição do gerador. |
| 25. Avaliação | Original 18 | Precisão/sensibilidade, cobertura, Wilson, teste reservado e enviesamento do juiz; diagrama. |
| 26. Segurança | Original 20 | OWASP 2025, autorização externa e novo laboratório de injeção. |
| 27. LLMOps | Original 19 | Custo por tarefa, percentis, cache autorizada e minimização/pseudonimização. |
| 28. Governação | Novo | RGPD/AI Act/NIST, disposições oficiais e calendário alterado pelo Regulamento (UE) 2026/1744; alcance documental declarado. |
| 29. Futuro | Original 22 | Separação de cenários e garantias; competências sem promessas de segurança de emprego. |
| A. Padrões | Original 23 | Movido para consulta; JSON corrigido e terminologia harmonizada. |
| B. Glossário | Original A | Acrescentados catorze termos; definições de temperatura/RAG revistas. |
| C. Leitura de fontes + bibliografia | Original B | Orientação mantida; referências vagas convertidas em 41 entradas concretas, incluindo as três acrescentadas no fecho. |

### Cortes e substituições justificados

- Retiradas fórmulas em texto simples ilegível, confiança fictícia, JSON inválido e percentagens retóricas sem origem. O conceito útil foi reexplicado, não apenas apagado.
- Reescrito o capítulo de raciocínio porque corrigir frases isoladas deixaria um enquadramento incoerente sobre processos internos, ToT e amostras independentes. Os três objetivos de laboratório mantêm-se.
- Retiradas listas vagas de «blogs», «cursos» e «iniciativas regulatórias» do apêndice de referências, substituídas por identificadores verificáveis e protocolo de leitura. Goodfellow, Jurafsky e os artigos históricos mantêm-se.
- O índice mostra secções, sem todos os subtítulos, para evitar que navegação ocupe espaço desproporcionado. O conteúdo permanece acessível no texto.
- `verbatim` passou a `listings` com acentos e quebras de linha; os 39 labs originais foram revistos e há oito novos (47 no total).

## 2026-11-03 — Exemplos, compilação e revisão

- Exemplo local da Lavandaria, contrato, fontes e registos fictícios, pesquisa lexical, consulta autorizada, gerador substituível e avaliação determinística.
- 30 testes com casos positivos/negativos, acesso cruzado, injeção no documento, contratos inválidos, evidência e limites; 12 regressões conhecidas separadas de qualquer alegação de generalização.
- Scripts históricos identificados como heurísticas; retirados resultados constantes apresentados como extração e confiança probabilística inventada.
- Validador de estrutura editorial, referências/citações, instâncias JSON e avisos de compilação.
- Actions adaptada para push e pull request, testes, BibTeX, SHA no PDF e artefactos de evidência. Removida publicação automática de release deste fluxo de revisão; não foi criada qualquer tag.
- Inspeção visual de todas as páginas em miniaturas e amostra ampliada de fórmulas, diagramas, tabelas, laboratórios, índice e bibliografia. Corrigida proximidade de texto no esquema do Transformer e avisos de largura/glossário.

O relatório `VALIDACAO_SEGUNDA_EDICAO.md` identifica as execuções concretas e as questões humanas. A decisão posterior do autor de terminar e fazer merge está registada na secção de fecho abaixo.

## 2026-11-03 — Fecho autorizado pelo autor

- O autor pediu expressamente para terminar o trabalho pendente e fazer merge do PR #1; mantém-se a branch existente.
- Verificação documental dos artigos jurídicos citados: RGPD e artigo 113 do AI Act, com Regulamento (UE) 2026/1744. Registados localizadores e alcance do acesso.
- Consulta dos métodos originais de CoT, self-consistency, ToT e autocorreção intrínseca; nenhuma reprodução de estudos é alegada.
- Revisão editorial dos percursos inicial e técnico. Corrigidas a obrigatoriedade contraditória da persona, a alegação universal sobre exemplos e imprecisões entre embedding inicial, representação contextual e metáfora geométrica.
- 52 inferências locais com Qwen2.5-0.5B-Instruct Q4_K_M e llama.cpp b11960; prompts, respostas, hashes e avaliação guardados. O capítulo 25 inclui contagens e um erro factual que passou o contrato. Não se afinou o prompt sobre os resultados.
- Atualizadas nota de edição, documentação e distinção entre demonstração offline e ensaio real. Não houve estudo com leitores humanos independentes nem parecer jurídico profissional.
- Critério de integração: testes e compilação final sem erros, inspeção do PDF e CI bem-sucedida antes de marcar o PR pronto e fazer merge. O PR regista o SHA e as execuções finais. Nenhuma tag ou release é criada por este fecho.
