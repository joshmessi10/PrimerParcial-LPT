# Programa en Lex
Para la función Lamda de Python, escriba un gramática
regular para que comprenda el funcionamiento de la
misma.

Implemente esta gramática regular en LEX. El programa debe
recibir un archivo de texto como parámetro de entrada y debe
devolver (imprimir) si se acepta o no la expresión.

# Modo de uso:
```
lex lambda.l
gcc lex.yy.c -ll
./a.out archivo.txt
```
