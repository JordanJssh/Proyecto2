
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
    palabra='Harry'
    archi=open ('harry.txt','r')
    linea=archi.readline()
    for line in lineas:
        palabras=line.split(' ')
        for p in palabra:
            if p ==palabra:
                repetidas +=1

    print("Las palabra Harry se repite:",repetidas)


leertxt()

