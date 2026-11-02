def valor_mais_alto(lista):
    if len(lista) == 0:
        return 0
    else: 
        maior_do_resto = valor_mais_alto(lista[1:])
        if lista[0] > maior_do_resto:
            return lista[0]
        else:
            return maior_do_resto

print(valor_mais_alto([6, 3, 9, 2]))