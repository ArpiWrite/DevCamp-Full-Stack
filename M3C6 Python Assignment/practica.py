#Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. 
#Crea un objeto usando la clase.

class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

usuarioUno = Usuario("Arosera", "myDevCode45*")
print(usuarioUno.nombre)
print(usuarioUno.contraseña)
