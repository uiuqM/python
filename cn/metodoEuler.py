from tabulate import tabulate as tbl
from sympy import symbols, Function
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
'''#####################################################################################
Esse código visa implementar a resolução numérica de equações diferenciais ordinárias.
Usando o método de Euler
by Wilque Muriel do Nasimento Coelho.
########################################################################################'''

#simbolos usados nas equações.

def f(x, y):
    evaluated = eval(Ylinha)
    return evaluated

def g(x, y, z):
    evaluated = eval(eqJ)
    return evaluated

#entrada da funçao do PVI, malha, h...
print('Entre com as soluções do PVI: ')
Ylinha = input('Digite aqui y linha: ')
y0 = float(input('Digite y0: '))

malha = input('Digite a malha: ')
malha = malha.split(', ')
h = float(input('Digite o valor de h: '))
a = float(malha[0])
b = float(malha[1])

m = int((b-a)/h)

x = a
j = []
yLista = [y0]
eqJ = 'x+(y*z)'
xLista = [x]

print('Y linha = {}'.format(Ylinha))
print('Y zero = {}'.format(y0))
print('A malha = {}'.format(malha))
print('H = {}'.format(h))

#Esse loop faz a aproximação númerica pelo método de Euler.
for i in range(0, m):
    x = xLista[i]
    y = yLista[i]
    Y = f(x, y)
    yLista.append(g(yLista[i], h, Y))
    xLista.append(xLista[i]+h)
    j.append(i)

sol = solve_ivp(f, (a, b), (y0, ), max_step=h)
tabela = [j, xLista, yLista]
print(tbl({"j": j, "xj": xLista, "yj": yLista, "y(xj)": sol.y.T}, tablefmt='fancy_grid', floatfmt='.3f', headers='keys'))

#Plotando tabela com os resultados.
plt.plot(xLista, yLista, 'bo--', label="Solução aproximada.")
plt.plot(sol.t, sol.y.T, label='solução exata.')
plt.title("Solução exata e aproximada")
plt.ylabel('y')
plt.ylabel('x')
plt.legend(loc='lower right')
plt.show()