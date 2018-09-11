from No import Node


class Arvore:
    def __init__(self):
        self.raiz = None

    estadoFinal =0
    idNo =0



    def inserir(self,valor):

        if(self.raiz is None):
            self.raiz = Node(0,valor, None)
        else:
            self.idNo += 1
            self._inserir(valor, self.raiz)


    def _inserir(self,valor,node):
        if(valor < node.valor):
            if(node.esquerda is None):
                node.esquerda = Node(self.idNo,valor,node.id)
            else:
                self._inserir(valor,node.esquerda)
        elif valor > node.valor:
            if(node.direita is None):
                node.direita =Node(self.idNo,valor,node.id)
            else:
                self._inserir(valor,node.direita)
        else:
            self.idNo -= 1
            return False

    def preOrder(self):
         if self.raiz is not None:
             self._preOrder(self.raiz)

    def _preOrder(self,no):
        if no is not None:
            print("IdNo:",no.id,"Valor:",no.valor,"Pai:",no.pai)
            self._preOrder(no.esquerda)
            self._preOrder(no.direita)


    def buscaProfundidade(self,estadoFim, estadoInicio):
        abertos =[]
        abertos.append(estadoInicio)
        fechados =[]

        while abertos is not None:
            noComparado = abertos.pop(0)
            if self._compare(noComparado, self.estadoFinal):
                return True




    def _compare(self,noComparado,sucesso):
        compara =[]
        for linha in range(0,len(noComparado)):
            for coluna in range(0,len(noComparado)):
                if noComparado[linha][coluna] != sucesso[linha][coluna]:
                    return False
                else:
                   compara.append(True)
        if len(compara) == 9:
            return True





T = Arvore()
T.inserir(10)
T.inserir(5)
T.inserir(12)
T.inserir(6)
T.inserir(12)
T.inserir(8)
T.inserir(1)
T.preOrder()
z = 1242

inicio =  [
          [1,2,3],
          [4,5,6],
          [7,8,0]
                 ]

fim =     [
          [1,2,4],
          [3,5,6],
          [7,8,0]
                 ]



print(len(z))


