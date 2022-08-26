#Realice los siguientes programas:
#Leer un numero entero positivo y calcular su Factorial.


from re import X


while 1:
    print("selecione un Ejercio")
    print("1#Leer un numero entero positivo y calcular su Factorial.")
    print("2#Calcular la serie de Taylor")
    print("3#Calcular las siguientes series: Sen X y Cos X ")
    print("4#Salir")
    p=int(input())
    if p==4:
        break
    elif p==1:
        while 1:
            try:
                print
                a=int(input("ingrese un valor entero y mayor a 0: "))
                if a>0 :
                    break
            except:
                print("Escriba un numero entero")
        aux=a
        sumatoria=1
        while aux>0:
            sumatoria=sumatoria*aux          
            aux=aux-1
        print(f"{a}! = {sumatoria}")
    elif p==2:
        print ("calcular la serie de Taylor")

        x=int(input("ingrese X "))
        n=int(input("ingrese N "))
        aux1=n
        sum1=1
        sum2=0
        while n > 0:
            while aux1>0:
                sum1=sum1*aux1
                aux1=aux1-1
            sum2=sum2+((x**n)/sum1)
            n=n-1
        print(sum2)
    elif p==3:
        
        
        print("calcular Sen X")

        x1=int(input("ingrese X: "))
        n1=int(input("ingrese N: "))
        aux2=n1
        aux3=n1
        sum3=1      
        sum4=0
        while aux2>0:
            while aux3 > 0:
                sumaux=(2*aux3+1)
                sum3=sum3*sumaux
                aux3=aux3-1
            y1=2*n1+1
            sum4=sum4+(((-1)**n1)*(x1**y1)/sum3)
            aux2=aux2-1
        print(f"Sen X= {sum4}")

        print("calcular Cos X")
        aux4=n1
        aux5=n1
        sum5=1
        sum6=0
        while aux4>0:
            while aux5>0:
                sumaux2=(2*n1)
                sum5=sum5*sumaux2
                aux5=aux5-1
            y2=2*n1
            sum6=sum6+(((-1)**n1)*(x1**y2)/sum5)
            aux4=aux4-1
        print(f"Cos X= {sum6}")

        


