# C vs. Python
## Lenguajes Compilados
Un lenguaje compilado convierte el código fuente en código máquina antes de ejecutarse. Ejemplos:

C, C++, Rust, Go
Ventajas
✅ Mayor velocidad de ejecución: El código ya está traducido a instrucciones de bajo nivel optimizadas.
✅ Menos consumo de recursos: No requiere un intérprete en tiempo de ejecución.
✅ Mayor optimización: Los compiladores aplican técnicas de optimización para mejorar el rendimiento.

Desventajas
❌ Menos flexibilidad: Cualquier cambio en el código requiere recompilación.
❌ Mayor tiempo de desarrollo: Compilar y depurar puede ser más complejo.

## Lenguajes Interpretados
Un lenguaje interpretado ejecuta el código línea por línea sin necesidad de compilación previa. Ejemplos:

Python, JavaScript, Ruby, PHP
Ventajas
✅ Más flexibilidad: Permite cambios rápidos en el código sin recompilar.
✅ Fácil de depurar: La ejecución línea por línea facilita la detección de errores.
✅ Portabilidad: Se puede ejecutar en múltiples plataformas sin recompilar.

Desventajas
❌ Menor rendimiento: La interpretación en tiempo real hace que la ejecución sea más lenta.
❌ Mayor consumo de recursos: El intérprete agrega una capa extra de procesamiento.

## Comparación de Rendimiento
Para comparar el rendimiento, podemos evaluar tiempos de ejecución con un mismo algoritmo en dos lenguajes:

```
gcc suma.c -o suma
./suma
```
Tiempo de ejecución en C: 0.003162 segundos

```
python3 suma.py
```
Tiempo de ejecución en Python: 0.099191 segundos
