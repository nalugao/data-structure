#funcao recursiva que conta o numero de elementos na lista

def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:])

print(conta([2, 5, 7]))