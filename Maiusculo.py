class ErroMinusculo(Exception):
    pass

try:
    a = str(input())
    if a.isupper() is False:
        raise ErroMinusculo("A string esta com letras minusculas")
    
except ErroMinusculo as E:
    print(E)

else:
    print("A string esta com os maiusculos corretos")