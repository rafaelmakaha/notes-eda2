### Arvore AVL

### Classe nó
class Node(object):
    def __init__(self, valor):
        self.value = value
        self.esq = None
        self.dir = None
        self.altura = 1

### Classe árvore

class Arvore(object):
    def insere(self, raiz, key):
        
        if not root:
            return Node(key)