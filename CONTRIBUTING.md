# Guía de Contribución

Primero que nada, ¡muchas gracias por tu interés en colaborar con el repositorio de Share IT! Este archivo proporciona las instrucciones para que puedas hacer tus contribuciones de manera ordenada y eficiente.

## 1. Haz un Fork del repositorio

Para comenzar, haz un **fork** del repositorio a tu cuenta de GitHub. Esto creará una copia de este proyecto en tu propia cuenta, en la que podrás trabajar libremente sin afectar el repositorio original.

- Ve a la página principal de este repositorio.
- Haz clic en el botón **Fork** en la parte superior derecha.
- Esto creará una copia del repositorio en tu cuenta de GitHub.

## 2. Clona el repositorio en tu máquina local

Una vez que hayas hecho el fork, clona el repositorio a tu máquina local para poder trabajar en él.

```bash
git clone https://github.com/tu-usuario/mi-repositorio.git
```

## 3. Crea una nueva rama para tu contribución
Es recomendable que crees una nueva rama para trabajar en una característica o corrección específica. No trabajes directamente en la rama **main**.

```bash
git checkout -b nombre-de-tu-rama
```

## 4. Realiza tu contribución
Realiza tu contribución siguiendo la estructura propuesta en el README principal de este repositorio. Si por ejemplo quisieras añadir un libro de Python, deberías ir a la carpeta **lenguajes**, luego la subcarpeta **python** y finalmente la subcarpeta **libros**.

Los cambios serán revisados y fusionados con este repositorio *solo* si respetan la estructura de carpetas proporcionada.

## 5. Haz commit de tus cambios
Una vez que hayas terminado de hacer los cambios, haz commit de tus modificaciones con un mensaje claro y descriptivo.

```bash
git add .
git commit -m "Añadido libro de Python titulado 'Fluent Python'"
```

## 6. Haz un push de tus cambios al Fork
Después de hacer commit de tus cambios, "pushealos" al repositorio de tu fork en GitHub.
```bash
git push origin nombre-de-tu-rama
```

## 7. Abre un Pull Request (PR)
Ahora que tus cambios están en tu fork, puedes abrir un pull request (PR) para que los revisemos e integremos tus cambios en el repositorio principal.

- Ve a tu repositorio en GitHub y haz clic en **Compare & pull request**.
- Asegúrate de que estás enviando el pull request a la rama main del repositorio original.
- Agrega una descripción detallada de los cambios que has realizado.

## 8. Revisión de Pull Requests
Una vez que hayas enviado el pull request, nosotros lo revisaremos. Podremos hacer comentarios o sugerir cambios. Si es necesario, realiza los ajustes que se te pidan y haz un push de los cambios adicionales a tu rama.

## 9. Merge del Pull Request
Si todo está en orden y los cambios cumplen con las directrices del proyecto, procederemos a hacer un **merge** de tu pull request en la rama **main** del repositorio.

## 10. Mantén tu Fork sincronizado con este repositorio
Para asegurar que las contribuciones sean de alta calidad y consistentes con el proyecto, es importante que te asegures de que tu fork esté sincronizado con este repositorio. Mantener el fork sincronizado asegura que tengas la versión más actualizada de este repositorio, lo que ayuda a evitar conflictos cuando abras un pull request. Si no sincronizas tu fork, podría ser que tu PR no se pueda fusionar correctamente debido a conflictos con los archivos ya existentes.
```bash
  git remote add upstream https://github.com/eliasvelazquezdev/share-it-resources.git
  git fetch upstream
  git merge upstream/main
```

