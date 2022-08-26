#edad = 0
#while edad < 18:
#   edad = edad + 1
#   print (f"Felicidades, tienes  {edad} años")
#
# En el ejemplo anteror, notese que cuando la variable edad tiene el valor de uno (1); 
# en el mensaje aparecerá 1 años en plural, lo cual no es valido porque debería ser en singular, 
# es decir 1 año.
# Implemente este caso para que aprezca en forma correcta.


edad = 0
while edad < 18:
    edad = edad+1
    if edad==1: 
        print(f"Felicidades, tienes  {edad} año")
    else:  
        print(f"Felicidades, tienes  {edad} años")
    