# Conversione

# eta = 20 #eta è un intero
# frase = "La mia età è " #frase è una stringa
# print(frase + str(eta))
#===============================================================================================================================
#Stampa su più righe

# print ("""prima linea
# seconda linea
# terza linea""")
#===============================================================================================================================
#Funzione Input()

# nome = input("Scrivi il tuo nome: ")
# print("Ciao" + nome)

# print("Quanti anni hai?")
# eta = input()
# etaNum = 21
# print("Hai " + eta + " anni")
# print(type(eta))
# print(str(etaNum) + " è di tipo " + str(type(etaNum)))

# robot_name = "Chappie"
# robot_age = 1
# print("Ciao! Il mio nome è: " + robot_name + " e ho " + str(robot_age) + " anno")
# user_name = input("Tu come ti chiami? ")
# print("Ciao " + user_name + "!")
# user_age = int(input("Quanti anni hai? "))
# age_difference = user_age - robot_age
# print(str(user_age) + " anni!? Sono " + str(age_difference) + " più di me!")
# print("A presto!")
#===============================================================================================================================
#Booleani
# vero = True
# print(vero)
# print(str(type(vero)))
#===============================================================================================================================
#Comparatori

#==
#!=
#&&
#||
#<
#>
#===============================================================================================================================
#Condizioni

#if ed else
# age = int(input("Tua età: "))
# if age >=18:
#     print("Sei maggiorenne")
# else:
#     print("Sei minorenne")

#elif
# age = int(input("Tua età: "))
# if age >= 18:
#     patente = (input ("Hai la patente? si o no: "))
#     array = ["si", "SI", "sì", "Sì", "Si"]
#     if age >= 18 and patente in array:
#         print("Complimenti stronzo, puoi noleggiare una ferrari")
#     elif age >=18 and patente == "no":
#         print("Fatti la cazzo di patente, perdente")
# else:
#     print("Raggiungi la maggiore età e fatti la patente")

#===============================================================================================================================
#CICLI
#WHILE
# counter = 0
# while counter <=10:
#     print(counter)
#     counter+=1

# limite = int(input("Metti limite: "))
# counter = int(input ("Inserisci numero da cui partire: "))
# while (counter <= limite):
#     print(str(counter) + "/" + str(limite))
#     counter+=1

#Uso del break
# run = True
# stop = 1000
# counter = 0

# while (run == True):
#     print(counter)
#     counter += 1
#     if counter > stop:
#         print("Sto uscendo dal loop...")
#         break

#FOR

# for numero in range(11): #range(valore_inizio, valore_fine, valore_intervallo_incremento) è una funzione che permette di settare un intervallo
#     print(numero)

# for numero in range(20, 200):
#     print(numero)

#===============================================================================================================================
#LIBRERIE
#Modulo Random
#import random
# for numero in range(10):
#     val = random.randint(0,25)
#     print(val)

#Generare 10 numeri pari random da 0 a 10 --> random.randrange(0,10,2)
#Generare 10 numeri dispari random da 0 a 10 --> random.randrange(1,10,2)

# lista = ['Io', 'Ganimede', 'Callisto', 'Europa'] #array
# for numero in range(4):
#     #print(str(numero) +" " + random.choice(lista))
#     print(lista[numero])

#Modulo Math
# import math
# print("radice quadrata " + str(math.sqrt(49)))

# print("elevazione a potenza " + str(math.pow(3,4)))

#===============================================================================================================================
import math

while (True):
    print("1 - Somma")
    print("2 - Sottrazione")
    print("3 - Moltiplicazione")
    print("4 - Divisione")
    scelta = int(input())
    if (scelta == 1):
        print("SOMMA")
        num1 = int(input("Inserisci primo numero: "))
        num2 = int(input("Inserisci secondo numero: "))
        print("Risultato: " + str(num1 + num2))
    elif (scelta == 2):
        print("SOTTRAZIONE")
        num1 = int(input("Inserisci primo numero: "))
        num2 = int(input("Inserisci secondo numero: "))
        print("Risultato: " + str(num1 - num2))
    elif (scelta == 3):
        print("MOLTIPLICAZIONE")
        num1 = int(input("Inserisci primo numero: "))
        num2 = int(input("Inserisci secondo numero: "))
        print("Risultato: " + str(num1 * num2))
    elif (scelta == 4):
        print("DIVISIONE")
        num1 = int(input("Inserisci primo numero: "))
        num2 = int(input("Inserisci secondo numero: "))
        print("Risultato: " + str(num1 / num2))