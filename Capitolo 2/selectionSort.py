
def findMin(lista:list): #funzione che cerca il numero minimino in un'array
    minimo = lista[0]
    for i in range(len(lista)):
        if(lista[i]<minimo):
            minimo=lista[i]
    return lista.index(minimo)

def selectionSort(lista:list):
    listaOrdinata = [] #lista da ritornare
    for i in range(len(lista)):
        index = findMin(lista) #Prendo l'indice del valore più piccolo
        listaOrdinata.append(lista[index]) #lo aggiungo alla lista da ritornare
        lista.pop(index) #lo rimuovo dall'array iniziale 
    return listaOrdinata

print(selectionSort([9,3,4,6,32,11,9,8]))#[3, 4, 6, 8, 9, 9, 11, 32]

    
