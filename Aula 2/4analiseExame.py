notas = {}
with open('exame.txt', 'r') as arq:
    linhas = arq.readlines()
    for linha in linhas:
        nome, nota_str = linha.strip().split(': ')
        notas[nome] = list(map(float, nota_str.split(', ')))
with open('exameFinal.txt', 'w') as arq:
    for nome, notas_lista in notas.items():
        avg_grade = sum(notas_lista) / len(notas_lista)
        status = 'APROVADO' if avg_grade >= 7 else 'REPROVADO'
        arq.write(f"{nome}: {avg_grade:.1f}, {status}\n");