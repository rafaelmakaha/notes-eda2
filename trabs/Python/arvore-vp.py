import time

BLACK = "BLACK"
RED = "RED"

class Node(object):
    def __init__(self, key):
        self.key = key
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None

class Arvore(object):

    def insert(self, root, key):
        
        # Cria o novo nó
        node = Node(key)

        # Caso seja raiz
        if root == None:
            node.color = BLACK
            root = node
            return root
        
        # Encontra o pai do nó
        currentNode = root
        while currentNode != None:
            potentialParent = currentNode
            if node.key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        
        # Seta o pai do nó
        node.parent = potentialParent
        
        # Seta o lado no pai em que o nó será setado
        if node.key < node.parent.key:
            node.parent.left = node
        else:
            node.parent.right = node

        # Chama o rebalanceamento da árvore
        self.fixTree(root, node)

        return root

    def fixTree(self,root, node):

        while Node(node.parent.color) == RED and node != root:

            # Caso o pai esteja a esquerda do avô
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                # Caso 3 - Pai e tio vermelhos
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent  # unknown

                else:
                    # Caso 4 - Pai vermelho e tio preto, peso interno
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(root,node)
                    
                    # Caso 5 - Pai vermelho e tio preto, peso externo
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(root,node.parent.parent)
            
            # Caso o pai esteja a direita do avô
            else:
                uncle = node.parent.parent.right

                # Caso 3
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent

                else:
                    # Caso 4
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(root,node)
                    
                    # Caso 5
                    node.parent.color = BLACK
                    node.parent.parent.color = BLACK
                    self.left_rotate(root,node.parent.parent)

        root.color = BLACK

    def left_rotate(self,root, node):
        
        sibling = node.right
        node.right = sibling.left

        if sibling.left != None:
            sibling.left.parent = node
        
        sibling.parent = node.parent
        
        if node.parent == None:
            root = sibling
        else:
            if node == node.parent.left:
                node.parent.left = sibling
            else:
                node.parent.right = sibling

        sibling.left = node
        node.parent = sibling
    
    def right_rotate(self,root, node):
        
        sibling = node.left
        node.left = sibling.right

        if sibling.right != None:
            sibling.right.parent = node
        
        sibling.parent = node.parent
        
        if node.parent == None:
            root = sibling
        else:
            if node == node.parent.right:
                node.parent.right = sibling
            else:
                node.parent.left = sibling

        sibling.right = node
        node.parent = sibling

    def inOrder(self, raiz):
        if raiz == None:
            return
        else:
            self.inOrder(raiz.left)
            print("{0} ".format(raiz.key), end="")
            self.inOrder(raiz.right)


rb = Arvore()
raiz = None

lista = [6, 8, 0, 7, 9, 1, 3, 4, 2, 5]
print("Amostra Inicial: " + str(lista))

rbTime = []

for i in lista:
    print("Insere:" + str(i))

    time1 = time.time()
    raiz = rb.insert(raiz, i)
    time2 = time.time()

    rbTime.append(str(time2 - time1))

    print("Impressão in Order: ")
    rb.inOrder(raiz)
    print("\n")

with open("rb_time", "w") as file_object:
    file_object.writelines("%s\n" % i for i in rbTime)
file_object.close
