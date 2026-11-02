#pegue uma lista
#se a lista estiver vazia, retorne zero
#se não, a soma total será o primeiro número da lista + a soma do restante da lista

def soma(lista):

    if len(lista) == 0:
        return 0
    return lista[0] + soma(lista[1:])

print(soma([1, 4, 2, 3]))