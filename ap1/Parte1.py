import math

#1.Faça um Programa que pergunte quanto você ganha por hora e
# o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhohr = float(input('Quanto voce ganha por hora?: '))
hrtrabalhada = float(input('Quantas horas foram trabalhadas?: '))
total = ganhohr * hrtrabalhada
print('O total do seu salário será:R$ {}'.format(total))
print('\n____________________________________________')
#2.Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.    C = 5 * ((F-32) / 9).

grauf = float(input('Quantos graus Fahrenheit?: '))
celsius = 5 * ((grauf-32) / 9)
print('A temperatura em Celsius será: {}.'.format(celsius))
print('\n____________________________________________')
#3.Faça um Programa que peça a temperatura em graus Celsius,
#transforme e mostre em graus Fahrenheit.

grauc = float(input('Quantos graus Celsius?: '))
fahren = (grauc * 1.8) + 32
print('A temperatura em Fahrenheit será: {}.'.format(fahren))
print('\n____________________________________________')
#4.Faça um Programa que peça 2 números inteiros e um número real.
#Calcule e mostre o produto do dobro do primeiro com metade do segundo.
#A soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n8 = int(input('Digite um numero inteiro: '))
n9 = int(input('Digite outro numero inteiro: '))
n10 = float(input('Agora digite um numero real: '))

metadeSegundo = (n9/2)
dobroPrimeiro = (n8*2)
produto = (dobroPrimeiro*metadeSegundo)
triPrimeiro=float((n8*3)+n10)
print('O produto do dobro do primeiro com metade do segundo:', produto)
print('A soma do triplo do primeiro com o terceiro:', triPrimeiro)
print('O terceiro elevado ao cubo.:', n10 ** 3)
print('\n____________________________________________')
#5. Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite a altura:'))
homens = (72.7*altura)-58
mulheres = (62.1*altura)-44.7
print('O peso ideal para homens e: {}, e para mulheres e: {}.'.format(homens, mulheres))
print('\n____________________________________________')

#6. João Papo-de-Pescador, homem de bem, comprou um microcomputador
# para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido
# pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
# limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.


pesoPeixe = float(input('Peso do peixe: '))
excesso = (pesoPeixe-50)
multa = (4.00)
valorMulta = (4.00*excesso)

if (pesoPeixe > 50):
 print('Joao devera pagar um total de multas de: ', excesso*multa)
else:
 print('Joao nao pagara multa!')
print('\n____________________________________________')

#7. Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.

ganhohr2 = float(input('Quanto voce ganha por hora?: '))
hrtrabalhada2 = float(input('Quantas horas foram trabalhadas no mes?: '))
salbruto = (ganhohr2*hrtrabalhada2)
ir = (salbruto/100)*11
inss = (salbruto/100)*8
sind = (salbruto/100)*5
salliq = salbruto - inss - sind - ir
print('Seu Resumo de salario sera: \n'
      '+Salario Bruto R$ {}, \n'
      '-IR (11%): R$ {},\n'
      '-INSS (8%) : R$ {}, \n'
      '-Sindicato (5%): R$ {}, \n'
      '-Salario Liquido: {}.'.format(salbruto, ir, inss, sind, salliq))
print('\n____________________________________________')

#8.Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros
#quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

cober_tinta = 3
lata = 18
preco_lata = 80.0
tamanho = float(input('Qual tamanho da area a ser pintada em metros quadrados? :'))
litros = tamanho/cober_tinta
lata_inteira = int(litros/preco_lata)

if(litros%lata != 0):
    lata_inteira += 1

total = lata_inteira * preco_lata
print('Quantidade de litros necessarios, {} '. format(litros))
print('Quantidade de latas de tinta necessarias, {}'.format(lata_inteira))
print('Total da compra e R$ {}'.format(total))



