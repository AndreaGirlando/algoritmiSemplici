def fact(x):
    if(x == 1):
        print("Ritorno 1")
        return 1
    else:
        print("Richiamo fact con x =",x)
        temp = x * (fact(x-1))
        print("Sono ritornato da fact con x =",x,"e sto ritornando il valore: ",temp)
        return temp


#Calcoliamo il fattoriale di 3 (3!)

print("Il fattoriale di 3 è: ",fact(3))

# Output:
# Richiamo fact con x = 3 #! alloco in memoria la funzione fact(3) e richiamo fact(2)
# Richiamo fact con x = 2 #! alloco in memoria la funzione fact(2) e richiamo fact(1)
# Ritorno 1  #! ritorno 1 e dealloco fact(1)
# Sono ritornato da fact con x = 2 e sto ritornando il valore:  2 #! grazie al return di fact(1) posso ritornare il risultato a fact(3) e deallocare la funzione
# Sono ritornato da fact con x = 3 e sto ritornando il valore:  6 #! grazie al return di fact(2) posso ritornare il risultato e deallocare la funzione
# Il fattoriale di 3 è:  6 #! stampo il valore ritornato da fact(3)
