# C vs. Python
## Lenguajes Compilados
Un lenguaje compilado convierte el código fuente en código máquina antes de ejecutarse, es decir, realiza la compilación de todo el código.

## Lenguajes Interpretados

## Lenguajes Interpretados
Un lenguaje interpretado ejecuta el código línea por línea sin necesidad de compilación previa.

# Comparacion

La ejecucion de los programas en un lenguaje compilado tiende a ser mas rapida que en un lenguaje interpretado.

# Ejemplo: Suma de numeros

# Ejecucion en Python
```
python3 suma.py
```
Tiempo de ejecución en Python de la suma de 1 a 99999: 0.010621 segundos
Tiempo de ejecución en Python de la suma de 1 a 999999: 0.084057 segundos
Tiempo de ejecución en Python de la suma de 1 a 9999999: 0.786043 segundos

#Ejecucion en C
```
gcc suma.c -o suma
./suma
```

Tiempo de ejecución en C de la suma de 1 a 99999: 0.000203 segundos
Tiempo de ejecución en C de la suma de 1 a 999999: 0.006102 segundos
Tiempo de ejecución en C de la suma de 1 a 9999999: 0.022541 segundos
