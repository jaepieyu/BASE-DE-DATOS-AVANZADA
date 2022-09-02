
def menu():
    Menulista={
        '1' : ('Añadir Persona a la lista',añadir_Persona),
        '2' : ('Borrar Persona de la lista',borrar_Persona),
        '3' : ('Mostar lista',mostar_Lista),
        '4' : ('Salir',salir)
    }
    selecion_Menu(Menulista, '4' )

def selecion_Menu(Menulista,opcion_salida):
    aux = None
    while aux != opcion_salida:
        desplegar_Menu(Menulista)
        aux = caturar_Variable(Menulista)
        ejecutar_Accion(Menulista,aux)

def desplegar_Menu(Menulista):
    for clave in sorted(Menulista):
        print(f' {clave}) {Menulista[clave][0]}')

def caturar_Variable(Menulista):
    while (a := input('Opción: ')) not in Menulista:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_Accion(Menulista,aux):
    Menulista[aux][1]()

class Persona ():
    nombre = ""
    apellido=""
    edad=""
    direccion = ""
    telefono = ""
    listaPersona = []

    def añadir(self):
        self.nombre=input(f"añade un nombre: ")
        self.apellido=input(f"añade un apellido: ")
        self.edad=input(f"añade la edad: ")
        self.telefono=input(f"añade la edad: ")
        self.direccion =input(f"añade la direccion: ")
      
        self.LP={
            "Nombre ":self.nombre,
            "Apellido ":self.apellido,
            "Edad ":self.edad,
            "Telefono ": self.telefono,
            "Direccion":self.direccion,
        }
        self.listaPersona.append(self.LP)
        
    def borrar(self):
        del self.listaPersona[-1]
    
    def mostar (self):
        for x in self.listaPersona:
            print (x)

px=Persona()

def añadir_Persona ():
    px.añadir()  

def borrar_Persona ():
    px.borrar()

def mostar_Lista ():
    px.mostar()

def salir():
    print('Finalizando Programa')

if __name__ == '__main__':
    menu()

