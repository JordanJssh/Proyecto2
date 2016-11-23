#### Lectura de Archivo txt


def creartxt():
    archi=open('Lectura.txt','w')
    archi.close
def grabartxt():
    archi=open('Lectura.txt','a')
    archi.write('Jorge')
    archi.close()

#creartxt()
#grabartxt()

def leertxt():
    caracteres=0
    archi=open ('Lectura.txt','r')
    linea=archi.readline()
    caracteres=caracteres+len(linea)
    while linea !="":
        #print (linea)
        linea=archi.readline()
        caracteres=caracteres+len(linea)
        #print(caracteres)
        #print(len(linea))
    archi.close()
    print(caracteres)

leertxt()
