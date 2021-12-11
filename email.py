staf={'gmail':'google','outlook':'Microsoft','hotmail':'Microsoft','yahoo':'Yahoo'}

correo=input('correo: ')
i=correo.split('@')[1].index('.')
name=correo.split('@')[0]
mail=correo.split('@')[1][:i].lower()

if (mail in staf):
    print(f'Hola {name}, estoy viendo que tu email está registrado con {staf[mail]}. ¡Eso es genial!')
else:
    print(f'Hola {name}, estoy observando que estás utilizando un dominio personalizado de {mail}. ¡Impresionante!')