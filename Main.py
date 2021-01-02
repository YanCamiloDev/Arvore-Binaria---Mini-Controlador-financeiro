from telas.TelaHome import TelaHome
from telas.TelaReceitas import TelaReceitas
from telas.TelaDespesas import TelaDespesas
from telas.TelaSaldo import TelaSaldo
from linkedList.LinkedList import LinkedList
from arvoreBinaria.ArvoreBinariaDeBusca import ArvoreBinariaDeBusca
from telas.TelaPesquisa import TelaPesquisa
import os

# Criando o código principal:
if __name__ == '__main__':

    # Instanciando classes:
    listaReceitas = LinkedList()
    listaDespesas = LinkedList()
    receita = TelaReceitas()
    despesas = TelaDespesas()
    saldo = TelaSaldo()
    idsReceitas = 0
    idsDespesas = 0

    # Opções do módulo principal:
    op_home = "0"
    while op_home != "5":
        os.system("cls")
        TelaHome.render()
        op_home = input(" Digite uma opção (1..5): ")

        # Opção referente a receitas financeiras:
        if op_home == "1":
            # Aplicação de lista encadeada:
            novaLista, idAtual = receita.render(listaReceitas, idsReceitas)
            if novaLista is not None:
                listaReceitas = novaLista
                idsReceitas = idAtual

        # Opção referente a despesas financeiras:
        if op_home == "2":
            # Aplicação de lista encadeada:
            novaLista, idAtual = despesas.render(listaDespesas, idsDespesas)
            if novaLista is not None:
                listaDespesas = novaLista
                idsDespesas = idAtual

        # Opção referente ao saldo financeiro:
        if op_home == "3":
            # Aplicação de lista encadeada:
            saldo.render(listaDespesas.getItem() + listaReceitas.getItem())

        # Opção referente à pesquisa de dados:
        if op_home == "4":
            # Aplicação de árvore binária de busca:
            linkedListDespesas = listaDespesas.getItem()
            linkedListReceitas = listaReceitas.getItem()
            listaJoin = linkedListDespesas + linkedListReceitas
            if len(listaJoin) > 0:
                arvore = ArvoreBinariaDeBusca(listaJoin.pop(0))
                for li in listaJoin:
                    arvore.insert(li)
                TelaPesquisa().pesquisar(arvore)
