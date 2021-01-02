# Módulo para pesquisar os dados

# Importando módulos:
from datetime import datetime
from model.Despesa import Despesa
import os
import locale


# Criando classe para pesquisar dados:
class TelaPesquisa:
    # Criando método para padronizar os dados em moeda real:
    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

    # Criando método para operacionalizar a árvore binária:
    def pesquisar(self, arvoreDeBusca):
        os.system("cls")
        TelaPesquisa.headerDespesas()
        print(" +" + "-" * 100 + "+")
        TelaPesquisa.footerDespesas()
        nome = input(" Digite o termo pesquisado: ")

        # Procurando o termo na árvore binária:
        encontrados = arvoreDeBusca.search(nome)
        if encontrados:
            os.system("cls")
            TelaPesquisa.headerDespesas()
            totalSaldo = 0
            for movimentacao in encontrados:
                if isinstance(movimentacao, Despesa):
                    print(" | |" + '\033[31m' + '{:^14}'.format('DESPESA') + '\x1b[0m' +
                          " | " + '\033[31m' + '{:<20}'.format(movimentacao.getNome()) + '\x1b[0m' +
                          " | " + '\033[31m' + '{:<20}'.format(movimentacao.getTipo()) + '\x1b[0m' +
                          " | " + '\033[31m' + '{:^10}'.format(str(movimentacao.getData())) + '\x1b[0m' +
                          " | " + '\033[31m' + '{:>20}'.format(locale.currency(movimentacao.getValor(), grouping=True))
                          + '\x1b[0m' + "| |")
                else:
                    print(" | |" + '\033[92m' + '{:^14}'.format('RECEITA') + '\x1b[0m' +
                          " | " + '\033[92m' + '{:<20}'.format(movimentacao.getNome()) + '\x1b[0m' +
                          " | " + '\033[92m' + '{:<20}'.format(movimentacao.getTipo()) + '\x1b[0m' +
                          " | " + '\033[92m' + '{:^10}'.format(str(movimentacao.getData())) + '\x1b[0m' +
                          " | " + '\033[92m' + '{:>20}'.format(locale.currency(movimentacao.getValor(), grouping=True))
                          + '\x1b[0m' + "| |")
                totalSaldo = totalSaldo + movimentacao.getValor()
            print(" | +" + "-" * 15 +
                  "+" + "-" * 22 +
                  "+" + "-" * 22 +
                  "+" + "-" * 12 +
                  "+" + "-" * 21 + "+ |")
            print(" +" + "-" * 100 + "+")
            TelaPesquisa.footerDespesas()
            input('  Voltar >>>')
            os.system('cls')

    # Criando método estático para o cabeçalho:
    @staticmethod
    def headerDespesas():
        print()
        print(" +" + "-" * 100 + "+")
        print(" |" + '{:^100}'.format(" Controle Financeiro ") + "|")
        print(" +" + "-" * 100 + "+")
        print(" +" + '{:-^100}'.format(" Pesquisa ") + "+")
        print(" |" + " " * 100 + "|")
        print(" | +" + "-" * 15 +
              "+" + "-" * 22 +
              "+" + "-" * 22 +
              "+" + "-" * 12 +
              "+" + "-" * 21 + "+ |")
        print(" | |" + '{:^14}'.format("MOVIMENTAÇÃO") +
              " | " + '{:^20}'.format("NOME") +
              " | " + '{:^20}'.format("TIPO") +
              " | " + '{:^10}'.format("DATA") +
              " | " + '{:^20}'.format("VALOR") + "| |")
        print(" | +" + "-" * 15 +
              "+" + "-" * 22 +
              "+" + "-" * 22 +
              "+" + "-" * 12 +
              "+" + "-" * 21 + "+ |")

    # Criando método estático para o rodapé:
    @staticmethod
    def footerDespesas():
        print(" +" + "-" * 100 + "+")
        data = datetime.now()
        print(" |" + '{:^100}'.format("Aracaju (SE), " + str(data.strftime('%d/%m/%Y %H:%M'))) + "|")
        print(" +" + "-" * 100 + "+")
