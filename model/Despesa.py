# Módulo dos métodos setters e getters das despesas financeiras

# Importando módulo:
from model import Movimentacao

# HERANÇA
class Despesa(Movimentacao.Movimentacao):

    # Construtor
    def __init__(self):
        super().__init__()
