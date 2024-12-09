# Reto 2: 🖼️Enmarcando nombres

Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su taller 🖼️, pero el marco debe cumplir unas reglas específicas. Tu tarea es ayudar a los elfos a generar este marco mágico.

## Reglas:

- Dado un array de nombres, debes crear un marco rectangular que los contenga a todos.
- Cada nombre debe estar en una línea, alineado a la izquierda.
- El marco está construido con \* y tiene un borde de una línea de ancho.
- La anchura del marco se adapta automáticamente al nombre más largo más un margen de 1 espacio a cada lado.

## Ejemplo de funcionamiento:

```javascript

createFrame(['midu', 'madeval', 'educalvolpz'])

// Resultado esperado:
***************
* midu        *
* madeval     *
* educalvolpz *
***************

createFrame(['midu'])

// Resultado esperado:
********
* midu *
********

createFrame(['a', 'bb', 'ccc'])

// Resultado esperado:
*******
* a   *
* bb  *
* ccc *
*******

createFrame(['a', 'bb', 'ccc', 'dddd'])

```

## ¿Qué deberías hacer?🤔

1. Determinar la longitud del nombre más largo. Esto lo logramos recorriendo el array y determinando la longitud de los nombres por números de caracteres. Podemos usar Math.max().
2. Luego calculamos el ancho del marco, que sería la longitud del nombre más largo + 2 espacios y 2 asteriscos.
3. Contruimos las líneas del marco, la superior e inferior. Esto lo logramos con el método repeat(), primero seleccionando el carácter que se va a repetir, en este caso '\*', y luego el ancho que deberá tener el mismo, en este caso el frameWidth.
4. Construimos el marco que deberá tener el nombre. Utilizamos el método padEnd(), que se encarga de rellenar el final de una cadena con un cáracter específico hasta que alcance la longitud deseada.
5. Por último, combinamos las líneas (superior, intermedias, inferior). Usamos el método join() para poder añadir el salto de línea de cada elemento retornado.
