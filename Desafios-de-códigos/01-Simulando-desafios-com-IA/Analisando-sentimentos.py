import re

def analyze_sentiment():
    comentario = input()
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    elif count_positivo < count_negativo and count_neutro == 0:
        return "Negativo"
    else:
        return "Neutro"

sentimento = analyze_sentiment()
print("Sentimento:", sentimento)
