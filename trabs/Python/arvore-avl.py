### Arvore AVL
import time
from random import sample, choice

### Classe nó
class Node(object):
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dire = None
        self.altura = 1

### Classe árvore

class Arvore(object):

    # Faz a inserção de um novo valor
    def insere(self, raiz, key):
        # Caso seja raíz
        if raiz == None:
            return Node(key)
        elif key < raiz.valor:
            raiz.esq = self.insere(raiz.esq, key)
        else:
            raiz.dire = self.insere(raiz.dire, key)
        
        # Atualiza a altura da raíz
        raiz.altura = 1 + max(self.getAltura(raiz.esq), self.getAltura(raiz.dire))

        # Recebe o Fator de Balanceamento
        fb = self.getFatorBalanceamento(raiz)

        # Verifica necessidade de balanceamento da árvore
        if fb > 1 and key < raiz.esq.valor:
            return self.rotDir(raiz)
        if fb < -1 and key > raiz.dire.valor:
            return self.rotEsq(raiz)
        if fb > 1 and key > raiz.esq.valor:
            print("Entrei aqui: " + str(raiz.valor))
            raiz.esq = self.rotEsq(raiz.esq)
            return self.rotDir(raiz)
        if fb < -1 and key < raiz.dire.valor:
            print("Entrei aqui: " + str(raiz.valor))
            raiz.dire = self.rotDir(raiz.dire)
            return self.rotEsq(raiz)

        return raiz

    # Faz a remoção de um valor específico
    def delete(self, raiz, key):
        
        if raiz == None:
            print("raiz nula")
            return raiz
        elif key < raiz.valor:
            raiz.esq = self.delete(raiz.esq, key)
        elif key > raiz.valor:
            raiz.dire = self.delete(raiz.dire, key)
        else:
            if raiz.esq is None:
                aux = raiz.dire
                raiz = None
                return aux
            elif raiz.dire is None:
                aux = raiz.esq
                raiz = None
                return aux
            
            aux = self.getMenorValor(raiz.dire)
            raiz.valor = aux.valor
            raiz.dire = self.delete(raiz.dire, aux.valor)

        # is this really neccessary?
        # it does not seem that raiz is changed 
        if raiz == None:
            return raiz
        
        raiz.altura = 1 + max(self.getAltura(raiz.esq), self.getAltura(raiz.dire))

        fb = self.getFatorBalanceamento(raiz)

        if fb > 1 and self.getFatorBalanceamento(raiz.esq) >= 0:
            return self.rotDir(raiz)
        if fb < -1 and self.getFatorBalanceamento(raiz.dire) <= 0:
            return self.rotEsq(raiz)
        if fb > 1 and self.getFatorBalanceamento(raiz.esq) < 0:
            raiz.esq = self.rotEsq(raiz.esq)
            return self.rotDir(raiz)
        if fb < -1 and self.getFatorBalanceamento(raiz.dire) > 0:
            raiz.dire = self.rotDir(raiz.dire)
            return self.rotEsq(raiz)

        return raiz

    def rotEsq(self, a):
        b = a.dire
        c = b.esq

        b.esq = a
        a.dire = c
        
        a.altura = 1 + max(self.getAltura(a.esq), self.getAltura(a.dire))
        b.altura = 1 + max(self.getAltura(b.esq), self.getAltura(b.dire))

        return b

    def rotDir(self, a):
        
        b = a.esq
        c = b.dire

        b.dire = a
        a.esq = c
        
        a.altura = 1 + max(self.getAltura(a.esq), self.getAltura(a.dire))
        b.altura = 1 + max(self.getAltura(b.esq), self.getAltura(b.dire))

        return b

    def getAltura(self, raiz):

        if raiz == None:
            return 0
        else:
            return raiz.altura    
    
    def getFatorBalanceamento(self, raiz):
        if raiz == None:
            return 0
        else:
            return self.getAltura(raiz.esq) - self.getAltura(raiz.dire)
    
    def getMenorValor(self, raiz):
        if raiz is None or raiz.esq is None:
            return raiz
        else:
            self.getMenorValor(raiz.esq)
    
    def inOrder(self, raiz):
        if raiz == None:
            return
        else:
            self.inOrder(raiz.esq)
            print("{0} ".format(raiz.valor), end="")
            self.inOrder(raiz.dire)


# Inicia a árvore
avl = Arvore()
raiz = None

# Cria lista aleatória
#lista = sample(range(10), 10)
lista = [6, 8, 0, 7, 9, 1, 3, 4, 2, 5]
print("Amostra inicial: " + str(lista))

avlTime = []

for i in lista:
    print("Insere:" + str(i))

    time1 = time.time()
    raiz = avl.insere(raiz, i)

    time2 = time.time()
    avlTime.append(str(time2 - time1))

    print("Impressão in Order: ")
    avl.inOrder(raiz)
    print("\n")


with open("avl_time", "w") as file_object:
    file_object.writelines("%s\n" % i for i in avlTime)
file_object.close

# Seleção de amostras para remoção
delete_lista = []
n_delecoes = 3
# Valores de deleção fixos
delete_lista = [1, 0, 7]
# for i in range(n_delecoes):
#     aux = choice(lista)
#     delete_lista.append(aux)
# print(delete_lista)

# Execução da ação de deleção dos valores selecionados
for i in delete_lista:
    print("Remove: " + str(i))
    raiz = avl.delete(raiz, i)

    print("Impressão in Order: ")
    avl.inOrder(raiz)
    print("\n")
