from copy import deepcopy

from No import Node


class Arvore:

    estadoFinal =[]
    idNo =0



    def buscaProfundidade(self,estadoFim, estadoInicio):
        self.estadoFinal.append(estadoFim)
        estadoInicio.append([self.idNo,None])
        abertos =[]
        abertos.append(estadoInicio)
        fechados =[]
        while len(abertos) > 0:
            noComparado = abertos.pop(0)
            if len(abertos) > 0:
                verificaFilhos = deepcopy(abertos[0])
            tamanhoAbertos = len(abertos)
            self.imprimir(noComparado)
            if self._compare(noComparado, self.estadoFinal[0]):
                return "Valor encontrado"
            else:
                filhoCima = []
                filhoDireita = []
                filhoBaixo = []
                filhoEsquerda = []


                cima        =   self._moveCima(deepcopy(noComparado))
                direita     =   self._moveDireita(deepcopy(noComparado))
                baixo       =   self._moveBaixo(deepcopy(noComparado))
                esquerda    =   self._moveEsquerda(deepcopy(noComparado))

                filhoCima.append(cima)
                filhoDireita.append(direita)
                filhoBaixo.append(baixo)
                filhoEsquerda.append(esquerda)

                fechados.insert(0, noComparado)


                if filhoEsquerda[0] is not None:
                    if self._comparaFilhos(filhoEsquerda, fechados) is False & self._comparaFilhos(filhoEsquerda,abertos) is False:
                        self.idNo +=1
                        filhoEsquerda[0][3][0]=self.idNo
                        filhoEsquerda[0][3][1]=noComparado[3][0]
                        abertos.insert(0,filhoEsquerda[0])
                    else:
                        filhoEsquerda = [None]
                if filhoBaixo[0] is not None:
                    if self._comparaFilhos(filhoBaixo, fechados) is False & self._comparaFilhos(filhoBaixo,abertos) is False:
                        self.idNo += 1
                        filhoBaixo[0][3][0]=self.idNo
                        filhoBaixo[0][3][1]=noComparado[3][0]
                        abertos.insert(0, filhoBaixo[0])
                    else:
                        filhoBaixo = [None]
                if filhoDireita[0] is not None:
                    if self._comparaFilhos(filhoDireita,fechados) is False & self._comparaFilhos(filhoDireita,abertos) is False:
                        self.idNo += 1
                        filhoDireita[0][3][0]=self.idNo
                        filhoDireita[0][3][1]=noComparado[3][0]
                        abertos.insert(0, filhoDireita[0])
                    else:
                        filhoDireita = [None]
                if filhoCima[0] is not None:
                    if self._comparaFilhos(filhoCima,fechados) is False & self._comparaFilhos(filhoCima,abertos) is False:
                        self.idNo += 1
                        filhoCima[0][3][0]=self.idNo
                        filhoCima[0][3][1]=noComparado[3][0]
                        abertos.insert(0, filhoCima[0])
                    else:
                        filhoCima = [None]
                if (filhoCima[0] is None) & (filhoBaixo[0] is None) & (filhoEsquerda[0] is None) & (filhoDireita[0] is None):
                   self.buscaPai(noComparado,fechados,verificaFilhos)





    #def imprimirPai(self):


    def buscaPai(self,noComparado,fechados,verificaFilhos):
        for filhoFechados in fechados:
            if filhoFechados[3][0] == noComparado[3][1]:
                self.imprimir(filhoFechados)
                if noComparado[3][1] == verificaFilhos[3][1]:
                    return True
                else:
                    self.buscaPai(filhoFechados,fechados,verificaFilhos)
                    return True

    def _compare(self,noComparado,sucesso):
        compara =[]
        for linha in range(0,3):
            for coluna in range(0,3):
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
                for linha in range(0,3):
                    for coluna in range(0,3):
                        if filhoFechado[linha][coluna] == filho[0][linha][coluna]:
                            vetorIgualFilho.append(True)
                        if len(vetorIgualFilho) > 8:
                            vetor_comparacao.append(True)
                            return True
            return False




    def _moveCima(self, x):
        for linha in range(0, 3):
            for coluna in range(0, 3):
                if linha > 0:
                    if x[linha][coluna] is not None:
                        if x[linha - 1][coluna] is None:
                             x[linha - 1][coluna] = x[linha][coluna]
                             x[linha][coluna] = None
                             return x[:]


    def _moveDireita(self, x):
        for linha in range(0, 3):
            for coluna in range(0, 3):
                if coluna < 2:
                    if x[linha][coluna] is not None:
                        if x[linha][coluna + 1] is None:
                             x[linha][coluna + 1] = x[linha][coluna]
                             x[linha][coluna] = None
                             return x

    def _moveBaixo(self, x):
        for linha in range(0, 3):
            for coluna in range(0, 3):
                if linha < 2:
                    if x[linha][coluna] is not None:
                        if x[linha + 1][coluna] is None:
                             x[linha + 1][coluna] = x[linha][coluna]
                             x[linha][coluna] = None
                             return x

    def _moveEsquerda(self, x):
            for linha in range(0, 3):
                for coluna in range(0, 3):
                    if coluna > 0:
                        if x[linha][coluna] is not None:
                            if x[linha][coluna - 1] is None:
                                 x[linha][coluna - 1] = x[linha][coluna]
                                 x[linha][coluna] = None
                                 return x


    def imprimir(self,meuNo):
        print('\nIdNo:',meuNo[3][0]," idPai:",meuNo[3][1],'\t\t Estado Final')
        print(meuNo[0],'\t\t\t\t',self.estadoFinal[0][0])
        print(meuNo[1],'\t\t\t\t',self.estadoFinal[0][1])
        print(meuNo[2],'\t\t\t\t',self.estadoFinal[0][2])
        print('_______________________________________________')


inicio =  [
          [1,2,5],
          [4,3,6],
          [7,8,None],
                 ]

fim =     [
          [1,2,3],
          [5,4,6],
          [7,None,8]
                 ]



tree = Arvore()
print(tree.buscaProfundidade(fim,inicio))

