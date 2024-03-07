try:
    a = int(input())
    if a == 0:
        raise Exception("Valor igual 0")
    a = a/10
    print(a)
except Exception as e:
    print(e)
