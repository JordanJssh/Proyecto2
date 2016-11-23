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

dis=math.pow(b,2)-(4*a*c)

if dis>0:
    discrim=math.sqrt(dis)
    x1=0.0
    x1=(-b+discrim)/2*a
    x2=0.0
    x2=(-b-discrim)/2*a
    
    print("El valor de X1 es: ",x1,"El valor de X2 es: ",x2)
else:
    print("ERROR..!! DISCRIMINANTE NEGATIVO")

