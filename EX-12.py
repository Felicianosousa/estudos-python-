#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 5

altura=float(input('Digite a altura da pessoa para calcularmos eu peso. \n altura: '))
peso=(72.7*altura)-5

print(f'O peso de uma pessoa com {altura}m é : {peso:.2f}Kg')