from arvoreBinaria.Node import Node


class ArvoreBinaria:

    def __init__(self, data=None):
        if data:
            self.root = Node(key=data.getNome(), data=data)
        else:
            self.root = None

    def ordemSimetrica(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.ordemSimetrica(node.left)
        print(node.data)
        if node.right:
            self.ordemSimetrica(node.right)

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
