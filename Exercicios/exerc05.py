#2. Faça um programa que preencha por leitura um vetor
#de 10 posições, e conta quantos valores diferentes
#existem no vetor.



lista = []

i = 0
j = 1
k = 1
aux = 0

for i in range(10):
    print('Digite o',j,'° numero: ')
    n = int(input('Digite: '))
    lista.append(n)
    j = j+1
    for k in range(li):
        if (lista[i] != lista[10]):
                aux = aux + 1


print(lista)
print(aux)

#3. Faça um programa que preencha por leitura um vetor
#de 5 posições, e informe a posição em que um valor x
#(lido do teclado) está no vetor. Caso o valor x não seja
#encontrado, o programa deve imprimir o valor -1