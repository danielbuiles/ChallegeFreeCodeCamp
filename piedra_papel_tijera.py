import random,time,os

def dormir(a):
    positions={1:'piedra', 2:'tijera', 3:'papel'}
    print("robot eligiendo.")
    time.sleep(1)
    print("robot eligiendo..")
    time.sleep(1)
    print("robot eligiendo...")
    time.sleep(1)
    print(f'el robot eligió {positions[a]}')
    time.sleep(2)
    
while True:
    time.sleep(3)
    os.system('cls')
    player=int(input("1:piedra, 2:tijera, 3:papel \n"))
    IA=random.randint(1,3)
    if player==1 or player==2 or player==3:
        dormir(IA)
        if player==1 and IA==1:
            print("empate")

        elif player==1 and IA==2:
            print("ganaste")

        elif player==1 and IA==3:
            print("perdiste")

        elif player==2 and IA==1:
            print("perdiste")

        elif player==2 and IA==2:
            print("empate")

        elif player==2 and IA==3:
            print("ganaste")

        elif player==3 and IA==1:
            print("ganaste")

        elif player==3 and IA==2:
            print("perdiste")

        elif player==3 and IA==3:
            print("empate")
            
        
    else:
        print("Error solo se aceptan los numeros de 1-3 \n")