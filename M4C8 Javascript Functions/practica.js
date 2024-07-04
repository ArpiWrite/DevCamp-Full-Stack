/*
1. Cree un bucle for en JS que imprima cada nombre en esta lista. 
miLista = “velma”, “exploradora”, “jane”, “john”, “harry”
*/
let miLista = ["velma", "exploradora", "jane", "john", "harry"];

for (let nombre of miLista) {
    console.log(nombre)
};


/*
2. Cree un bucle while que recorra la misma lista y también imprima los nombres. Nota: Recuerda crear un contador para que el ciclo no sea infinito.
*/

let i= 0

while (i < 5) {
    console.log(miLista[i]);
    i++;
}


/*
3. Cree una función de flecha que devuelva "Hola mundo". 
*/

const saludo = () => "Hola mundo";
console.log(saludo());