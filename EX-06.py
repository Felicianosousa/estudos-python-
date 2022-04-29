#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
pi=3.141592653589931
raio=float(input('Digite o raio do circulo para calcularmos sua area: '))
area=(raio**2)*pi

print(f'A area de um círculo com {raio} de raio é: {area:.2f}')