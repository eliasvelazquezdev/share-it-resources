
## Data Structure & Classes Challenge

Nivel de dificultad: Mid Level 

## Descripción

El siguiente challenge fue parte de una live-coding interview para la posición de Intern Python Backend Developer en una empresa fintech de Berlin.


## Actividad

Para este live-coding challenge se debía desarrollar un script de Python e ir comentando cada implementación o decisión tomada a los developers encargados de tomar la prueba (eran 2).


#### Start
Please implement the word index for the given book.
Write the code that takes a text and returns a dictionary where the keys are the first letter of each word, and the values are the tuples of words starting with that letter and their first occurrence in the text, sorted in alphabetical order. Indexing is starting from 1.

```
# Example

# Input from the file:
raw_input = "Hello, this is my text"
# idx =      1      8    13 16 19

# Expected output

{
  "h": [("Hello", 1)], 
  "i": [("is", 13)], 
  "m": [("my", 16)], 
  "t": [("text", 19), ("this", 8)],
}
```