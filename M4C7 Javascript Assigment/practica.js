/*
Cree una función JS que acepte 4 argumentos. 
Suma los dos primeros argumentos, luego los dos segundos y multiplícalos. 
Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". 
Si es más pequeño, la consola registra "¡El número es menor que 50!" 
*/

function multiSuma(num1, num2, num3, num4) {
  
    const resultado = (num1 + num2) * (num3 + num4);
     
      if (resultado > 50) {
        console.log("¡El número es mayor que 50!")
      } else if (resultado < 50) {
        console.log("¡El número es menor que 50!")
      } else if (resultado === 50) {
        console.log("¡El número es exactamente 50!")
      } else {
        console.log("No sé que esperas que haga con esto, la verdad... Solo admito números...")
      }
    return resultado
  }
  
  valor1 = multiSuma(2,2,3,3);
  valor2 = multiSuma(2,7,3,3);
  valor3 = multiSuma(2,0,12,13);
  valor4 = multiSuma(2,2,"tres",3);