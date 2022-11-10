import matplotlib.pyplot as plt
from tabulate import tabulate as tbl
import numpy as np

x = []
y = []

listaIndice = []

total = int(input('quantos pontos: '))

for i in range(0, total):
    listaIndice.append(i+1)

for i in range(0, total):
    valx = float(input('Digite o valor para x{0}: '.format(i+1)))
    x.append(valx)
    valy = float(input('Digite o valor para y{0}: '.format(i+1)))
    y.append(valy)

tabela = [listaIndice, x, y]
print("TABELA DE COODERNADAS:")
print(tbl(tabela, tablefmt='fancy_grid', showindex=True, floatfmt='.1f', headers='firstrow'))

somaX = float()
for ponto in x:
    somaX += ponto

somaXAoQuadrado = float()
for ponto in x:
    somaXAoQuadrado += ponto**2

somaY = float()
for ponto in y:
    somaY +=ponto

somaXY = float()
for i in range(0, total):
    for i in range(i, total):
        somaXY += x[i]*y[i]
        break

print('Soma x: {:.2f}'.format(somaX))
print('Soma x ao quadrado: {:.2f}'.format(somaXAoQuadrado))
print('Soma y: {:.2f}'.format(somaY))
print('Soma xy: {:.2f}'.format(somaXY))

b1 = (total*somaXY-somaX*somaY)/(total*somaXAoQuadrado-somaX**2)

b0 = (somaY-somaX*b1)/total

print('b1 = {0} e b0 = {1}'.format(b1, b0))

listaYlinha = []
listaDiferenca = []

for i in range(0, total):
    listaYlinha.append(b0+b1*x[i])

for i in range(0, total):
    listaDiferenca.append(y[i]-listaYlinha[i])

print("TABELA Y LINHA E DIFERENÇA:")
tabela1 = [listaIndice, listaYlinha, listaDiferenca]

print(tbl({"i": listaIndice, "Xi": x, "Yi":y, "Y\'={:.3f}+{:.3f}*x".format(b0, b1): listaYlinha, "Di = Yi-Y\'i": listaDiferenca},
        tablefmt='fancy_grid', floatfmt='.1f', headers='keys'))

D = float()
for dif in listaDiferenca:
    D += dif**2

print('D = {:.2f}'.format(D))

x = np.array(x)

def f(x):
    return b0+b1*x

plt.plot(x, f(x), color='red')

plt.plot(x, y, label='line', ls='None', marker='o', markerfacecolor='green', markersize=12)

plt.xlabel('eixo X')
plt.ylabel('eixo Y')

plt.title('Diagrama de dispersão')

plt.show()