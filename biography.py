name=input('nombre: ')
birth=input('fecha de nacimiento: ')
adress=input('direccion: ')
goal=input('objetivo: ')

while True:
    if len(name)<=3 or len(name)>=10:
        name=input('nombre incorrecto ingrese nuevamente su nombre: ')
    elif len(birth)!=10 or birth.count('-') !=2:
        birth=input('fecha de nacimiento incorrecta ingrese nuevamente su fecha de nacimiento: ')
    elif len(adress)<10:
        adress=input('direccion incorrecta ingrese nuevamente su direccion: ')
    elif len(goal)<15:
        goal=input('objetivo incorrecto ingrese nuevamente su objetivo: ')
    else:
        print({'Nombre':name,
               'Fecha de nacimiento':birth,
               'Direccion':adress,
               'Objetivo':goal})
        break