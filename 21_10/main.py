def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = 1
    for j in range(i + 1, n):
        if lista[j] < lista[min_index]:
            min_index = j
    lista[i], lista[min_index] = lista[min_index], lista[1]

    valores = [64,25]
    print("Antes da ordem:", valores)
    selection_sort(valores)
    print("Depois de ordenar:", valores)
    