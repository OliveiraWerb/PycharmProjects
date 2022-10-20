"""
lista = [1,2,3,10,5,6]
valor = 8
resultado = False
for i in range(len(lista)):
    if lista[i] == valor:
        resultado = True
print(resultado)



lista = [1,2,3,4]
resultado = 2 in lista
print(resultado)

x = input("Digite valores separados por espaço: ").split()
print(x)


turma = [[5.0, 4.5, 7.0, 5.2, 6.1],[2.1, 6.5,8.0,7.0,6.7], [8.6, 7.0,9.1, 8.7,9.3]]
media = 0
for i in range(3):
    for j in range(5):
        media = media + turma[i][j]
media = media/15
print(media)


n = int(input('Digite a dimensao N da matriz: '))
m = int(input('Digite a dimensao M da matriz: '))
matriz = []
for i in range(n):
    matriz.append([0]*m)
#print em formato matriz
for i in range(n):
    print(matriz[i])
"""

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input('Digite um valor de: ('+str(i) + ',' +str(j) +'):' )))
    matriz.append(linha)
#contarpares
pares = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            pares = pares+1
#imprimir em formato matriz
for i in range(3):
    print(matriz[i])
print('A matriz contem', pares,'numeros pares!')
