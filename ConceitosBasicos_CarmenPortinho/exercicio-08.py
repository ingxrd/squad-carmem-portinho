'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''

valor_hora = float(input('Informe o valor da sua hora de trabalho: '))

horas_trabalhadas = int(input('Informe quantas horas trabalhou: '))

salario = valor_hora * horas_trabalhadas

print(f'Você trabalhou {horas_trabalhadas} horas a R${valor_hora:.2f} cada hora, portanto seu salário é de R${salario:.2f}.')