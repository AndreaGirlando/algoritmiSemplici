def greet(name):
    print ("Ciao, " + name + "!")
    greet2(name)
    
    
def greet2(name):
    print ("Come stai, " + name + "?")
    print("Volevo salutarti...")
    bye()

def bye():
    print("Ok, ciao!")
    
greet("Marco")
# output : 
# Ciao, Marco! #! Viene richiamata la funzione greet, le sue variabili vengono caricate in memoria
# Come stai, Marco? #! in greet viene richiamata greet2, le sue variabili vengono caricare in memoria
# Volevo salutarti...
# Ok, ciao! #! in greet2 viene richiamata la funzione bye
# dopo la funzione bye() le funzioni verranno deallocate partendo dall'ultima avviata
# ordine di deallocazione: bye() => greet2() => greet()

