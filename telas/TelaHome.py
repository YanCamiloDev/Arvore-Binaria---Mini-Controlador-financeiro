from datetime import datetime


# Criando classe:
class TelaHome:

    # Criando método estático para juntar cabeçalho, menu e rodapé:
    @staticmethod
    def render():
        TelaHome.headerHome()
        TelaHome.menuHome()
        TelaHome.footerHome()

    # Criano método estático para cabeçalho:
    @staticmethod
    def headerHome():
        print()
        print(" +" + "-" * 100 + "+")
        print(" |" + '{:^100}'.format(" Controle Financeiro ") + "|")
        print(" +" + "-" * 100 + "+")
        print(" +" + '{:-^100}'.format(" Home ") + "+")

    # Criando método estático para o menu:
    @staticmethod
    def menuHome():
        print('{:<102}'.format(" | 1 - Receitas") + "|")
        print('{:<102}'.format(" | 2 - Despesas") + "|")
        print('{:<102}'.format(" | 3 - Saldo") + "|")
        print('{:<102}'.format(" | 4 - Pesquisar") + "|")
        print('{:<102}'.format(" | 5 - Sair") + "|")
        print(" +" + "-" * 100 + "+")

    # Criando método estático para o rodapé:
    @staticmethod
    def footerHome():
        print(" +" + "-" * 100 + "+")
        data = datetime.now()
        print(" |" + '{:^100}'.format("Aracaju (SE), " + str(data.strftime('%d/%m/%Y %H:%M'))) + "|")
        print(" +" + "-" * 100 + "+")
