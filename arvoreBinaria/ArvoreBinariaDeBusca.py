from arvoreBinaria.ArvoreBinaria import ArvoreBinaria
from arvoreBinaria.Node import Node

RAIZ = "raiz"


class ArvoreBinariaDeBusca(ArvoreBinaria):

    v=[]

    def insert(self, value):
        parent = None
        x = self.root
        while x:
            parent = x
            if value.getNome() < x.key:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(key=value.getNome(), data=value)
        elif value.getNome() < parent.key:
            parent.left = Node(key=value.getNome(), data=value)
        else:
            parent.right = Node(key=value.getNome(), data=value)

    def search(self, value):
        self.v = []
        li = self._search(value, self.root)
        return li

    def _search(self, value, node):
        if node is None:
            return self.v
        if node.key == value:
            self.v.append(node.data)
        if value < node.key:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def menor(self, node=RAIZ):
        if node == RAIZ:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def maior(self, node=RAIZ):
        if node == RAIZ:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node=RAIZ):
        if node == RAIZ:
            node = self.root
        if node is None:
            return node
        if value < node.key:
            node.left = self.remove(value, node.left)
        elif value > node.key:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.menor(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)
        return node
