"""
Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
"""

idade = int(input('Digite a sua idade: '))

if idade < 12:
    print('Você é uma criança!')
elif 12 <= idade <18:
    print('Você é adolescente')
elif 18 <= idade <60: 
    print('Você é um adulto!')
else: 
    print('Você é idoso!')