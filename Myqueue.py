# nó pra alocação da fila
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#classe que define fila
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    #inserir na fila
    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        
        if self.first is None:
            self.first = node

        self.size = self.size + 1

    #remove da fila
    def pop(self):
        #remove do topo da lista
        if self.size > 0:
            elem = self.first.data
            