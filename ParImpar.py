class ErroImpar(Exception):
    pass
try:
    a = int(input("Digite o valor "))
    a = a % 2
    if a == 1:
        raise ErroImpar("O numero é impar")
    
except ErroImpar as E:
    print(E)

else:
    print("O numero é par")