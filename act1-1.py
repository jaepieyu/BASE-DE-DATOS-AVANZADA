from os import pread

#Leer tres numeros (a, b, c). Y ordenelo en forma descendente, es decir de mayor a menor. Favor controlar errores.

try:
    a = int(input("ingrese un valor para a: "))
    b = int(input("ingrese un valor para b: "))
    c = int(input("ingrese un valor para c: "))

    if c==b and a==b and a==c:
        print(a," = ",b," = ",c)
    elif a>=b and a>=c:
        if a==b: 
            print(a," = ",b," > ",c)
        elif a==c:
            print(a," = ",c," > ",b)
        elif b==c:
            print(a," > ",b," = ",c)
        elif b>c:
            print(a," > ",b," > ",c)  
        elif c>b:
            print(a," > ",c," > ",b)
    elif b>=a and b>=c:
        if b==a:
            print(b," = ",a," > ",c)
        elif b==c:
            print(b," = ",c," > ",a)
        elif a==c:
            print(b," > ",a," = ",c)
        elif a>c:
            print(b," > ",a," > ",c)
        elif c>a:
            print(b," > ",c," > ",a)
    elif c>=a and c>=b :
        if c==a:
            print(c," = ",a," > ",b)
        elif c==b:
            print(c," = ",b," > ",a)
        elif a==b:
            print(c," > ",a," = ",b)
        elif a>b:
            print(c," > ",a," > ",b)
        elif b>a:
           print (c," > ",b," > ",a)
except:
    print("Porfavor ingrese un numero")

