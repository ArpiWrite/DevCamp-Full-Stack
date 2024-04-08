# M2C4 Python Assignment 2 #

Las preguntas teóricas son:

- **¿Cuál es la diferencia entre una lista y una tupla en Python?**  
Son bastante parecidas, pero la diferencia más importante entre ellas es que la lista es mutable y la tupla inmutable. Esto quiere decir que a una lista le podemos añadir, quitar, ordenar los elementos, pero en las tuplas no. Por eso es importante pensar si vamos a querer que los elementos puedan cambiar o no.  
Una característica de las tuplas y las listas es que se pueden *desempaquetar*, pero es mejor hacerlo solo con las tuplas. Esto es porque al desempaquetar una tupla, si intentaramos usar el método de ordenación, nos saldría un error porque las tuplas son inmutables. Pero si se tratara de una lista, si se podría ordenar y cambiar toda la estructura de la lista.  
En el siguiente ejemplo, podemos observar que sin ordenarlas, la lista y la tupla darían el mismo resultado. No obstante, si aplicamos el método de ordenación comentado, en la tupla devolvería un error porque es inmutable, y en la lista sí se ordenaría, pero las variables creadas para desempacar no se corresponderían con lo que queríamos. En este caso, verbo_l tendría el valor **Yo**, sujeto_l el valor **Aroa** y predicado_l el valor **soy**.  
.  
frase_lista = ['Yo', 'soy', 'Aroa']  
.  
#frase_lista.sort()  
.  
sujeto_l, verbo_l, predicado_l = frase_lista  
print(sujeto_l)  
print(verbo_l)  
print(predicado_l)  
.  
print()  
.  
frase_tupla = ('Yo', 'soy', 'Aroa')  
.  
#frase_tupla.sort()  
.  
sujeto_t, verbo_t, predicado_t = frase_tupla  
print(sujeto_t)  
print(verbo_t)  
print(predicado_t)  

- **¿Cuál es el orden de las operaciones?**  
Cuando tenemos varios operadores diferentes, hay que realizarlos con cierto orden, para que el resultado sea el correcto. Hay una regla mnemotécnica que se puede usar para recordar mejor el orden: PEMDAS, en inglés.    
  * PARÉNTESIS
  * EXPONENCIAL
  * MULTIPLICACIÓN
  * DIVISIÓN
  * SUMA
  * RESTA
  
  Realmente, de estas operaciones, la multiplicación y división estarían al mismo nivel; lo mismo con la suma y resta. En estos casos, se suelen realizar las operaciones según las vayamos encontrando de izquierda a derecha.  
  *Ejemplo paso a paso:*  
  x = 5 + 4 * (6-3) / 2²  
  x = 5 + 4 * 3 / 2²  
  x = 5 + 4 * 3 / 4  
  x = 5 + 12 / 4  
  x = 5 + 3  
  x = 8



- **¿Qué es un diccionario Python?**  
Tal como suena, se trata de un diccionario, un sistema para almacenar datos, cuyo valor puedes ser de cualquier tipo: cadenas, listas, funciones, lo que sea. Pero tiene la característica de que además hay que incluir una llave, que será inmutable, para acceder a los datos dentro del diccionario.  
A cada llave le corresponde solo un valor y los elementos van separados por comas. Además, para seleccionar un elemento se utiliza de referencia la llave, no la posición como en otras estructuras. Si la llave que buscamos no se encuentra en el diccionario, aparecerá un error.

letras = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}

- **¿Cuál es la diferencia entre el método ordenado y la función de ordenación?**  
La diferencia radica en que con la función de ordenación podemos guardar la lista ordenada en otra variable y con el método ordenado no. Es decir, en el método ordenado pondríamos variable.sort() y cambiaríamos la estructura de la lista original y por ello python nos devolvería NONE al intentar almacenarla en otra variable, que no se puede. Usando la función sorted_list = sorted(variable) sí podemos crear otra variable para almacenar la nueva lista ordenada, sin modificar la original.
Otra diferencia es que el método ordenado es un método que solo aplica a listas, en cambio, la función sorted() se puede aplicar a cualquier iterable.

- **¿Qué es un operador de reasignación?**  
Un operador de reasignación es aquel que realiza la operación a una variable para cambiarle el valor a esa misma variable, se verá mejor con un ejemplo.  
.  
Si yo tengo 20 monedas y quiero añadir 20 más a la misma variable, se podría realizar la operación de la forma más básica:  
.  
monedas = 20  
monedas = monedas + 20  
.  
Con un operador de reasignación, en este caso para sumar, '+=', se podría acortar de esta manera y el valor de la variable monedas sería 40:  
monedas += 20


Esta es toda la asignación, ¡mucha suerte!

Con un operador de reasignación, en este caso para sumar, '+=', se podría acortar de esta manera y el valor de la variable monedas sería 40:  
monedas += 20


Esta es toda la asignación, ¡mucha suerte!
