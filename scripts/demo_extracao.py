import json

def extrair_dados_prompt(texto_bruto):
    # Simulação de uma lógica que explicaste no capítulo de ETL
    print(f"A analisar texto: {texto_bruto[:50]}...")
    # Exemplo de output que o teu livro ensina a obter
    resultado = {
        "status": "sucesso",
        "classe": "suporte_tecnico",
        "urgencia": "alta"
    }
    return json.dumps(resultado, indent=4)

if __name__ == "__main__":
    exemplo = "O meu acesso ao servidor crashou quando tentei fazer o push."
    print(extrair_dados_prompt(exemplo))