with open("notas.txt", "w") as notas:
    while True:
        nota = input('Coloque dados do estudante (nome[nota1,nota2,nota3], e depois escreva "FIM" para terminar):')
        if nota.upper() == "FIM":
            break
        notas.write(f"{nota}\n")
        