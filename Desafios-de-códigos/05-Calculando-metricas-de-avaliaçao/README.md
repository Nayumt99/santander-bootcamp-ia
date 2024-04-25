# Calculadora de Desempenho de Modelos de Machine Learning

Este é um script Python que permite calcular o desempenho de modelos de Machine Learning com base em matrizes de confusão. Ele determina a matriz de confusão com o melhor desempenho em termos de acurácia e precisão.

## Requisitos

Python 3.x

## Como Usar

1. Clone o repositório ou baixe o arquivo Calculando-metrica.py.
2. Execute o script Calculando-metrica.py.
3. Insira o número de matrizes de confusão a serem avaliadas.
4. Insira os valores das matrizes de confusão conforme solicitado.
5. O script calculará e imprimirá o índice, acurácia e precisão da matriz com o melhor desempenho.

## Exemplo de Uso

$ python Calculando-metrica.py
``
3
50,10,5,85
20,5,8,67
30,12,4,88
``

Saída:
````
Índice: 1
Acurácia: 0.9
Precisão: 0.83
````

##Funcionamento do Código

O script define uma função calcular_desempenho que recebe uma lista de matrizes de confusão como entrada e retorna o índice, acurácia e precisão da matriz com o melhor desempenho. Ele compara o desempenho das matrizes com base nas métricas de acurácia e precisão.
