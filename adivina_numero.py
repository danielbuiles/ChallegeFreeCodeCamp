import random
import os

def eleccion(req):
    if  req.lower() == 'p':
        print("Gracias por jugar! puede correr de nuevo este programa cuando quiera")
        os._exit(0)
    else:
        return int(req)
        
print("-------------Adivina el numero--------------")
num=int(input("ingrese el un numero del 1-50: "))
intentos=0
numRandom = random.randint(1,50)
while num!=numRandom:
    if num<1 or num>50:
        print("recuerde que el numero debe de estar entre 1 y 50\n")
        eleccion('p')
    elif num<numRandom:
        num=eleccion(input("el numero buscado es mayor! P:parar de jugar \n"))
        intentos+=1
    else:
        num=eleccion(input("el numero buscado es menor! P:parar de jugar \n"))
        intentos+=1
        
print(f"felicidades has encontrado el numero {numRandom} en {intentos} Intentos")