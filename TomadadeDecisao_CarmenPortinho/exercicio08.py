''' Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.'''

numero01 = int(input('Digite o primeiro número inteiro: '))
numero02 = int(input('Digite o segundo número inteiro: '))
numero03 = int(input('Digite o terceiro número inteiro: '))

if numero01 > numero02 and numero01 > numero03:
    print(f'O número {numero01} é o maior número entre os números digitados!')
if numero02 > numero01 and numero02 > numero03:
    print(f'O número {numero02} é o maior número entre os números digitados!')
else:
    print(f'O número {numero03} é o maior número entre os números digitados!')