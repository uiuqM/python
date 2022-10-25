import arvoreBinariaDeBusca as avl

operacao_escolhida = 0
while operacao_escolhida != 5:
    print(20 * "---")
    print("\n\n                     Menu das operações: \n\n")
    print(20 * "---")
    print("1. Operação de inserção de um elemento na AVL;")
    print("2. Operação de remoção de um elemento na AVL;")
    print("3. Operação de busca de um elemento na AVL;")
    print("4. Operação de impressão da árvore AVL.")
    print("0. Sair.")
    operacao_escolhida = int(input("Digite o número da operação: "))

    arv = avl.binarySearchTree()

    if operacao_escolhida == 1:
        num = int(input("Digite o valor a ser inserido: "))
        arv.insert(num)
    elif operacao_escolhida == 2:
        num = int(input('Digite o valor a ser removido:'))
        arv.remove(num)
    elif operacao_escolhida == 3:
        num = int(input('Digite o valor de busca: '))
        if arv.busca(num):
            print('valor existe na arvore')
        else:
            print('valor nao encontrado!')
    elif operacao_escolhida == 4:
        printa = input('Deseja imprimir em nivel ou em ordem?')
        if printa == 'em nivel':
            arv.levelOrder()
        elif printa == 'em ordem':
            arv.emOrdem()
