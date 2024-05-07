#Cree un bucle For de Python.

pets = ['Kira', 'Nika', 'Lola', 'Panda', 'Max']

for pet in pets:
    print(pet)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(a, b, c):
    resultado = a + b + c
    return resultado

print(suma(1,2,3))

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

resultado = lambda a, b, c: a + b + c

print(resultado(1,2,3))

#Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
#nombre = 'Enrique'
#lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

def coincide(dato, lista):
    if dato in lista:
        print(f'¡He encontrado a {nombre} en tu lista!')
    else:
        print(f'Aquí no hay nada parecido a {nombre} en tu lista...')

nombre = 'Enrique'

lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

coincide(nombre, lista_nombre)
