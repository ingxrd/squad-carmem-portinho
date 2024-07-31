'''Faça um programa que lê três números inteiros e os mostra em ordem
crescente.'''

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))


if num1 > num2:
    num1, num2 = num2, num1  # Troca os valores se num1 for maior que num2

if num1 > num3:
    num1, num3 = num3, num1  # Troca os valores se num1 for maior que num3

if num2 > num3:
    num2, num3 = num3, num2  # Troca os valores se num2 for maior que num3
    
print("Os números digitados em ordem crescente são:", num1, num2, num3)    


''' Ou podemos utilizar listas e a função sorted.

# Lê os três números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Cria uma lista com os números
numeros = [num1, num2, num3]

# Ordena a lista em ordem crescente
numeros_ordenados = sorted(numeros)

# Imprime os números ordenados
print("Os números em ordem crescente são:", numeros_ordenados)'''