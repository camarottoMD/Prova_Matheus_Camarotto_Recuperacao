turma1 = [('lucas', 9),('joão', 10),('pedro', 2),('maria', 3),('gabriela', 6)]
turma2 = [('gabriel', 9),('caio', 10),('rosana',9),('keudison', 3),('kleber', 6)]

def cursos(*turmas):
    notas = []
    for nome, nota in turmas:
        if nota > 8:
            notas.append(nota)
    soma = sum(notas)
    media = soma / len(notas)
    print(f'Essa foi a media das maiores notas salas {media}')

#filtro = list(filter(lambda nota: nota > 8,))


cursos(*turma1,*turma2)