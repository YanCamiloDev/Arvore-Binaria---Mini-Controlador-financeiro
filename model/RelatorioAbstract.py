# Módulo da classe abstrata

# Importando módulo:
from abc import ABC, abstractmethod


# Criando classe abstrata para conta:
class RelatorioAbstract(ABC):

    # Método abstrato para calcular saldo financeiro:
    @abstractmethod
    def calcularSaldo(self, lista):
        pass

    # Método abstrato para relatório de movimentações:
    @abstractmethod
    def relatorioMovimentacoes(self, lista):
        pass
