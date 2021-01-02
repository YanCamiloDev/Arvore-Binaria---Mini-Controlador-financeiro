from model.Despesa import Despesa
from dateutil.relativedelta import *
from datetime import datetime
from model.Receita import Receita
from model.RelatorioAbstract import RelatorioAbstract


# HERANÇA
class Resumo(RelatorioAbstract):

    def __init__(self, receitas=0, despesas=0, saldo=0, periodo=None):
        # ENCAPSULAMENTO (O UNDERLINE DEFINE COMO PRIVATE)
        self._periodo = periodo
        self._receitas = receitas
        self._despesas = despesas
        self._saldo = saldo

    # GETS E SETS
    def setPeriodo(self, periodo):
        self._periodo = periodo

    def setReceitas(self, receitas):
        self._receitas = receitas

    def setDespesas(self, despesas):
        self._despesas = despesas

    def setSaldo(self, saldo):
        self._saldo = saldo

    def getPeriodo(self):
        return self._periodo

    def getReceitas(self):
        return self._receitas

    def getDespesas(self):
        return self._despesas

    def getSaldo(self):
        return self._saldo

    # POLIMORFISMO
    def relatorioMovimentacoes(self, lista):
        date = datetime.now()
        cont = 0
        datas = []
        datas.append(date.date())
        for i in range(11):
            cont += 1
            dataSub = date + relativedelta(months=-cont)
            d = dataSub.date()
            datas.append(d)
        listaOfResumo = self._resume(lista, datas)
        return listaOfResumo

    # POLIMORFISMO
    def calcularSaldo(self, lista):
        saldo = 0
        for movimentacao in lista:
            if movimentacao.getData().year + movimentacao.getData().month == date.today().year + date.today().month:
                if isinstance(movimentacao, Despesa.Despesa):
                    saldo -= self.getValor()
                elif isinstance(movimentacao, Receita.Receita):
                    saldo += self.getValor()
        return saldo

    def _resume(self, lista, datas):
        saldo = 0
        receitas = 0
        despesas = 0
        resumoList = []
        for dataas in datas:
            for movimentacao in lista:
                if str(movimentacao.getData().year) + str(movimentacao.getData().month) == str(dataas.year) + str(
                        dataas.month):
                    if isinstance(movimentacao, Despesa):
                        despesas += movimentacao.getValor()
                        saldo -= movimentacao.getValor()
                    elif isinstance(movimentacao, Receita):
                        receitas += movimentacao.getValor()
                        saldo += movimentacao.getValor()
            resumoList.append(Resumo(receitas, despesas, saldo, dataas))
            receitas = 0
            saldo = 0
            despesas = 0
        return resumoList
