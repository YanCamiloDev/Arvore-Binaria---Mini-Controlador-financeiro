# Módulo da tela das receitas financeiras

# Importando módulos:
from datetime import datetime
from model.Receita import Receita
from linkedList.LinkedList import LinkedList
import os
import locale
import time


# Criando classe para as receitas financeiras:
class TelaReceitas:
    # Criando método para padronizar os dados em moeda real:
    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

    # Criando médoto para operacionalizar a lista encadeada:
    def render(self, lista=LinkedList(), idsLista=0):
        idFinal = idsLista
        # Opções do módulo das receitas financeiras:
        opReceitas = "0"
        while opReceitas != "4":
            os.system("cls")
            TelaReceitas.headerReceitas()
            self.listar(lista)
            TelaReceitas.menuReceitas()
            TelaReceitas.footerReceitas()
            opReceitas = input(" Digite uma opção (1..4): ")

            # Opção para inserir dados na lista encadeada:
            if opReceitas == "1":
                valor, novoId = self.adicionarDados(idFinal)
                print(" Receita cadastrada com sucesso!")
                print()
                idFinal = novoId
                lista.append(valor)
                time.sleep(1)
                os.system("cls")
                TelaReceitas.headerReceitas()
                self.listar(lista)
                TelaReceitas.menuReceitas()
                TelaReceitas.footerReceitas()

            # Opção para remover dados da lista encadeada:
            if opReceitas == "2":
                print()
                valor = int(input(" Digite o código a ser excluído: "))
                resultado = self.deleteItem(lista, valor)
                lista.remove(resultado)
                os.system("cls")
                TelaReceitas.headerReceitas()
                self.listar(lista)
                TelaReceitas.menuReceitas()
                TelaReceitas.footerReceitas()

            # Opções para gerar arquivo em PDF a partir dos dados da lista encadeda:
            if opReceitas == "3":
                print(" Gerar pdf...")
        return lista, idFinal

    # Criando método para consultar dados da lista encadeada:
    def listar(self, lista):
        totalReceitas = 0
        for item in lista:
            if isinstance(item, Receita):
                val = locale.currency(item.getValor(), grouping=True)
                print(" | |" + '\033[92m' + '{:^4}'.format(item.getId()) + '\x1b[0m' +
                      " | " + '\033[92m' + '{:<30}'.format(item.getNome()) + '\x1b[0m' +
                      " | " + '\033[92m' + '{:<20}'.format(item.getTipo()) + '\x1b[0m' +
                      " | " + '\033[92m' + '{:^10}'.format(str(item.getData())) + '\x1b[0m' +
                      " | " + '\033[92m' + '{:>19}'.format(val) + '\x1b[0m' + " | |")
                print(" | +" + "-" * 5 +
                      "+" + "-" * 32 +
                      "+" + "-" * 22 +
                      "+" + "-" * 12 +
                      "+" + "-" * 21 + "+ |")
                totalReceitas = totalReceitas + item.getValor()
        print(" |" + " " * 70 + "TOTAL: " + '{:>20}'.format(locale.currency(totalReceitas, grouping=True)) + "   |")

    # Criando método para inserir dados na lista encadeada:
    def adicionarDados(self, size):
        id = size + 1
        receitaOBJ = Receita()
        receitaOBJ.setId(size + 1)
        print()
        receitaOBJ.setNome(input(" Receita: "))
        receitaOBJ.setTipo(input(" Tipo de receita: "))
        receitaOBJ.setValor(float(input(" Valor: ")))
        receitaOBJ.setData(str(input(" Data (dd/mm/yyyy): ")))
        return receitaOBJ, id

    # Criando método para remover dados da lista encadeada:
    def deleteItem(self, lista, valor):
        for item in lista:
            if isinstance(item, Receita):
                if item.getId() == valor:
                    return item

    # Criando método estático para o cabeçalho:
    @staticmethod
    def headerReceitas():
        print()
        print(" +" + "-" * 100 + "+")
        print(" |" + '{:^100}'.format(" Controle Financeiro ") + "|")
        print(" +" + "-" * 100 + "+")
        print(" +" + '{:-^100}'.format(" Receitas ") + "+")
        print(" |" + " " * 100 + "|")
        print(" | +" + "-" * 5 +
              "+" + "-" * 32 +
              "+" + "-" * 22 +
              "+" + "-" * 12 +
              "+" + "-" * 21 + "+ |")
        print(" | |" + '\033[92m' + '{:^4}'.format("ID") + '\x1b[0m' +
              " | " + '\033[92m' + '{:^30}'.format("RECEITA") + '\x1b[0m' +
              " | " + '\033[92m' + '{:^20}'.format("TIPO DE RECEITA") + '\x1b[0m' +
              " | " + '\033[92m' + '{:^10}'.format("DATA") + '\x1b[0m' +
              " | " + '\033[92m' + '{:^20}'.format("VALOR") + '\x1b[0m' + "| |")
        print(" | +" + "-" * 5 +
              "+" + "-" * 32 +
              "+" + "-" * 22 +
              "+" + "-" * 12 +
              "+" + "-" * 21 + "+ |")

    # Criando método estático para o menu:
    @staticmethod
    def menuReceitas():
        print(" |" + " " * 100 + "|")
        print(" |" + '{:^100}'.format("(1) Inserir  (2) Excluir  (3) Gerar PDF  (4) Voltar") + "|")
        print(" |" + " " * 100 + "|")
        print(" +" + "-" * 100 + "+")

    # Criando método estático para o rodapé:
    @staticmethod
    def footerReceitas():
        print(" +" + "-" * 100 + "+")
        data = datetime.now()
        print(" |" + '{:^100}'.format("Aracaju (SE), " + str(data.strftime('%d/%m/%Y %H:%M'))) + "|")
        print(" +" + "-" * 100 + "+")
