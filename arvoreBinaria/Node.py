from model.Movimentacao import Movimentacao


class Node(object):

    def __init__(self, key=None, data=None, left=None, right=None):
        if isinstance(data, Movimentacao):
            self.key = key
            self.data = data
            self.left = left
            self.right = right

    def __str__(self):
        return str(self.data)
