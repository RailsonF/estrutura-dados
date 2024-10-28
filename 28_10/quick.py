def quick_sort(lista):
    if len(lista) <=1:
        return lista
    pivo = lista[0]
    i = 1
    j = len(lista) -1

    while i < j:
        while i <= j and lista[i] <= pivo:
            i+=1
        while i <=j and lista[i] > pivo:
            j-=1
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]
            
    lista[0], lista[j] = lista[j], lista[0]        
  
    quick_sort(lista[:j])
    quick_sort(lista[j+1:])
    
    return lista

lista_desordenada = [3, 7, 8, 5, 2, 1, 9, 6, 4]
lista_ordenada = quick_sort(lista_desordenada)
print(lista_ordenada)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #for i in range(lista):
       #if i < lista[0]:
'''    
    Python
def quick_sort(lista):
    """Implementa o algoritmo Quick Sort usando for e if.

    Args:
        lista: A lista a ser ordenada.

    Returns:
        A lista ordenada.
    """

    if len(lista) <= 1:
        return lista  # Lista com 1 ou menos elementos já está ordenada

    # Escolhendo o pivô (primeiro elemento nesse exemplo)
    pivo = lista[0]
    # Inicializando índices para percorrer a lista
    i = 1
    j = len(lista) - 1

    while i <= j:
        # Encontrar um elemento maior ou igual ao pivô
        while i <= j and lista[i] <= pivo:
            i += 1
        # Encontrar um elemento menor ou igual ao pivô
        while i <= j and lista[j] > pivo:
            j -= 1

        # Se os índices ainda não se cruzaram, trocar os elementos
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]

    # Colocar o pivô na posição correta
    lista[0], lista[j] = lista[j], lista[0]

    # Chamadas recursivas para ordenar as sublistas
    quick_sort(lista[:j])
    quick_sort(lista[j+1:])

    return lista

# Exemplo de uso
lista_desordenada = [3, 7, 8, 5, 2, 1, 9, 6, 4]
lista_ordenada = quick_sort(lista_desordenada)
print(lista_ordenada)       
'''