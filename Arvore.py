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
        abertos = estadoInicio
        fechados =[]
        self.raiz = Node(self.idNo,estadoInicio,None)
        self.idNo +=1
        while abertos is not None:
            filhos =[]
            noComparado = abertos.pop(0)
            if self._compare(noComparado, self.estadoFinal):
                return True
            else:
                filhoCima       = self._moveCima(noComparado)
                filhoDireita    = self._moveDireita(noComparado)
                filhoBaixo      = self._moveBaixo(noComparado)
                filhoEsquerda   = self._moveEsquerda(noComparado)

                fechados.insert(0, noComparado)

                if self._comparaFilhos(filhoEsquerda, fechados) is False & self._comparaFilhos(filhoEsquerda,abertos) is False:
                    abertos.insert(0,filhoEsquerda)
                elif self._comparaFilhos(filhoBaixo, fechados) is False & self._comparaFilhos(filhoBaixo,abertos) is False:
                    abertos.insert(0, filhoBaixo)
                elif self._comparaFilhos(filhoDireita,fechados) is False & self._comparaFilhos(filhoDireita,abertos) is False:
                    abertos.insert(0, filhoDireita)
                elif self._comparaFilhos(filhoCima,fechados) is False & self._comparaFilhos(filhoCima,abertos) is False:
                    abertos.insert(0, filhoCima)
                else:
                    return False








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


    def _comparaFilhos(self,filho,fechados):
            vetor_comparacao = []

            for filhoFechado in fechados:
                vetorIgualFilho =[]
                for linha in range(0,len(filho)):
                    for coluna in range(0,len(filho)):
                        if filhoFechado[linha][coluna] == filho[linha][coluna]:
                            vetorIgualFilho.append(True)
                        if len(vetorIgualFilho) > 8:
                            return True
                        else:
                            vetor_comparacao.append(True)

            if len(vetor_comparacao) == len(fechados):
                return True
            else:
                return False




    def _moveCima(self,x):
        for linha in range(0,len(x)):
            for coluna in range(0,len(x)):
                if x[linha][coluna] is not None & linha > 0 & x[linha-1][coluna] is None:
                 x[linha-1][coluna] = x[linha][coluna]
                 x[linha][coluna] = None
                 return x


    def _moveDireita(self,x):
        for linha in range(0,len(x)):
            for coluna in range(0,len(x)):
                if x[linha][coluna] is not None & coluna < 2 & x[linha][coluna+1] is None:
                 x[linha][coluna+1] = x[linha][coluna]
                 x[linha][coluna] = None
                 return x

    def _moveBaixo(self,x):
        for linha in range(0,len(x)):
            for coluna in range(0,len(x)):
                if x[linha][coluna] is not None & linha < 2 & x[linha+1][coluna] is None:
                 x[linha+1][coluna] = x[linha][coluna]
                 x[linha][coluna] = None
                 return x

    def _moveEsquerda(self,x):
        for linha in range(0,len(x)):
            for coluna in range(0,len(x)):
                if x[linha][coluna] is not None & coluna > 0 & x[linha][coluna-1] is None:
                 x[linha][coluna-1] = x[linha][coluna]
                 x[linha][coluna] = None
                 return x


    #def insereFilhosArvore(self,arvore,node):


T = Arvore()
T.inserir(10)
T.inserir(5)
T.inserir(12)
T.inserir(6)
T.inserir(12)
T.inserir(8)
T.inserir(1)
p = T.preOrder()



inicio =  [
          [1,2,3],
          [4,5,6],
          [7,8,0],
                 ]

fim =     [
          [1,2,4],
          [3,5,6],
          [7,8,0]
                 ]

p =5
inicio.append((2,5))
z = inicio


print(len(fim))



