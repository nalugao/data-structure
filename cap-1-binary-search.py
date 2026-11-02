def pesquisa_binaria(lista, item):
    inicio = 0
    fim = len(lista)

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9, 12]

print(pesquisa_binaria(minha_lista, 3))