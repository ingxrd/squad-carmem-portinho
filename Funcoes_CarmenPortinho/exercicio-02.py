''' 2 - Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721. '''

def reverter_numero(numero):
    return int(str(numero)[::-1])

numero_reverso = reverter_numero(127)
print(f'O número 127 revertido é: {numero_reverso}')