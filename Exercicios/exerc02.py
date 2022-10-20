#Lista de Exercicios 1

# 1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Olá mundo!')

# 2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

n1=input('Digite um numero:')
print('O numero digitado foi: ',n1)

#3.	Faça um Programa que peça dois números e imprima a soma.

print('Digite dois numeros: ')
n2=int(input())
n3=int(input())

print('A soma entre os dois é:', n2 + n3)

#4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Digite 4 numeros:')
n4=float(input())
n5=float(input())
n6=float(input())
n7=float(input())

media=(n4+n5+n6+n7)/4

print('A media dos numeros digitados é: ',media)


#5.Faça um Programa que converta metros para centímetros.

metro=float(input('Digite quantos metros:'))
centimetro=(metro*100)
print('Esse valor em cm é {}cm'.format(centimetro))

#6.	Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio=float(input('Digite o raio:',))
area=(math.pi*(raio**2))

print('A area do raio e: {}m quadrados'.format(area))

#7.Faça um Programa que pergunte quanto você ganha por hora
#e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoHora=float(input('Digite o ganho hora:'))
horasTrabalhadas=float(input('Digite as horas trabalhadas:'))
salario=float(input('Qual salario: '))
totalExtra=(ganhoHora*horasTrabalhadas)
print('O total do seu salario é:{}'.format(salario+totalExtra))

#8.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.    C = 5 * ((F-32) / 9).

grauFahr=float(input('Digite o grau F°: '))
grauCel=(5*((grauFahr-32)/9))

print('O grau em celsius e:',grauCel)

#9.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius=float(input('Digite o grau C°: '))
fahren=((celsius*1.8)+32)

print('O grau em fahrenheit e:',fahren)

#10.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre o produto do dobro do primeiro com metade do segundo.
#a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

n8=int(input('Digite um numero inteiro: '))
n9=int(input('Digite outro numero inteiro: '))
n10=float(input('Agora digite um numero real: '))

metadeSegundo=(n9/2)
dobroPrimeiro=(n8*2)
produto=(dobroPrimeiro*metadeSegundo)
triPrimeiro=float((n8*3)+n10)
print('O produto do dobro do primeiro com metade do segundo:', produto)
print('A soma do triplo do primeiro com o terceiro:', triPrimeiro)
print('O terceiro elevado ao cubo.:', n10 ** 3)

#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

altura=float(input('Digite a altura:'))
homens=((72.7*altura)-58)
mulheres=((62.1*altura)-44.7)

print('O peso ideal para homens e:{} e para mulheres e {}'.format(homens,mulheres))


#12.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que
# o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar
# uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
# quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

pesoPeixe=float(input('Peso do peixe: '))
excesso=(pesoPeixe-50)
multa=(4.00)
valorMulta=(4.00*excesso)

if (pesoPeixe > 50):
 print('Joao devera pagar um total de multas de: ', excesso*multa)
else:
 print('Joao nao pagara multa')


#13.	Faça um Programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.


