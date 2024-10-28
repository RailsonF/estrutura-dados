def quick_sort(lista):
    if len(lista) <= 1:
        return lista  
    pivot = lista[0] 
    i = 1
    j = len(lista) - 1

    while i < j:
        
        while i <= j and lista[i] <= pivot:
            i += 1
        
        while i <= j and lista[j] > pivot:
            j -= 1

        
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]

    lista[0], lista[j] = lista[j], lista[0]
    
    quick_sort(lista[:j])
    quick_sort(lista[j+1:])

    return lista

lista = [3, 7, 8, 5, 2, 1, 9, 6, 4]
lista_ordenada = quick_sort(lista)
print(lista_ordenada)