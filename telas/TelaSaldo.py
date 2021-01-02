from datetime import datetime
from linkedList.LinkedList import LinkedList
from model.Resumo import Resumo
import locale
import os


class TelaSaldo:

    def __init__(self):
        self.listaGeral = LinkedList()

    def render(self, lista):
        self.listaGeral = lista
        os.system("cls")
        TelaSaldo.headerSaldo()
        # GERAR RELATÓTIO
        l = Resumo().relatorioMovimentacoes(lista)
        # LISTAR
        self.listar(l)
        print(" +" + "-" * 100 + "+")
        TelaSaldo.footerSaldo()
        input(' Voltar >>>')
        os.system('cls')


    # Criando método estático para o cabeçalho:
    @staticmethod
    def headerSaldo():
        print()
        print(" +" + "-" * 100 + "+")
        print(" |" + '{:^100}'.format(" Controle Financeiro ") + "|")
        print(" +" + "-" * 100 + "+")
        print(" +" + '{:-^100}'.format(" Saldo ") + "+")
        print(" |" + " " * 100 + "|")
        print(" | +" + "-" * 18 +
              "+" + "-" * 27 +
              "+" + "-" * 27 +
              "+" + "-" * 21 + "+ |")
        print(" | |" + '{:^17}'.format("PERÍODO") +
              " | " + '\033[92m' + '{:^25}'.format("RECEITA") + '\x1b[0m' +
              " | " + '\033[31m' + '{:^25}'.format("DESPESA") + '\x1b[0m' +
              " | " + '\033[1;34m' + '{:^20}'.format("SALDO") + '\033[0;00m' + "| |")
        print(" | +" + "-" * 18 +
              "+" + "-" * 27 +
              "+" + "-" * 27 +
              "+" + "-" * 21 + "+ |")

    # Criando método estático para o rodapé:
    @staticmethod
    def footerSaldo():
        print(" +" + "-" * 100 + "+")
        data = datetime.now()
        print(" |" + '{:^100}'.format("Aracaju (SE), " + str(data.strftime('%d/%m/%Y %H:%M'))) + "|")
        print(" +" + "-" * 100 + "+")

    def listar(self, lista):
        saldoTot=0
        for item in lista:
            print(" | |" + '{:^17}'.format(str(str(item.getPeriodo().month) + '/' + str(item.getPeriodo().year))) +
                  " | " + '\033[92m' + '{:>25}'.format(locale.currency(item.getReceitas(), grouping=True)) + '\x1b[0m' +
                  " | " + '\033[31m' + '{:>25}'.format(locale.currency(item.getDespesas(), grouping=True)) + '\x1b[0m' +
                  " | " + '\033[1;34m' + '{:>19}'.format(locale.currency(item.getSaldo(), grouping=True)) + '\033[0;00m' + " | |")
            print(" | +" + "-" * 18 +
                  "+" + "-" * 27 +
                  "+" + "-" * 27 +
                  "+" + "-" * 21 + "+ |")
            saldoTot += item.getSaldo()
        print(" |" + " " * 70 + "TOTAL: " + '{:>20}'.format(locale.currency(saldoTot, grouping=True)) + "   |")
