'''gastos = {'moradia':[('matheus',100),('matheus',100)],'alimentação':[('matheus',100),('matheus',100)], 'educacao':[('matheus',100),('matheus',100)]}'''

def orcamento(dicionario):
    gasto_categoria = {}
    for categoria in dicionario.items():
        for nome in categoria:
            

    return gasto_categoria
orcamento(gastos)

















'''
gastos = {'moradia':[('matheus',100),('matheus',100)]},{'alimentação':[('matheus',100),('matheus',100)]}, {'educacao':[('matheus',100),('matheus',100)]}

def orcamento(dicionario):
    gasto_categoria = {}
    for categoria in dicionario:
        print(categoria)
        for lista in categoria.values():
            for nome, valor in lista:
                nome = nome.lower()
                if nome not in gasto_categoria:
                    gasto_categoria[nome] = 0
                gasto_categoria[nome] += valor
    return gasto_categoria
print(orcamento(gastos))'''