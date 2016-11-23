## EPN-ESFOT-ASI PROGRAMACIÓN AVANZADA 2016-B

## Autores: Campoverde Jorge - Montoya Katherine - Sanchez Jordan
## Fecha: 23-Nov-2016

import os

def menu ():
    print("\t\t\t**CALCULO DE PERIMETROS Y AREAS**")
    print("\n-OPCIONES:")
    print("1.- Circulo")
    print("2.- Triangulo")
    print("3.- Cuadrado")
    print("4.- Poligonos Regulares de 5 a 10 lados")
    

def circulo():
    pi=3.1415
    radio=float(input("\nINGRESE EL VALOR DEL RADIO: "))
    a= 2*pi*radio
    p= pi*radio**2
    print ("\nEl valor del perimetro es: ",p)
    print ("El valor del area es: ",a)
    archi=open('ResultadoCirculo.txt','a')
    archi.write('')
    archi.write('Resultado\n')
    archi.write(str(a))
    archi.write('\n')
    archi.write(str(p))
    archi.close()
    

def triangulo():
    x=float (input("\nIngrese el valor de los lados: "))
    h=float (input("Ingrese el valor de la altura: "))
    a=(x*h)/2
    p=x+x+x
    print ("\nEl valor del perimetro es: ",p)
    print ("El valor del area es: ",a)
    archi=open('ResultadoTriangulo.txt','a')
    archi.write('Resultado\n')
    archi.write(str(a))
    archi.write('\n')
    archi.write(str(p))
    archi.close()

def cuadrado():
    l=float(input("\nIgrese el valor del lado: "))
    a=l*l 
    p=l+l+l+l
    print ("\nEl valor del perimetro es: ",p)
    print ("El valor del area es: ",a)
    
def poligonos_r():
    n=float(input("Ingrese el numerode lados: "))
    l=float(input("Ingrese la medida de uno de los lados: "))
    a=float(input("Ingrese la medida del apotema: "))
    
    if n>=5 or n<=10:
        a=(n*l*a)/2
        p=n*l
    else:
        print("Ingrese un numero valido")

    print ("\nEl valor del perimetro es: ",p)
    print ("El valor del area es: ",a)

def crartxt():
    archi=open('ResultadoCirculo.txt','w')
    archi.close()
    archi=open('ResultadoTriangulo.txt','w')
    archi.close()
    archi=open('ResultadoCuadrado.txt','w')
    archi.close()
    archi=open('ResultadoPoligonosRegulares','w')
    archi.close()
    
    
    
def main():
    menu()
    a='a'
    opc=int(input("\nESCOJA UNA OPCION(PARA TERMINAR EL ""\n""PROGRAMA NO DIJITE NADA Y PRESIONE ENTER): "))
    while opc !="":
        if opc==1:
            circulo()
        if opc==2:
            triangulo()
        if opc==3:
            cuadrado()
        if opc==4:
            poligonos_r()
        if opc>4:
            print("\nOPCION INCORRECTA... INTENTE DE NUEVO")
        a=input("\nPRESIONE ENTER PARA CONTINUAR...")
        if a=="":
            os.system("cls")
        menu()
        opc=int(input("\nESCOJA UNA OPCION(PARA TERMINAR EL ""\n""PROGRAMA NO DIJITE NADA Y PRESIONE ENTER): "))
    print("\nFIN DEL PROGRAMA..!!")   
main()
