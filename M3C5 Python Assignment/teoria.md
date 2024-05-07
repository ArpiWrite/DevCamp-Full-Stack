## PREGUNTA 1
**¿Qué es un condicional?**

Un condicional es una construcción, que tal como su nombre indica, establece condiciones para que se ejecuten nuestras órdenes o no. Por esto, deducimos que el condicional busca un valor True o False. 

Es importante recordar que para esta construcción es imprescindible conocer los ***operadores de condición***:

Funcionan tanto para cadenas como para números:

- == Igual que
- != Diferente que
- <> Diferente que (está en desuso, pero es útil reconocerlo)

Los siguientes solo funcionan con números:

- \> Mayor que
- \>= Mayor o igual que
- < Menor que
- <= Menor o igual que

La sintaxis comienza con la estructura if, seguida de la condición que queremos que evalúe el programa, sin olvidar terminar la línea con ***dos puntos (:)***. A continuación, sigue el bloque con las órdenes a ejecutar si la condición se cumple, que siempre deben ir con un sangrado para que el programa las reconozca como tal.

La sintaxis sería la siguiente:

    if condición:
        aquí las órdenes que se ejecutarán si la condición se cumple

Un ejemplo sencillo:

    edad = 18

    if edad >= 18:
        print("Eres mayor de edad")

En este caso, el programa reconoce que la condición se cumple y ejecuta la orden de imprimir.

En el ejemplo anterior, si no se cumpliera la condición, el programa no devolvería nada, pero tenemos la opción de indicarle una orden para cuando la condición no se cumple, con la estructura ***else***, que colocaríamos después de la condición y su bloque de órdenes.

Siguiendo con el ejemplo anterior, pero con un valor de edad diferente, se vería así:

    edad = 17

    if edad >= 18:
        print("Eres mayor de edad")

    else:
        print("No eres mayor de edad.")
        print("Recuerda que estás en la edad de aprender.")

En este caso, como no se cumple la condición, se ejecutarían las órdenes de **else**. 

Otros detalles a tener en cuenta:

- Un bloque de instrucciones puede contener varias órdenes y deben tener el mismo sangrado.
- Aunque Python permite que cada bloque tenga un número de espacios distinto en el sangrado, se aconseja utilizar siempre el mismo.

        if edad >= 18:
                print("Eres mayor de edad")
        else:
            print("No eres mayor de edad.")
            print("Recuerda que estás en la edad de aprender.")

- Cuidado, porque diferentes sangrados en un mismo bloque sí darían error.

        if edad >= 18:
            print("Eres mayor de edad")
        else:
                print("No eres mayor de edad.")
            print("Recuerda que estás en la edad de aprender.")

- Para "rellenar" un bloque de instrucciones que todavía no hemos escrito y poder ejecutar el programa, se utiliza la instrucción **pass**, ya que Python requiere que se escriba alguna instrucción en cualquier bloque.

        edad = int(input("¿Cuántos años tiene? "))
        
        if edad < 120:
            pass
        else:
            print("¡No me lo creo!")
            print(f"Usted dice que tiene {edad} años.")

Para terminar con los condicionales, falta mencionar que se pueden añadir más condiciones incluyendo la estructura ***elif*** (contracción de else if). Es importante el orden en el que se escriben las condiciones, porque en el momento que se cumpla una, el programa dejará de evaluar el resto.

Ejemplo:

    edad = int(input("¿Cuántos años tiene? ")) 

    if edad < 18:
        print("Es usted menor de edad.")

    elif edad < 0:
        print("No se puede tener una edad negativa")

    else:
        print("Es usted mayor de edad.")

En este caso, al escribir un valor negativo se mostraría el mensaje *"Es usted menor de edad."*, cuando la intención es que se muestre el mensaje *"No se puede tener una edad negativa"*.

El orden correcto sería el siguiente:

    edad = int(input("¿Cuántos años tiene? "))
    
    if edad < 0:
        print("No se puede tener una edad negativa")

    elif edad < 18:
        print("Es usted menor de edad.")

    else:
        print("Es usted mayor de edad.")


## INICIO PREGUNTA 2

**¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?**

Definamos de forma sencilla qué son los bucles: son una herramienta para alterar el flujo normal de un programa, más especificamente, nos permiten repetir una porción de código tantas veces como queramos.

Hay 2 tipos de bucles en Python: ***for*** y ***while***.

La principal diferencia entre estos bucles es, que mientras que **while** se puede ejecutar de manera infinita si no le decimos cuando parar (esto es cuando la condición que le damos resulte **falsa**), el bucle **for** solo se repetirá la cantidad posible de veces, que dependerá de la **cantidad de elementos** que haya.

Vamos con los ejemplos para ver la sintaxis y entender mejor cada uno.

Ejemplo de While:

    a = 1
    while a < 10:
        print("¡Hola, mundo!")

Como hemos comentado, en este ejemplo el código se ejecutaría de forma infinita, porque el valor de la variable **a** nunca cambia y la condición *a < 10 (1 < 10)* siempre es verdadera; recordemos que el bucle while solo parará cuando la condición resulte **falsa**. Esta situación puede romper nuestro programa, para que esto no pase, necesita que nosotros le demos un ***valor centinela***, lo que se traduciría como un valor limitante.

    a = 1
    while a < 10:
        print("¡Hola, mundo!")
        a += 1

Ahora, cada vez que el código se ejecute, el valor de la variable **a** se irá incrementando hasta que su valor sea 10. En ese momento, la condición *10 < 10* será **falsa** y el bucle dejará de ejecutarse.
Este bucle es útil para cuando no sabemos la cantidad de veces que se tendrá que ejecutar el código hasta llegar al valor centinela que lo finalice.

Ahora vayamos con el bucle **for**, que es más utilizado que el bucle while, precisamente porque en la mayoría de situaciones tendremos una cantidad concreta de elementos, y esta será la cantidad limitada de veces que podrá ejecutarse el código.

Ejemplo del bucle for:

    lenguajes = ["Python", "C", "C++", "Java"]

    for lenguaje in lenguajes:
        print(lenguaje)

En este caso lo que ha ocurrido es lo siguiente: el bucle **for** ejecuta el bloque de código indentado, *en este caso la llamada a print()* tantas veces como elementos haya en la colección indicada a la derecha del operador ***in***. Pero, cada vez que ese código es ejecutado, la variable lenguaje tendrá un valor diferente: en la primera ejecución será igual a "Python"; en la segunda, a "C"; y así hasta alcanzar el final de la lista.

Lo habitual es que si tienes una variable en plural, entonces la **variable de bloque** (la variable que corresponde a cada elemento y va después de **for**) será la misma en singular. Por eso en este caso, el nombre de la variable de la colección es *lenguajes* y la de bloque *lenguaje*.

El bucle for se puede utilizar para las ***colecciones*** (listas, tuplas y diccionarios) y las ***cadenas*** (entendidas como una colección de caracteres), es decir, cualquier **iterable**.

Es habitual encontrarse también el siguiente tipo de estructura donde **range()** genera una lista de números a iterar:

    for i in range(1, 11):
        print(i)


## INICIO PREGUNTA 3

**¿Qué es una lista por comprensión en Python?**

La comprensión de listas, del inglés *list comprehensions*, es una funcionalidad que nos permite crear listas avanzadas en una misma línea de código. Esto quiere decir que las listas que habitualmente creamos en varias líneas de código, podemos crearlas en una sola.

Ejemplo en el que queremos una lista con los elementos elevados al cubo.

Modo **tradicional**:

    num_list = range(1, 11)
    cubed_nums = []

    for num in num_list:
        cubed_nums.append(num**3)

    print(cubed_nums) => [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

Mismo ejemplo modo **lista por comprensión**:

    cubed_nums = [num ** 3 for num in num_list]

    print(cubed_nums) => [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

De forma más avanzada también se pueden incluir condicionales.

Ejemplo para obtener solo los números pares de un rango.

Modo **tradicional**:

    num_list = range(1, 11)
    even_nums = []

    for num in num_list:
        if num % 2 == 0:
            even_nums.append(num)

    print(even_nums) => [2, 4, 6, 8, 10]

Mismo ejemplo modo **lista por comprensión**:

    even_nums = [num for num in num_list if num % 2 == 0]

    print(even_nums) => [2, 4, 6, 8, 10]

Aunque pueda parecer muy útil utilizar las listas de comprensión, no debemos olvidar que es importante que nuestro código sea fácil de leer y entender por otros desarrolladores, y esta herramienta precisamente no lo hace muy legible. 

Podemos usarlas con moderación para listas sencillas y es bueno reconocerlas por si las encontramos en otros trabajos.


## INICIO PREGUNTA 4

**¿Qué es un argumento en Python?**

Un **argumento** es un valor que le damos a una función, pero para entender exactamente qué es, resulta necesario diferenciarlo de **parámetro**.

Pongamos un ejemplo para explicarlo.

    def resta(a, b):
        return a - b

    resta(30, 10)

En una función hay varias partes: la primera, en la que **definimos** la función con la palabra reservada ***def***, le damos un nombre y entre paréntesis le damos valores, que en este punto se denominan **parámetros** (en este ejemplo *(a, b)*). 

Después de crear la función e indicarle las instrucciones que queremos que siga, solo tenemos que llamar a la función usando el nombre que le hemos dado y entre paréntesis indicamos los valores que queremos que utilice para ejecutar la función, que en esta parte se denominan **argumentos** (en el ejemplo *(30, 10)*)

- Se pueden utilizar ***argumentos por posición***, como en este ejemplo, que en orden, 30 se posiciona como el parámetro *a* y 10 como el parámetro *b*.
- O también se podrían usar ***argumentos por nombre***, donde los argumentos son precedidos por un identificador, y se puede alterar su posición. Se vería así:

        def resta(a, b):
            return a - b

        resta(a=30, b=10)


## INICIO PREGUNTA 5

**¿Qué es una función Lambda en Python?**

Las funciones lambda en Python son una forma corta de declarar funciones pequeñas, se comportan como funciones normales declaradas con la palabra clave **def** y podemos empaquetarlas (como si las metiéramos en una variable) para introducirlas en otras funciones.

La sintaxis es:

    lambda argumentos: expresión

Vamos con un ejemplo sencillo en el que usamos la función lambda para obtener nombre y apellido, y luego la introducimos en una función de saludo.

Función **lambda**:

    nombre_completo = lambda nombre, apellido: f'{nombre} {apellido}'

    print(nombre_completo('Pepito', 'Grillo')) => Pepito Grillo

Función **saludo**:

    def saludo(usuario):
        print(f'¡Buenos días, {usuario}!')

    saludo(nombre_completo('Pepito', 'Grillo')) => ¡Buenos días, Pepito Grillo!

En este caso estamos usando la función **lambda** como argumento de la función **saludo**.


## INICIO PREGUNTA 6

**¿Qué es un paquete pip?**

**Pip** (*pip installs package*) es una herramienta para instalar y gestionar ***librerías externas*** en Python. **PyPI** (*Índice de paquetes de Python* o *Python Package Index*), conocido como **CheeseShop** es un repositorio donde encontrar e instalar programas desarrollados y compartidos por la comunidad de Python.

La ***sintaxis*** de Pip para instalar un paquete, por ejemplo **NumPy** (paquete que permite procesar de manera muy eficiente grander colecciones de datos de números, registros y objetos), es muy simple:

    pip install numpy

Pip también nos permite ***actualizar y administrar las versiones*** de los paquetes. Un problema que puede surgir de la actualización de las versiones, es que podríamos afectar a otros proyectos que necesitaban versiones anteriores para poder seguir ejecutándose. 

Por eso, una de las principales ventajas de trabajar con pip es que nos permite crear ***ambientes virtuales*** (*entornos de desarrollo independientes*) para cada proyecto, lo que se traduce en poder instalar las versiones que necesitamos sin afectar al resto de aplicaciones.
