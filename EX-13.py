#Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h=float(input("digite a altura da pessoa "))
sexo=input("digite o sexo da pessoa M ou F")

if sexo=='M':
    peso=(62.1*h)-44.7
else:
    peso=(72.7*h)*58
print(f'o peso para uma pessoa com {h}m e sexo {sexo} é: {peso}Kg')
