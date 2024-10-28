#CRIA UMA FUNÇÃO CHAMADA SELECTON_SORT QUE TEM COMO PARÂMETRO list
def selection_sort(lista):
    #ESSE N VAI LER A QUANTIDADE DE ITENS QUE TEM NA LISTA
    n = len(lista)
    # PERCORRA N E ARMAZENE EM I CADA ITERAÇÃO 
    for i in range(n):

        min_index = i
    for j in range(i + 1, n):
        if lista[j] < lista[min_index]:
            min_index = j
    lista[i], lista[min_index] = lista[min_index], lista[1]

valores = [64,25,23,]
print("Antes da ordem:", valores)
selection_sort(valores)
print("Depois de ordenar:", valores)
