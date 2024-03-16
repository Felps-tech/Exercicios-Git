with open('exame.txt', 'r') as arq:
    linhas = arq.readlines()
num_linhas = len(linhas)
notas = [float(input(f'Nota do exame do aluno {i + 1}: ')) for i in range(num_linhas)]
for i in range(num_linhas):
    linha = linhas[i].strip().split(': ')
    linha[-1] = f'{linha[-1].strip()}, {notas[i]:.1f}'
    linhas[i] = ': '.join(linha) + '\n'
with open('exame.txt', 'w') as arq:
    arq.writelines(linhas)