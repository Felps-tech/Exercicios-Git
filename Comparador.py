try:
    a = str(input("Primeira String "))
    b = str(input("Segunda String "))
    if len(a) != len(b):
        raise Exception("Comprimentos diferentes")
    print("Comprimentos iguais")
except Exception as e:
    print(e)