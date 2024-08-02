"""
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
"""

horas_por_semana = float(input('Digite o número de horas de exercício físico por semana: '))

minutos_por_mes = horas_por_semana * 60 * 4

# Calcular o total de calorias queimadas em um mês (considerando 5 calorias por minuto)
calorias_por_minuto = 5
total_calorias_queimadas = minutos_por_mes * calorias_por_minuto

print(f'Total de calorias queimadas em um mês: {total_calorias_queimadas} kcal')