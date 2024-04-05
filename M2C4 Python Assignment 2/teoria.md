# M2C4 Python Assignment 2 #

Las preguntas teóricas son:

- **¿Cuál es la diferencia entre una lista y una tupla en Python?**  
Son bastante parecidas, pero la diferencia más importante entre ellas es que la lista es mutable y la tupla inmutable. Esto quiere decir que a una lista le podemos añadir, quitar, ordenar los elementos, pero en las tuplas no, nos daría error. Por eso es importante pensar si vamos a querer que los elementos puedan cambiar o no.

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
Tal como suena, se trata de un diccionario, un sistema para almacenar datos, de cualquier tipo: cadenas, listas, funciones, lo que sea. Pero tiene la característica de que además hay que incluir una llave para acceder a los datos dentro del diccionario.

- **¿Cuál es la diferencia entre el método ordenado y la función de ordenación?**  
La diferencia radica en que con la función de ordenación podemos guardar la lista ordenada en otra variable y con el método ordenado no.

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
