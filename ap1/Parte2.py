#9. Faça um Programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


metros = float(input("Informe os m²: "))
litros = metros/6
if(metros%108 > 0 and metros%21.6>0):
    latas = metros//108
    latas = latas + 1
    preçol = latas * 80
    galao = metros//21.6
    galao = galao + 1
    preçog = galao * 25
    print("Você vai precisar de: {} latas de 18L e vai gastar {} reais".format(latas,preçol))
else:
    latas = metros/108
    preçol = latas * 80
    galao = metros/21.6
    preçog = galao * 25
    print("Você vai precisar apenas de {} latas de 18L e vai gastar {} reais".format(latas,preçol))
    print("Você vai precisar apenas de {} galao de 3,6L e vai gastar {} reais".format(galao,preçog))


#10. Faça um programa que peça o tamanho de um arquivo para download (em MB)
#e a velocidade de um link de Internet (em Mbps), calcule e informe
#o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (MBps): '))
print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60))



#11.Faça um programa para o cálculo de uma folha de pagamento,
#sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para
#o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#Salário Bruto: (5 * 220)   : R$ 1100,00
#(-) IR (5%)                     	: R$   55,00
#(-) INSS ( 10%)                 : R$  110,00
#FGTS (11%)                     : R$  121,00
#Total de descontos         : R$  165,00
#Salário Liquido                : R$  935,00

valor_da_hora = float(input("Digite quanto você recebe por hora: "))
horas_trabalhadas = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
salario_bruto = valor_da_hora * horas_trabalhadas
if salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

IR = salario_bruto * (desconto_ir / 100)
INSS = salario_bruto * (10 / 100)
FGTS = salario_bruto * (11 / 100)
total_de_descontos = IR + INSS
salario_liquido = salario_bruto - total_de_descontos

print(
    f"\nSalário Bruto     : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${total_de_descontos:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
)


#12. Faça um Programa que leia um número
#e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
#se digitar outro valor deve aparecer valor inválido.

numero = input('Digite um numero: ')

if numero == 1:
    print ('1-Domingo')
elif numero == 2:
    print ('2-Segunda')
elif numero == 3:
    print ('3-Terça')
elif numero == 4:
    print ('4-Quarta')
elif numero == 5:
    print ('5-Quinta')
elif numero == 6:
    print ('6-Sexta')
elif numero == 7:
    print ('7-Sabádo')
else:
    print ('Intrada invalida')

#13.  Faça um programa que lê as duas notas parciais obtidas por um aluno
#disciplina ao longo de um semestre,
#e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

#Média de Aproveitamento Conceito
#Entre 9.0 e 10.0        A
#Entre 7.5 e 9.0         B
#Entre 6.0 e 7.5         C
#Entre 4.0 e 6.0         D
#Entre 4.0 e zero        E

#O algoritmo deve mostrar na tela as notas, a média,
#o conceito correspondente e a mensagem “APROVADO”
#e o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


nota1=float(input("Digite nota 1: "))
nota2=float(input("Digite nota 2: "))
media=(nota1+nota2)/2
if media >=9:
   conceito = "A"
elif media >= 7.5:
   conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
elif media >= 0:
    conceito = "E"
if conceito == "A" or "B" or "C":
    resultado = "Aprovado!"
elif conceito == "D" or "E":
    resultado = "Reprovado"
print("Nota 1: %.2f\nNota 2:%.2f"%(nota1,nota2))
print("Média: %.2f"%media)
print("Conceito: %s"%conceito)
print("Resultado: %s"%resultado)