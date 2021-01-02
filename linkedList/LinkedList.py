from linkedList.Node import Node
from model.Movimentacao import Movimentacao


class LinkedList:

    def __init__(self):
        self.cabeca = None
        self._size = 0

    def append(self, element):
        # SÓ PODEM SER ADICIONADOS ELEMENTOS DE MOVIMENTAÇÃO (RECEITA OU DESPESA)
        if isinstance(element, Movimentacao):
            if self.cabeca:
                pointer = self.cabeca
                while pointer.next:
                    pointer = pointer.next
                pointer.next = Node(element)
            else:
                self.cabeca = Node(element)
            self._size = self._size + 1

    # ORDENAR A LINKED LIST
    def orderLista(self):
        return sorted(self, key=lambda a: a, reverse=False)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        pointer = self.cabeca
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def getItem(self):
        l=[]
        node = self.cabeca
        while node:
            l.append(node.data)
            node = node.next
        return l

    def __setitem__(self, index, elem):
        pointer = self.cabeca
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")

        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def pop(self):
        valor = self.cabeca.data
        self.cabeca = self.cabeca.next
        self._size = self._size - 1
        return valor

    def remove(self, valor):
        assert self.cabeca, "Impossível remover valor de lista vazia."
        if self.cabeca.data == valor:
            self.cabeca = self.cabeca.next
            self._size = self._size - 1
            return True
        else:
            anterior = self.cabeca
            pointer = self.cabeca.next
            while pointer:
                if pointer.data == valor:
                    anterior.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                anterior = pointer
                pointer = pointer.next
        return False

    def index(self, elem):
        pointer = self.cabeca
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
