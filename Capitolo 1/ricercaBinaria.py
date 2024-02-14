
def binary_search(list, item):
    low = 0  #Indice iniziale
    high = len(list)-1 #Indice finale
    
    while low <= high: #Il ciclo continua fino a quando l'indice finale sarà minore o uguale di quello iniziale
        mid = (low+high) // 2 #Calcolo del indice centrale
        guess = list[mid] # viene preso il valore centrale nell'array
        global nPassaggi
        nPassaggi = nPassaggi + 1 
        if guess == item: 
            return mid # se è uguale verrà semplicemente ritornato
        
        if guess > item: # in questo caso il valore si trova nella prima parte dell'array
            high = mid - 1 # essendo nella prima parte dell'array l'indice finale sarà l'indice del valore centrale -1

        if guess < item: # in questo caso il valore si trova nella seconda parte dell'array
            low = mid + 1  # essendo nella seconda parte dell'array l'indice iniziale sarà l'indice del valore centrale -1

def regular_search(list,item):

    for x in range(len(list)):
        global nPassaggi
        nPassaggi = nPassaggi + 1
        if(list[x]==item):
            return x


listaNomi = ['Alessandro', 'Carlo', 'Giovanni', 'Luca', 'Marco', 'Matteo', 'Pippo', 'Pluto', 'Sebastiano'] # creazione lista
nomeDaCercare = "Pluto" # nome da cercare nella lista

nPassaggi = 0 # numero dei passaggi
nameIndex = binary_search(listaNomi,nomeDaCercare)
print("Il nome '"+nomeDaCercare+"' è stato trovato nella posizione "+str(nameIndex)+" in "+str(nPassaggi)+" passaggi con la ricerca binaria")

nPassaggi = 0 # numero dei passaggi
nameIndex = regular_search(listaNomi,nomeDaCercare)
print("Il nome '"+nomeDaCercare+"' è stato trovato nella posizione "+str(nameIndex)+" in "+str(nPassaggi)+" passaggi con la ricerca lineare")

# Il nome 'Pluto' è stato trovato nella posizione 8 in 3 passaggi con la ricerca binaria
# Il nome 'Pluto' è stato trovato nella posizione 8 in 9 passaggi con la ricerca lineare