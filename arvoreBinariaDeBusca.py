import queue

class Node():
    def __init__(self, data):
        self.data = data
        self.esquerda = None
        self.direita = None
        self.pai = None
        self.altura = 1

class binaryTree():
    def __init__(self, data=None, node=None): #construtor
        if node:
            self.raiz = node
        elif data:
            node = Node(data)
            self.raiz = node
        else:
            self.raiz = None

    '''def search(self, value, node=None):
        if node is None:
            node = self.raiz
        if (value > node.data):
            self.search(node.direita)
        elif (value < node.data ):
            self.search(node.esquerda)
        elif (node.data == value):
            return True
        return False'''
        
class binarySearchTree(binaryTree):
    def insert(self, value):
        pai = None
        x = self.raiz
        while(x):
            pai = x
            if(value<x.data):
                x = x.esquerda
            else:
                x = x.direita
        if pai is None:
            self.raiz = Node(value)
        elif value < pai.data:
            pai.esquerda = Node(value)
            pai.esquerda.pai = pai
            self._verificaInsercao(pai.esquerda)
        else:
            pai.direita = Node(value)
            pai.direita.pai = pai
            self._verificaInsercao(pai.direita)

    def altura(self):
        if self.raiz !=None:
            return self._altura(self.raiz, 0)
        else:
            return 0
    def _altura(self, current, currentAlt):
        if current == None: 
            return currentAlt
        alturaEsq = self._altura(current.esquerda, currentAlt+1)
        alturaDir = self._altura(current.direita, currentAlt+1)
        return max(alturaEsq, alturaDir)
    '''def imprimeArvore(self):
        if self.raiz != None:
            self._imprimeArvore(self.raiz)
    
    def _imprimeArvore(self, node):
        if(node!=None):
            self._imprimeArvore(node.esquerda)
            print (str(node.data))
            self._imprimeArvore(node.direita)'''

    def searchMin(self, node=None): #procura o menor elemento da árvore.
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.searchMin(node.esquerda)
        else:
            print(node.data)

    def searchMax(self, node=None): #procura o maior elemento da árvore.
        if node is None:
            node = self.raiz
        if node.direita:
            self.searchMax(node.direita)
        else:
            print(node.data)

    def find(self, value): #busca na arvore passa a raiz pra uma funcao privada.
        if self.raiz != None:
            return self._find(value, self.raiz)
        else:
            return None

    def _find(self, value, current): #compara o valor com o nó atual
        if current.data == value:
            return current
        elif value < current.data and current.esquerda !=None:
            return self._find(value, current.esquerda)
        elif value > current.data and current.direita !=None:
            return self._find(value, current.direita)
        return None

    def search(self, value): #busca na arvore passa a raiz pra uma funcao privada.
        if self.raiz != None:
            return self._search(value, self.raiz)
        else:
            return False

    def _search(self, value, current): #compara o valor com o nó atual
        if current.data == value:
            return True
        elif value < current.data and current.esquerda !=None:
            return self._search(value, current.esquerda)
        elif value > current.data and current.direita !=None:
            return self._search(value, current.direita)
        return False

    def preOrdem(self, node=None): #imprime a arvore em pre ordem.
        if node is None:
            node = self.raiz
        print(node.data, end=" ")
        if node.esquerda:
            self.preOrdem(node.esquerda)
        if node.direita:
            self.preOrdem(node.direita)

    def emOrdem(self, node=None): #imprime arvore em ordem.
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.emOrdem(node.esquerda)
        print(node.data, end = " ")
        if node.direita:
            self.emOrdem(node.direita)

    def posOrdem(self, node =None): #imprime a arvore em pos ordem.
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.posOrdem(node.esquerda)
        if node.direita:
            self.posOrdem(node.direita)
        print(node.data, end = " ")

    def remove(self, valor):
        return self.deletaNode(self.find(valor))
        
    def deletaNode(self, node):

        def minValorNode(n): #retorna o menor valor com o node de input como raiz
            current = n
            while current.esquerda != None:
                current = current.esquerda
            return current
        
        def numFilhos(n):
            numFilhos = 0
            if n.esquerda!=None: numFilhos+=1
            if n.direita!=None: numFilhos+=1
            return numFilhos

        nodePai = node.pai
        nodeFilho = numFilhos(node)

        #CASO 1 o nó não tem filhos.
        if nodeFilho == 0:
            if nodePai.esquerda == node: #pai passa apontar pra None
                nodePai.esquerda = None
            else:
                nodePai.direita = None
        
        #CASO 2 o nó tem um filho.
        elif nodeFilho == 1:
            if node.esquerda != None:
                filho = node.esquerda
            else:
                filho = node.direita
            if nodePai.esquerda == node:
                nodePai.esquerda = filho
            else:
                nodePai.direita = filho
            filho.pai = nodePai

        if nodeFilho == 2:
            #pega o sucessor do nó deletado.
            sucessor = minValorNode(node.direita)
            #copia para o nó
            node.data = sucessor.data
            self.deletaNode(sucessor)
        
        if nodePai != None:
            nodePai.altura = 1+max(self.getAltura(nodePai.esquerda), self.getAltura(nodePai.direita))
            self._verificaRemove(nodePai)
        
    def levelOrder(self, node=None): #imprime a arvore em nivel.
        node = self.raiz
        fila = queue.Queue()
        fila.put(node)

        while fila.qsize():
            node = fila.get()
            print(node.data, end=" ")
            if node.esquerda:
                fila.put(node.esquerda)
            if node.direita:
                fila.put(node.direita)
    
    def _verificaInsercao(self, current, cam=[]):
        if current.pai == None:
            return 
        cam=[current]+cam
        alturaEsq = self.getAltura(current.pai.esquerda)
        alturaDir = self.getAltura(current.pai.direita)

        if abs(alturaEsq-alturaDir)>1:
            cam = [current.pai]+cam
            self._rebalanco(cam[0], cam[1], cam[2])
            return
        novaAltura = 1+current.altura
        if novaAltura>current.pai.altura:
            current.pai.altura = novaAltura
        
        self._verificaInsercao(current.pai, cam)

    def _verificaRemove(self, current):
        if current == None:
            return
        alturaEsq = self.getAltura(current.esquerda)
        alturaDir = self.getAltura(current.direita)

        if abs(alturaEsq-alturaDir)>1:
            y = self._menorFilho(current)
            x = self._menorFilho(y)
            self._rebalanco(current, y, x)
        
        self._verificaRemove(current.pai)

    def _rebalanco(self, z, y, x):
        if y==z.esquerda and x==y.esquerda:
            self._rotacaoDireita(z)
        elif y==z.esquerda and x==y.direita:
            self._rotacaoEsquerda(y)
            self._rotacaoDireita(z)
        elif y==z.direita and x==y.direita:
            self._rotacaoEsquerda(z)
        elif y==z.direita and x==y.esquerda:
            self._rotacaoDireita(y)
            self._rotacaoEsquerda(z)
        else:
            raise Exception('configuracao incompativel!')

    def _rotacaoDireita(self, z):
        subRaiz = z.pai
        y = z.esquerda
        t3 = y.direita
        y.direita = z
        z.pai = y
        z.esquerda = t3
        if t3 != None:
            t3.pai = z
        y.pai = subRaiz
        if y.pai == None:
            self.raiz = y
        else:
            if y.pai.esquerda == z:
                y.pai.esquerda = y
            else:
                y.pai.direita = y
        z.altura = 1+max(self.getAltura(z.esquerda), self.getAltura(z.direita))
        y.altura = 1+max(self.getAltura(y.esquerda), self.getAltura(y.direita))
    def _rotacaoEsquerda(self, z):
        subRaiz = z.pai
        y = z.direita
        t2 = y.esquerda
        y.esquerda = z
        z.pai = y
        z.direita = t2
        if t2 !=None:
            t2.pai = z
        y.pai = subRaiz
        if y.pai == None:
            self.raiz = y
        else:
            if y.pai.esquerda == z:
                y.pai.direita = y
            else:
                y.pai.direita = y
        z.altura = 1+max(self.getAltura(z.esquerda), self.getAltura(z.direita))
        y.altura = 1+max(self.getAltura(y.esquerda), self.getAltura(y.direita))

        
    def getAltura(self, current):
        if current == None:
            return 0
        return current.altura
    def _menorFilho(self, current):
        esquerda = self.getAltura(current.esquerda)
        direita = self.getAltura(current.direita)
        return current.esquerda if esquerda>=direita else current.direita


#class avlTree(binarySearchTree)
arv = binarySearchTree()

'''arv.insert(40)
arv.insert(20)
arv.insert(10)
arv.insert(60)
arv.insert(30)
arv.insert(50)
arv.insert(70)

arv.searchMin()
arv.searchMax()
arv.preOrdem()
print()
arv.emOrdem()
print()
arv.posOrdem()
print()
print(arv.search(70))
arv.remove(70)
arv.emOrdem()
print()'''

'''arv.insert(8)
arv.insert(3)
arv.insert(10)
arv.insert(1)
arv.insert(6)
arv.insert(14)
arv.insert(4)
arv.insert(7)
arv.insert(13)

arv.levelOrder()'''

arv = binarySearchTree()
operacao_escolhida = 2
while operacao_escolhida != 0:
    print(20 * "---")
    print("\n\n                     Menu das operações: \n\n")
    print(20 * "---")
    print("1. Operação de inserção de um elemento na AVL;")
    print("2. Operação de remoção de um elemento na AVL;")
    print("3. Operação de busca de um elemento na AVL;")
    print("4. Operação de impressão da árvore AVL.")
    print("0. Sair.")
    operacao_escolhida = int(input("Digite o número da operação: "))

    if operacao_escolhida == 1:
        num = int(input("Digite o valor a ser inserido: "))
        sair = False
        arv.insert(num)
    elif operacao_escolhida == 2:
        num = int(input('Digite o valor a ser removido:'))
        arv.remove(num)
    elif operacao_escolhida == 3:
        num = int(input('Digite o valor de busca: '))
        if arv.search(num):
            print('valor existe na arvore')
        else:
            print('valor nao encontrado!')
    elif operacao_escolhida == 4:
        printa = input('Deseja imprimir em nivel ou em ordem?')
        if printa == 'em nivel':
            arv.levelOrder()
            print()
        elif printa == 'em ordem':
            arv.emOrdem()
            print()
    elif operacao_escolhida == 5:
        print(str(arv.altura()))