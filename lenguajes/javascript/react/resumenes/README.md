## Conceptos Clave de React y TypeScript

### 1. Reactividad en React

- React es una biblioteca reactiva que actualiza la UI automáticamente cuando cambian el estado o las props.

### 2. Estados en React

- El `useState` gestiona datos dinámicos y controla el ciclo de vida del componente.
- Cuando cambia el estado, React vuelve a renderizar automáticamente el componente.

### 3. Props

- Las `props` permiten pasar datos desde un componente padre a un hijo.
- Son inmutables y se usan para personalizar componentes.

### 4. Ciclo de vida con `useEffect`

- Se usa para manejar efectos secundarios como llamadas a APIs o suscripciones.
- Su arreglo de dependencias define cuándo se ejecuta:
  - **Vacío:** Solo al montar el componente.
  - **Con dependencias:** Cada vez que cambian esas dependencias.

### 5. Gestores de paquetes

- Herramientas como NPM, Yarn y Bun que permiten gestionar las dependencias y bibliotecas necesarias para un proyecto.
- Similares a Maven en Java, ayudan a instalar, actualizar y eliminar librerías.

---

## Hooks y React Moderno

### 6. Hooks básicos

- `useState`: Maneja el estado local de un componente.
- `useEffect`: Maneja efectos secundarios y el ciclo de vida.
- `useCallback`: Memoriza funciones para evitar recrearlas en cada renderizado.
- `useMemo`: Memoriza cálculos complejos para evitar recalcularlos innecesariamente.
- `useRef`: Referencia elementos del DOM o valores persistentes sin desencadenar renderizados.

### 7. Hooks personalizados

- Encapsulan lógica reutilizable usando hooks estándar.
- Ejemplo: Un hook para manejar solicitudes HTTP (`useFetch`).

### 8. Diferencia entre hooks personalizados y estándar

- Los hooks estándar (como `useState` y `useEffect`) son provistos por React y cubren casos comunes.
- Los hooks personalizados encapsulan lógica específica reutilizable combinando hooks estándar.

### 9. Reglas de los hooks

- Solo pueden usarse en el nivel más alto de un componente o hook personalizado.
- Siempre deben empezar con `use`.

---

## TypeScript en React

### 10. TypeScript y JSX (`tsx`)

- Los archivos `.tsx` combinan TypeScript y JSX.
- Permiten definir tipos para `props`, estado y eventos.

### 11. Interfaces para `props`

```tsx
interface Props {
  titulo: string;
  numero: number;
}
```

### 12. Tipado en hooks

```tsx
const [contador, setContador] = useState<number>(0);
```

---

## Manejo del Estado Global

### 13. Context API y herramientas avanzadas

- Usa Context API para estados simples (como tema o autenticación).
- Para aplicaciones más complejas, utiliza Redux, Zustand o Jotai.

---

## Optimización y Rendimiento

### 14. Árbol de reconciliación

- React compara el Virtual DOM actual con el nuevo para aplicar cambios mínimos al DOM real.
- Esto mejora el rendimiento al evitar actualizaciones innecesarias.

### 15. Evitar renders innecesarios

- Usa `React.memo` para componentes funcionales que no cambian frecuentemente.
- Usa `useCallback` para memorizar funciones.
- Usa `useMemo` para memorizar cálculos costosos.

### 16. Debouncing y Throttling

- **Debouncing:** Retrasa la ejecución de una función hasta que el evento deje de ocurrir.
- **Throttling:** Asegura que una función se ejecute solo una vez en un intervalo de tiempo.

### 17. Manejo de la carga de imágenes y recursos

- Usa técnicas como lazy loading o code splitting para cargar recursos solo cuando sean necesarios.
- Herramientas como `React.lazy` o librerías como `react-loadable` son útiles.

---

## Manejo de APIs REST

### 18. Consumo de APIs con fetch

```javascript
const fetchData = async () => {
  try {
    const response = await fetch("https://api.example.com");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
};
```

### 19. Axios y configuración global

```javascript
import axios from "axios";

const api = axios.create({
  baseURL: "https://api.example.com",
  headers: { Authorization: "Bearer token" },
});

api.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error)
);
```

### 20. Tipos para datos de API

```tsx
interface Producto {
  id: number;
  nombre: string;
}
```

---

## Técnicas Avanzadas

### 21. Closures en JavaScript

```javascript
function contador() {
  let count = 0;
  return () => ++count;
}

const incrementar = contador();
console.log(incrementar()); // 1
console.log(incrementar()); // 2
```

### 22. WebSockets

```javascript
const socket = new WebSocket("ws://example.com/socket");

socket.onopen = () => console.log("Conexión abierta");
socket.onmessage = (event) => console.log(event.data);
```

### 23. Seguridad en aplicaciones frontend

- **Validación de entrada:** Sanitiza datos antes de procesarlos.
- **Protección contra XSS:** Escapa datos dinámicos en la UI.
- **Uso de HTTPS:** Cifra conexiones cliente-servidor.
- **Autenticación segura:** Usa tokens como JWT.

---

## Bundlers y Transpiladores

### 24. Bundlers

- Herramientas como Webpack o Vite combinan y optimizan archivos JavaScript, CSS, imágenes, etc.
- Generan archivos listos para producción, minimizados y optimizados.

### 25. Transpiladores

- Babel transpila código moderno (TypeScript, JSX) a versiones compatibles con navegadores más antiguos.
