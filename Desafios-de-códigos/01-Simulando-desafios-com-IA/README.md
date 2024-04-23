# Análise de Sentimento

Este script em Python realiza uma análise básica de sentimento em texto inserido pelo usuário. Ele utiliza expressões regulares para tokenizar o texto de entrada e classificá-lo em sentimentos positivos, negativos ou neutros com base na ocorrência de palavras-chave específicas.

## Como Funciona

1. Texto de Entrada: O usuário fornece um comentário ou declaração em texto.
2. Tokenização: O texto de entrada é tokenizado em palavras individuais usando expressões regulares para remover pontuações e converter todas as palavras para minúsculas.
3. Classificação de Sentimento: O script contém listas predefinidas de palavras positivas, negativas e neutras. Ele conta as ocorrências de palavras positivas, negativas e neutras no texto de entrada.
4. Tomada de Decisão: Com base nas contagens de palavras positivas, negativas e neutras, o script determina o sentimento geral.
5. Saída: O script imprime o resultado da análise de sentimento: se o texto de entrada é classificado como positivo, negativo ou neutro.

## Palavras-Chave

* Palavras Positivas: "bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"

* Palavras Negativas: "ruim", "péssimo", "horrível", "terrível", "odeio"

* Palavras Neutras: "mas", "deixou", "apesar", "embora"

## Uso

1. Execute o script.
2. Insira um comentário ou declaração em texto quando solicitado.
3. O script analisará o sentimento do texto de entrada e imprimirá o resultado.

Exemplo
````
Sentimento: Positivo
````

## Observação

Esta análise de sentimento é básica e depende exclusivamente da correspondência de palavras-chave. Pode não capturar com precisão o sentimento em frases ou contextos complexos.

Você pode expandir as listas de palavras positivas, negativas e neutras para melhorar a precisão da análise de sentimento para seu caso de uso específico.

## Possíveis Futuras Melhorias

* Aprimoramento do Vocabulário: Expandir as listas de palavras positivas, negativas e neutras para incluir uma variedade mais ampla de termos, melhorando assim a precisão da análise de sentimento.

* Utilização de Modelos de Aprendizado de Máquina: Implementar algoritmos de aprendizado de máquina, como classificadores de sentimento baseados em modelos de linguagem pré-treinados, para uma análise mais sofisticada e contextualizada.

* Consideração de Contexto: Desenvolver métodos para considerar o contexto em que as palavras são usadas, levando em conta a estrutura gramatical e o significado das frases para uma análise mais precisa.

* Interface Gráfica do Usuário (GUI): Criar uma interface gráfica interativa para tornar a entrada de texto mais amigável e visualizar os resultados da análise de sentimento de forma mais intuitiva.

* Suporte a Múltiplos Idiomas: Expandir o script para suportar análise de sentimento em diferentes idiomas, adaptando as listas de palavras-chave e regras gramaticais conforme necessário.
