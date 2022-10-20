import math

#Faça um programa que calcule o IMC de uma pessoa
#IMC = massa em kg / altura em metros elevado ao
#quadrado) e informe a sua classificação segundo a tabela a
#seguir, obtida na Wikipédia
#IMC Classificação.

#< 18,5) Abaixo do Peso
#[18,5 – 25) Saudável
#[25 – 30) Peso em excesso
#[30 – 35) Obesidade Grau I
#[35 – 40) Obesidade Grau II (severa)
#>= 40 Obesidade Grau III (mórbida)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / math.pow(altura, 2)

print('Seu imc é,',imc)

if imc <= 18.5:
    print('Abaixo do Peso')
elif imc > 18.5 and imc <= 25:
    print('Saudavel')
elif imc > 25 and imc <= 35:
    print('Obesidade Grau I')
elif imc > 35 and imc <= 40:
    print('Obesidade grau II (Severa)')
else:
    print('Obesidade Grau III (mórbida)')

#1.Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 < n2:
    maior = n2
else:
    maior = n1

print('O maior é,',maior)

#2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input('Digite um valor: '))

if valor < 0:
    print('O numero', valor,'e negativo.')
else:
    print('O numero', valor,'e positivo.')

#3.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')


if letra in "aeiou":
    print('A letra digitada "',letra,'"e vogal.')
else:
    print('A letra digitada "',letra,'" e consoante.')

#4.	Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:

#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if media < 7:
    print('A media do aluno é:', media,' Reprovado!')
elif media >= 7 and media == 9:
    print('A media do aluno é:', media, 'Aprovado!')
else:
    print('Aluno aprovado com distincao com a media: {}!'.format(media))

#5.Faça um Programa que leia três números e mostre o maior deles.

print('Digite tres numeros: ')
d1 = int(input())
d2 = int(input())
d3 = int(input())

if d1 > d2 and d1 > d3:
    print("O maior numero e {}!".format(d1))
elif d2 > d3:
    print("O maior é o {}!".format(d2))
else:
    print("O Maior é o {}!".format(d3))

#6.Faça um Programa que leia três números e mostre o maior e o menor deles.

print('Digite tres numeros: ')
m1 = int(input())
m2 = int(input())
m3 = int(input())

if m1 > m2 and m1 > m3:
    maior = m1
elif m2 > m3:
    maior = m2
else:
    maior = m3

if m1 < m2 and m1 < m3:
    menor = m1
elif m2 < m3:
    menor = m2
else:
    menor = m3

print("O Maior e {}, e o menor e {}.".format(maior, menor))

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
