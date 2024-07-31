'''
4. Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
'''

nota = float(input("Digite a nota do aluno (de 0 a 10): "))

if 0 <= nota <= 10:
    if nota >= 7:
        print("O aluno está aprovado.")
    else:
        print("O aluno está reprovado.")
else:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")