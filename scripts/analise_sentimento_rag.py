"""
Demonstração técnica: Classificador de Intenção com Fallback.
Este script exemplifica os conceitos de 'Groundedness' e 'Controlo Estocástico' 
abordados no Capítulo 15 do livro.
"""

def classificar_feedback(texto):
    # Simulação de categorias técnicas definidas no livro
    categorias = ["Dúvida Técnica", "Bug Report", "Sugestão", "Elogio"]
    
    # Lógica de "Prompting" simulada
    print(f"--- Processando Input: '{texto}' ---")
    
    # Simulação de uma resposta estruturada (JSON-like)
    if "erro" in texto.lower() or "crash" in texto.lower():
        return {"intent": "Bug Report", "confidence": 0.98, "needs_human": True}
    elif "como" in texto.lower() or "?" in texto.lower():
        return {"intent": "Dúvida Técnica", "confidence": 0.85, "needs_human": False}
    else:
        return {"intent": "Indeterminado", "confidence": 0.0, "needs_human": True}

if __name__ == "__main__":
    casos = [
        "O sistema dá erro 500 ao abrir o PDF.",
        "Como posso mudar a temperatura do modelo no prompt?",
        "Gostei muito do design."
    ]
    
    for caso in casos:
        resultado = classificar_feedback(caso)
        print(f"Resultado: {resultado}")