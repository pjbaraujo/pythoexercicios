"""
ex004
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo
e todas as informações possiveis sobre ela
"""
a = input('Digite algo: ')

print('O tipo primitivo desse valor é ',type(a))
print('Só tem espaço: ', a.isspace())
print('É um número: ', a.isnumeric())
print('É alfabetico: ', a.isalpha())
print('É alfanumerico: ', a.isalnum())
print('EStá em maisculo', a.isupper())
print('Está em minuscolo', a.islower())
print('Está capitalizada: ', a.istitle())