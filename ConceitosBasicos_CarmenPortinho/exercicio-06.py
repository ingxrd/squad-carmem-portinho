'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''


velocidade_aviao =  600 
velocidade_carro = 100 
velocidade_onibus = 80 
kilometragem = float(input('Digite a distância em kilometros : '))

tempo_aviao =  kilometragem /velocidade_aviao
tempo_carro = kilometragem / velocidade_carro
tempo_onibus = kilometragem / velocidade_onibus

print(f'O tempo de viajem de avião é de { tempo_aviao:.2f} horas , de carro é de { tempo_carro:.2f} horas, de onibus é de {tempo_onibus:.2f} horas')