# Módulo para testes

# Importando módulos:
from model.Despesa import Despesa
from model.Receita import Receita

# Testando:
r = Receita()
r.setNome('hugo')
r.setData()
r.setValor(23.2)
d = Despesa()
d.setNome('jose')
d.setData()
d.setValor(345.65)
arv = ArvoreBinariaDeBusca(r)
arv.insert(d)
lia = arv.search('jose')

for movimentacao in lia:
    print(' NOME: ', movimentacao.getNome())
    print(' DATA: ', movimentacao.getData())
    print(' VALOR: ', movimentacao.getValor())
    print()