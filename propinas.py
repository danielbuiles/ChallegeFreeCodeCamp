import random
import os
def service():
    fac=float(input('¿Cuál es la factura total de hoy, por favor?\n'))
    pro=random.choice([18,20,25])
    por=round(fac*float(pro)/100,2)
    res=round(fac+por,2)
    print(f'La propina aplicando el {pro}% is ${por}, que contabiliza un total de ${res}\n')
    personas=int(input('cuantas personas lo acompañan?  '))
    print('\ncada persona en la mesa ha de pagar $',round(res/personas,2),' en total.')
    if input("otro usuario? s:si"):
        service()
    
service()