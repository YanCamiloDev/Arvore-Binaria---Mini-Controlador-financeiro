from datetime import datetime
import locale


class Movimentacao:

    # Criando método para padronizar os dados em moeda real:
    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

    # Construtor
    def __init__(self, id=0, valor=0.0, tipo="", data=None, nome=""):
        # ENCAPSULAMENTO (O UNDERLINE DEFINE COMO PRIVATE)
        self._id = id
        self._valor = valor
        self._tipo = tipo
        self._data = data
        self._nome = nome

    # Criando métodos setters para alterar os atributos para as movimentações financeiras:
    def setId(self, id):
        self._id = id

    def setNome(self, nome):
        self._nome = nome

    def setData(self, data):
        dataCap = datetime.strptime(data, '%d/%m/%Y').date()
        self._data = dataCap

    def setValor(self, valor):
        self._valor = valor

    def setTipo(self, tipo):
        self._tipo = tipo

    # Criando métodos getters para consultar os atributos para as movimentações financeiras:
    def getId(self):
        return self._id

    def getNome(self):
        return self._nome

    def getTipo(self):
        return self._tipo

    def getData(self):
        return self._data

    def getValor(self):
        return self._valor
