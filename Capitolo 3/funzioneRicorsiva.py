# Per creare una funzione ricorsiva, abbiamo bisogno che questa si comporti in modo
# diverso in base all'input che le passiamo
def countdown(i):
    print(i)
    if(i < 1): #Caso base
        print("Countdown finito")
        return
    else: #Caso ricorsivo
        countdown(i-1)

countdown(10)
# Esempio di output: 10 9 8 7 6 5 4 3 2 1 0

#Esempio senza condizione
# def countdown(i):
#     print(i)
#     countdown(i-1)
# Esempio di output: 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4....=> all'infinito