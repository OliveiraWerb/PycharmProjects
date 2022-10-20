#7.Faça um programa que pergunte o preço de três produtos e informe qual produto
#você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print('Qual o preco do produto 1?')
p1 =float(input())
print('Qual o preco do produto 2?')
p2 =float(input())
print('Qual o preco do produto 3?')
p3 =float(input())


if p1 < p2 and p1 < p3:
    menorp = p1
elif p2 < p3:
    menorp = p2
else:
    menorp = p3

print('Voce deve comprar o produto de {}, pois ele e o mais barato.'.format(menorp))