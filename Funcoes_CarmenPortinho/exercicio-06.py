'''6. Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício'''

import random

def palavra_secreta():
    palavras = ['amor', 'codigo', 'python', 'mulheres', 'empoderamento']
    return random.choice(palavras).lower()  #seleciona palavra aleatoria e converte minúsculas

def exibir_palavra(palavra, letras_adivinhadas): # palavra secreta a
    return ' '.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])#cria lista de caracters

def jogo_forca():
    palavra = palavra_secreta()  # Obtém a palavra secreta em minúsculas
    letras_adivinhadas = set()# inicializa um conjunto vazio com elementos unicos
    tentativas_restantes = 6
    letras_erradas = set()

    print("Bem-vindo ao jogo da Forca!")
    print("Tente adivinhar a palavra.")

    while tentativas_restantes > 0:
        print("\n" + exibir_palavra(palavra, letras_adivinhadas))
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_adivinhadas or tentativa in letras_erradas:
            print("Você já tentou essa letra.")
        elif tentativa in palavra:
            letras_adivinhadas.add(tentativa)
            if set(palavra) <= letras_adivinhadas:
                print(f"Parabéns! Você adivinhou a palavra: {palavra}")
                break
        else:
            letras_erradas.add(tentativa)
            tentativas_restantes -= 1
            print("Letra incorreta.")

        if tentativas_restantes == 0:
            print(f"Você perdeu! A palavra era: {palavra}")

jogo_forca()
