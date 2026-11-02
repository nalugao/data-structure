def quicksort(array):
    if len(array) < 2:
        return array # caso base
    else:
        array_pivot = array[0] # caso recursivo
        menor = [i for i in array[1:0] if i <= array_pivot]
        maior = [i for i in array[1:] if i > array_pivot]
        return quicksort(menor) + [array_pivot] + quicksort(maior)

print(quicksort([10, 5, 2, 3]))