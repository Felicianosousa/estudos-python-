#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A=o produto do dobro do primeiro com metade do segundo .
#B=a soma do triplo do primeiro com o terceiro.
#C=o terceiro elevado ao cubo.
n1=int(input('Digite um numero inteiro:'))
n2=int(input('Digite o segundo numero inteiro:'))
n3=float(input('Digite um numero real: '))

A=(n1*2)+(n2/2)
B=3*n1+n3
C=n3**3

print(f'o dobro de {n1} + a metade de {n2} é: {A:.2f}')
print(f'o triplo de {n1} +  {n3} é: {B:.2f}')
print(f'{n3} elevado ao cubo é: {C:.2f}')