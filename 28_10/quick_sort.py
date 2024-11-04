def quick_sort(lista):
    if len(lista) <= 1:
        return lista  
    pivo = lista[0] 
    # O I COMEÇA NO SEGUNDO ELEMENTO, POIS O PRIMEIRO 
    i = 1
    #O J COMEÇA NO ÚLTIMO ELEMENTO
    j = len(lista) - 1 
    #ESSE PRIMEIRO LOOP ORGANIZA OS ELEMENTOS QUE ESTÃO ERRADOS EM RELAÇÃO AO PIVÔ
    #ESSE LOOP VAI CONTINUAR ENQUANTO O I FOR MENOR QUE J
    while i < j:
        while i <= j and lista[i] <= pivo:
            i += 1
        while i <= j and lista[j] > pivo:
            j -= 1
        
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]

    lista[0], lista[j] = lista[j], lista[0]
    
    esquerda = quick_sort(lista[:j])
    direita =  quick_sort(lista[j+1:])

    return esquerda + [lista[j]] + direita

lista = [3, 7, 8, 5, 2, 1, 9, 6, 4]
print(f"Antes de ordenar: {lista}")
lista_ordenada = quick_sort(lista)
print(f"Depois de ordenar: {lista_ordenada}")