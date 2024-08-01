"""
O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
"""

pares = 0
impares = 0

numero = -1  
while numero != 0:
    numero = int(input('Digite um número (ou 0 para encerrar): '))
    
    if numero > 0:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    elif numero < 0:
        print('Por favor, insira apenas números positivos.')

print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')
