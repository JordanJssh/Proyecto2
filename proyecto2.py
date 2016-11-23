print("ESCUELA POLITECNICA NACIONAL")
print("Integrantes: \nJorge Campoverde\nKatty Montoya\nJordan Sánchez")

def creatxt():
    archi=open('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('Jorge Campoverde\n')
    archi.write('Katty Montoya\n')
    archi.write('Jordan Sanchez\n')
    archi.close()
creatxt()
grabartxt()

def leertxt():
    archi=open('datos.txt','r')
    linea=archi.readline()
    while linea !="":
        print linea
        linea=archi.readline()
    archi.close()
