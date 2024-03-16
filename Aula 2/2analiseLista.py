def addLinha(linha):
    parte = linha.strip().split('[')
    nome = parte[0].strip()
    notaStr = parte[1].strip(']')
    notas = [float(x.strip()) for x in notaStr.split(',')]

    return {'nome': nome, 'nota': notas}

with open("notas.txt", "r") as arq:
    alunos = [addLinha(linha) for linha in arq]

with open("aprovado.txt", "w") as aprovado, open("exame.txt", "w") as exame, open("reprovado.txt", "w") as reprovado:
    for aluno in alunos:
        media = (sum(aluno['nota']) / 3)
        if media >= 7:
            aprovado.write(f"{aluno['nome']}: {media}\n")
        elif media < 7 and media >= 5:
            exame.write(f"{aluno['nome']}: {media}\n")
        else:
            reprovado.write(f"{aluno['nome']}: {media}\n")