
#### Busqueda palabra harry


def creartxt():
    archi=open('Lectura.txt','w')
    archi=open('Conteo.txt','w')
    archi.close
def grabartxt():
    archi=open('Lectura.txt','a')
    archi.write('Jorge')
    archi.close()

#creartxt()
#grabartxt()

def leertxt():
    repetidas=0
    clave='Harry'
    archi=open ('harry.txt','r') #Abre el archivo harry
    linea=archi.readline() # lee la linea del archivo
    palabras=linea.split(' ')# separa la linea leida quitando los espacios
    cadena=len(palabras) #cadena es igualada al numero de palabras que fueron separadas en el comando anterior
    for i in range(cadena-1): # i en el rango de la cadena
        if palabras[i]==clave: # evalua si la posicion de i de palabras es igual a la clave que es Harry
            repetidas=repetidas+1 #si encuentra la coinsidencia repetidas aumenta
    while linea != "": #repite todo lo mencionado antes hasta que no haya lineas
        linea=archi.readline()
        palabras=linea.split(' ')
        cadena=len(palabras)
        for i in range(cadena):
            if palabras[i]==clave:
                repetidas=repetidas+1
    archi.close()
    #for line in lineas:
     #   palabras=line.split(' ')
      #  for p in clave:
       #     if p ==clave:
        #        repetidas +=1

    print("Las palabra Harry se repite: ",repetidas)


leertxt()

