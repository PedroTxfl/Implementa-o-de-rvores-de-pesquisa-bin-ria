from Node import Node

class ArvPesqBinaria:

    def __init__(self):
        self.root = None

    def is_empty(self):
        if (self.root == None):
            return True
        else:
            return False

    def get_root(self):
        return self.root

    def insert(self, key):
        nodo = Node(key)
        if (self.is_empty()): #se ta vazia vira raiz logo
            self.root = nodo
        else: #caso ja tenha raiz, vai percorrer a lista atras do lugar certo
            nodo_pai = None
            nodo_atual = self.root

            while True:
               if (nodo_atual != None): #nas próximas repetições vai usar
                   nodo_pai = nodo_atual
                   if (nodo.getKey() < nodo_atual.getKey()):                      
                        nodo_atual = nodo_atual.getLeft()
                   else: 
                        nodo_atual = nodo_atual.getRight()
               else: #achou o pai do lugar certo
                    if (nodo.getKey() < nodo_pai.getKey()): 
                        nodo_pai.setLeft(nodo) #colocar o filho
                        nodo.setParent(nodo_pai)
                    else:
                        nodo_pai.setRight(nodo)
                        nodo.setParent(nodo_pai)
                    break

    def search(self, key):
        if (self.is_empty()):
            print("Árvore vazia") #nao tem como procurar no nada
        else:
            nodo_atual = self.root
            while True:
                if (nodo_atual != None):
                    if key == nodo_atual.getKey(): #verifica se é 
                        print("Encontrado!")
                        return nodo_atual.getKey()
                    elif key < nodo_atual.getKey(): #esq
                        nodo_atual = nodo_atual.getLeft()
                    else: #dir
                        nodo_atual = nodo_atual.getRight()
                else: #se nodo atual none = percorreu e não achou
                    print("Não foi encontrado na árvore")
                    break

    def size(self, nodo_atual): #parametro tem que ser colocado para colocar o root e possibilitar a corrida
        if nodo_atual == None:
            return 0
        else:    #desenhei em papel pra entender  | RECURSAO LE EM PRÉ ORDEM
            return 1 + self.size(nodo_atual.getLeft()) + self.size(nodo_atual.getRight()) 
            
    def height(self, nodo_atual): #muito dificil precisei procurar bastante na internet #ontem tarde vi que altura na teoria conta a raiz como a altura 0
        if nodo_atual == None:
            return 0
        else:
            height_left = 0
            height_right = 0

            if nodo_atual.left:
                height_left = self.height(nodo_atual.left)

            if nodo_atual.right:
                height_right = self.height(nodo_atual.right)
                
            if height_right > height_left:
                return height_right + 1
            return height_left + 1

    def get_father(self, key):
        if (self.is_empty()):
            print("Árvore vazia")
        else:
            nodo_atual = self.root
            while True:
                if key == nodo_atual.getKey():
                    pai = nodo_atual.getParent()
                    if pai == None:
                        print("Este nó não tem pai pois ele é a RAIZ.")
                        return
                    else:
                        print("O pai deste nó é: ", pai.getKey())
                        return nodo_atual.getParent()
                elif key < nodo_atual.getKey():
                    nodo_atual = nodo_atual.getLeft()
                elif key > nodo_atual.getKey():
                    nodo_atual = nodo_atual.getRight()
                else: 
                    print("Não encontrado")
                    break

                
    ####### CAMINHAMENTOS


    #VED
    def pre_order(self, nodo_atual):
        if (nodo_atual != None):
            print(nodo_atual.getKey(), end=" ")                   #print(' %d' % nodo_atual.getKey(), end=" ")
            self.pre_order(nodo_atual.getLeft())
            self.pre_order(nodo_atual.getRight())
    #EVD
    def in_order(self, nodo_atual):
        if (nodo_atual != None):
            self.in_order(nodo_atual.getLeft())
            print(nodo_atual.getKey(), end=" ")                   #,end(" ")
            self.in_order(nodo_atual.getRight())
    #VDE
    def post_order(self, nodo_atual):
        if (nodo_atual != None):
            self.post_order(nodo_atual.getLeft())
            self.post_order(nodo_atual.getRight())
            print(nodo_atual.getKey(), end=" ")

