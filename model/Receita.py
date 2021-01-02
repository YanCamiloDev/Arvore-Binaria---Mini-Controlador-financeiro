# Módulo dos métodos setters e getters das receitas financeiras

# Importando módulo:
from model import Movimentacao

# HERANÇA
class Receita(Movimentacao.Movimentacao):

    # Cronstrutor
    def __init__(self):
        super().__init__()
