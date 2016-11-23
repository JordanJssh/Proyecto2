import math 

print("ESCUELA POLITECNICA NACIONAL")
print("Integrantes: ")
print("Jorge Campoverde\nKatty Montoya\nJordan Sanchez")

print("Calculo de las raices de la funcion cuadratica")
a=0
b=0
c=0
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))

dis=0
dis=math.sqrt(math.pow(b,2)-(4*a*c))

if dis>0:
    ##poner codigo aqui...
    print(dis)
else:
    print("ERROR..!! DISCRIMINANTE NEGATIVO")

