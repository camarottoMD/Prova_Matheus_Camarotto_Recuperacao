biblioteca = [{'usuario':'matheus','paginas':9},{'usuario':'felipe','paginas':9},{'usuario':'gabriel','paginas':2}]

def leitura(dictBiblio, min=5):
    lista2 = []
    for user in dictBiblio:
        if user['paginas'] > min:
            lista2.append(user['usuario'])
    print(f'Os usuarios que fizeram a leitura mínima díaria são: {lista2}')

leitura(biblioteca)