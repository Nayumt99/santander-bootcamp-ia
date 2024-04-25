def calcular_desempenho(matrizes):
    melhor_indice = 0
    melhor_acuracia = 0
    melhor_precisao = 0

    for i, matriz in enumerate(matrizes):
        vp, fp, fn, vn = matriz
        acuracia = (vp + vn) / (vp + fp + fn + vn)
        precisao = vp / (vp + fp)

        if acuracia > melhor_acuracia or (acuracia == melhor_acuracia and precisao > melhor_precisao):
            melhor_indice = i + 1
            melhor_acuracia = acuracia
            melhor_precisao = precisao

    return melhor_indice, round(melhor_acuracia, 2), round(melhor_precisao, 2)

# Função para ler as matrizes de confusão
def ler_matrizes():
    num_matrizes = int(input())
    matrizes = []

    for _ in range(num_matrizes):
        matriz = list(map(int, input().split(',')))
        matrizes.append(matriz)

    return matrizes

# Exemplo de uso
entrada = ler_matrizes()
indice, acuracia, precisao = calcular_desempenho(entrada)
print(f"Índice: {indice}")
print(f"Acurácia: {acuracia}")
print(f"Precisão: {precisao}")
