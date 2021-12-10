print("------------ingrese las palabras separadas por comas para verificar si son palindormos--------------")
print("no colocar ningun espacio o no funcionara!!")
print("ej:madam,malayan,geeks\n")
data=input("palabras: ").strip().split(',')

def palindromos(data:list):
    resultado=[]
    
    for i in data:
        word=[]
        for l in i:
            word.append(l)
        word.reverse()
        if ''.join(word) ==i:
            resultado.append({i:'es palindromo'})
        else:
            resultado.append({i:'no es palindromo'})
            
    return resultado

print(palindromos(data))