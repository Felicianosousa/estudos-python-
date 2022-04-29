#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
# mê
totalhoras=float(input("quantas horas voce trabalho no mes? "))
vlrhoras=float(input("qual o valor da sua hora? "))

saltotal=totalhoras*vlrhoras

print(f'O valor do salario é R$ {saltotal:.2f}')