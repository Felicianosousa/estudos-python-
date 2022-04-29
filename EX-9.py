#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
F=float(input('Digite a temperatura em graus Fahrenheit para converrtemos para Celsius:'))
C = 5 * ((F-32) / 9)
print(f'{F}ºF é equivalente a {C:.2f}ºC')