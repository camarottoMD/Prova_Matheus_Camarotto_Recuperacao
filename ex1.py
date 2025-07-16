agenda = [('lucas', 8),('joão', 8),('pedro', 2),('maria', 3),('gabriela', 6)]

def consultas(lista):
    lista2 = []
    for nome, consulta in lista:
        if consulta > 3 :
            lista2.append(nome)
    print(f'Os pacientes com mais de três consultas marcadas são:{lista2}')

consultas(agenda)