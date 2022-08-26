def accion1():
    Ds1={
        'Nombre Función':('accion1'),
        'descripción': ('Suma A y B,','A+B',' muestra el resultado C'),
    }
    print(Ds1)
    while True:
        try:
            A=int(input("Ingrese el valor de A: "))
            B=int(input("Ingrese el valor de B: "))
            break
        except:
            print("ingrese un valor entero")
    C=A+B
    print(C)

def accion2():
    Ds2={
        'Nombre Función':('accion2'),
        'descripción': ('Resta A y B','A-B', 'muestra el resultado '),
    }
    print(Ds2)
    while True:
        try:
            A=int(input("Ingrese el valor de A: "))
            B=int(input("Ingrese el valor de B: "))
            break
        except:
            print("ingrese un valor entero")
    C=A-B
    print(C)

def accion3():
    Ds3={
        'Nombre Función':('accion3'),
        'descripción': ('Multiplica A y B','A*B', 'muestra el resultado '),
    }
    print(Ds3)
    while True:
        try:
            A=int(input("Ingrese el valor de A: "))
            B=int(input("Ingrese el valor de B: "))
            break
        except:
            print("ingrese un valor entero")
    C=A*B
    print(C)

def accion4():
    Ds4={
        'Nombre Función':('accion4'),
        'descripción': ('Divide A y B', 'A/B','muestra el resultado '),
    }
    print(Ds4)
    while True:
        try:
            A=int(input("Ingrese el valor de A: "))
            B=int(input("Ingrese el valor de B: "))
            break
        except:
            print("ingrese un valor entero")
    C=A/B
    print(C)

def accion5():
    Ds5={
        'Nombre Función':('accion5'),
        'descripción': ('Cierra el programa'),
    }
    print(Ds5)

def menu_principal(): 
    opciones = {
        '1 ': ('Opción 1'),
        '2 ': ('Opción 2'),
        '3 ': ('Opción 3'),
        '4 ': ('Opción 4'),
        '5 ': ('Opción 5'),
    }
    print(opciones)
  

if __name__ == '__main__':

    while (True):
        try:
            menu_principal()
            a = int(input("ingrese un opción valida : "))
            if a == 1:
                accion1()
            elif a==2:
                accion2()
            elif a==3:
                accion3()
            elif a==4:
                accion4()
            elif a==5:
                accion5()
                break
        except:
            print("ingrese un valor valido")






