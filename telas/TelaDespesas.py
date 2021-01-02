from datetime import datetime
from model.Despesa import Despesa
from linkedList.LinkedList import LinkedList
import locale
import time
import os


class TelaDespesas:

    # Criando método para padronizar os dados em moeda real:
    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

    def __init__(self):
        listaDespesa = LinkedList()

    # Criando médoto para operacionalizar a lista encadeada:
    def render(self, lista=LinkedList(), idsLista=0):
        idDespesas = idsLista

        # Opções do módulo das despesas financeiras:
        opDespesas = "0"
        while opDespesas != "4":
            os.system("cls")
            TelaDespesas.headerDespesas()
            self.listar(lista)
            TelaDespesas.menuDespesas()
            TelaDespesas.footerDespesas()
            opDespesas = input(" Digite uma opção (1..4): ")

            # Opção para inserir dados na lista encadeada:
            if opDespesas == "1":
                valor, id = self.adicionarDados(idDespesas)
                idDespesas = id
                print(" Despesa cadastrada com sucesso!")
                print()
                lista.append(valor)
                time.sleep(1)
                os.system("cls")
                TelaDespesas.headerDespesas()
                self.listar(lista)
                TelaDespesas.menuDespesas()
                TelaDespesas.footerDespesas()

            # Opção para remover dados da lista encadeada:
            if opDespesas == "2":
                print()
                valor = int(input(" Digite o código a ser excluído: "))
                resultado = self.deleteItem(lista, valor)
                lista.remove(resultado)
                os.system("cls")
                TelaDespesas.headerDespesas()
                self.listar(lista)
                TelaDespesas.menuDespesas()
                TelaDespesas.footerDespesas()

            # Opções para gerar arquivo em PDF a partir dos dados da lista encadeda:
            if opDespesas == "3":
                print(" Gerar pdf...")
        return lista, idDespesas

    # Criando método para consultar dados da lista encadeada:
    def listar(self, lista):
        totalDespesas = 0
        for item in lista:
            if isinstance(item, Despesa):
                val = locale.currency(item.getValor(), grouping=True)
                print(" | |" + '\033[31m' + '{:^4}'.format(item.getId()) + '\x1b[0m' +
                      " | " + '\033[31m' + '{:<30}'.format(item.getNome()) + '\x1b[0m' +
                      " | " + '\033[31m' + '{:<20}'.format(item.getTipo()) + '\x1b[0m' +
                      " | " + '\033[31m' + '{:^10}'.format(str(item.getData())) + '\x1b[0m' +
                      " | " + '\033[31m' + '{:>19}'.format(val) + '\x1b[0m' + " | |")
                print(" | +" + "-" * 5 +
                      "+" + "-" * 32 +
                      "+" + "-" * 22 +
                      "+" + "-" * 12 +
                      "+" + "-" * 21 + "+ |")
                totalDespesas = totalDespesas + item.getValor()
        print(" |" + " " * 70 + "TOTAL: " + '{:>20}'.format(locale.currency(totalDespesas, grouping=True)) + "   |")

    # Criando método para inserir dados na lista encadeada:
    def adicionarDados(self, size):
        id = size + 1
        despesaObj = Despesa()
        despesaObj.setId(id)
        print()
        despesaObj.setNome(input(" Despesa: "))
        despesaObj.setTipo(input(" Tipo de despesa: "))
        despesaObj.setValor(float(input(" Valor: ")))
        despesaObj.setData(input(" Data (dd/mm/yyyy): "))
        return despesaObj, id

    # Criando método para remover dados da lista encadeada:
    def deleteItem(self, lista, valor):
        for item in lista:
            if isinstance(item, Despesa):
                if item.getId() == valor:
                    return item

    # Criando método estático para o cabeçalho:
    @staticmethod
    def headerDespesas():
        print()
        print(" +" + "-" * 100 + "+")
        print(" |" + '{:^100}'.format(" Controle Financeiro ") + "|")
        print(" +" + "-" * 100 + "+")
        print(" +" + '{:-^100}'.format(" Despesas ") + "+")
        print(" |" + " " * 100 + "|")
        print(" | +" + "-" * 5 +
              "+" + "-" * 32 +
              "+" + "-" * 22 +
              "+" + "-" * 12 +
              "+" + "-" * 21 + "+ |")
        print(" | |" + '\033[31m' + '{:^4}'.format("ID") + '\x1b[0m' +
              " | " + '\033[31m' + '{:^30}'.format("DESPESA") + '\x1b[0m' +
              " | " + '\033[31m' + '{:^20}'.format("TIPO DE DESPESA") + '\x1b[0m' +
              " | " + '\033[31m' + '{:^10}'.format("DATA") + '\x1b[0m' +
              " | " + '\033[31m' + '{:^20}'.format("VALOR") + '\x1b[0m' + "| |")
        print(" | +" + "-" * 5 +
              "+" + "-" * 32 +
              "+" + "-" * 22 +
              "+" + "-" * 12 +
              "+" + "-" * 21 + "+ |")

    # Criando método estático para o menu:
    @staticmethod
    def menuDespesas():
        print(" |" + " " * 100 + "|")
        print(" |" + '{:^100}'.format("(1) Inserir  (2) Excluir  (3) Gerar PDF  (4) Voltar") + "|")
        print(" |" + " " * 100 + "|")
        print(" +" + "-" * 100 + "+")

    # Criando método estático para o rodapé:
    @staticmethod
    def footerDespesas():
        print(" +" + "-" * 100 + "+")
        data = datetime.now()
        print(" |" + '{:^100}'.format("Aracaju (SE), " + str(data.strftime('%d/%m/%Y %H:%M'))) + "|")
        print(" +" + "-" * 100 + "+")
