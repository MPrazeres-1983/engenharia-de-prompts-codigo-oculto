# Lavandaria das Meias Desaparecidas

Caso fictício da segunda edição. Python **3.10+**, apenas biblioteca padrão. Sem rede, chaves, custos de API ou dados reais. Pesquisa lexical + templates; **não executa um LLM nem implementa MCP**.

Na raiz do repositório:

```bash
python3 -m exemplos.lavandaria --cliente cliente-A --pergunta "Faltam duas meias."
python3 -m exemplos.lavandaria --cliente cliente-A --pergunta "Estado LAV-001"
python3 -m exemplos.lavandaria --cliente cliente-A --pergunta "Estado LAV-002"
python3 -m exemplos.lavandaria --cliente cliente-A --pergunta "Qual o prazo?" --exportar-contexto
python3 -m exemplos.lavandaria.avaliar
python3 -m unittest discover -s tests -v
```

`--cliente` escolhe um papel fictício; não autentica ninguém. Numa integração, a identidade tem de vir da autenticação da aplicação e nunca de texto ou argumentos propostos pelo modelo. O contexto exportado conserva o pedido original como dados e contém apenas fontes autorizadas. Uma alegação no pedido não muda a identidade.

## Contrato e critérios

`contrato.schema.json` descreve a saída. `validar_saida` implementa as regras deste contrato fixo e verifica que os excertos constam das fontes autorizadas; não é um motor genérico de JSON Schema nem um verificador lógico de todas as frases. Nenhuma confiança probabilística é fabricada.

| Critério | Verificação |
|---|---|
| CA-01 | Peças em falta: pedir talão sem inventar causa. |
| CA-02 | Cada cliente consulta o seu registo. |
| CA-03 | Acesso cruzado negado no executor; mesma mensagem para ID inexistente. |
| CA-04 | Ausência de prazo não se transforma numa garantia. |
| CA-05 | Campos extra, tipos errados e troca de ID rejeitados. |
| CA-06 | Fontes inventadas, excertos falsos ou vazios rejeitados. |

A classificação é uma baseline de palavras-chave, com prioridade: estado, prazo/compensação, peças em falta, outro. Dois IDs distintos, ID ausente numa consulta de estado, entrada vazia ou mais de 2000 caracteres encaminham. Os 12 casos em `dados/casos_avaliacao.json` são regressões conhecidas; não são um teste reservado de generalização. O cálculo de Wilson para 8/10 é um exemplo matemático separado e não é aplicado à suite como estimativa de tráfego real.

## Ligar um modelo real

`responder` aceita uma função `gerador(Contexto) -> dict`. O adaptador recebe apenas o contexto autorizado e deve devolver a proposta estruturada, sem executar ações. A aplicação mantém validação e autorização. Antes de o usar, implementar a API e versão escolhidas, parsing estrito, recusa, timeout e limites. Testar primeiro com dados fictícios e registar execução/versão/configuração. Nenhuma chamada real de modelo foi executada para produzir os resultados desta revisão.

Não existe um servidor MCP neste pacote. Para o acrescentar, escolher um SDK compatível com a especificação usada, implementar transporte/autenticação e acrescentar testes de protocolo. O executor de domínio mantém as suas barreiras.

Limites deliberados: sem escrita, reembolsos, envio de mensagens, base de dados persistente, autenticação real ou aprendizagem semântica. Os testes de injeção verificam a autorização do executor; não demonstram resistência de um LLM a ataques.
