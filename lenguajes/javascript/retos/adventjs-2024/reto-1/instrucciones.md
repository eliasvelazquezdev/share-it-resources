# Reto 1: 🎁¡Primer regalo repetido!

Santa Claus 🎅 ha recibido una lista de números mágicos que representan regalos 🎁, pero algunos de ellos están duplicados y deben ser eliminados para evitar confusiones. Además, los regalos deben ser ordenados en orden ascendente antes de entregárselos a los elfos.

## Reglas

Tu tarea es escribir una función que reciba una lista de números enteros (que pueden incluir duplicados) y devuelva una nueva lista sin duplicados, ordenada en orden ascendente.

## Ejemplo de funcionamiento:

```javascript
const gifts1 = [3, 1, 2, 3, 4, 2, 5]
const preparedGifts1 = prepareGifts(gifts1)
console.log(preparedGifts1) // [1, 2, 3, 4, 5]

const gifts2 = [6, 5, 5, 5, 5]
const preparedGifts2 = prepareGifts(gifts2)
console.log(preparedGifts2) // [5, 6]

const gifts3 = []
const preparedGifts3 = prepareGifts(gifts3)
console.log(preparedGifts3) // []
// No hay regalos, la lista queda vacía
```

## ¿Qué deberías hacer?🤔

1. Buscamos una forma de que no hayan valores repetidos. Esto lo logramos con el método set()
2. Retornamos el array uniqueGifts convertido de un Set a un array usando el operador de propagación. Luego, aplicamos el método sort con una función de comparación para ordenar los elementos en orden ascendente.

### Algunos Datos del método set()

- Valores Únicos: No puede contener valores duplicados.
- Orden de Inserción: Los elementos de un Set se almacenan en el orden en que fueron insertados.
- Operaciones Útiles: Tiene métodos y propiedades que permiten realizar operaciones como añadir, eliminar y buscar elementos.
