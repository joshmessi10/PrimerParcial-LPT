#include <stdio.h>   
#include <stdlib.h>  
#include <string.h>  

#define MAX_LINE 1024  


int contar_coincidencias(FILE *archivo, const char *palabra) {
    char linea[MAX_LINE];  
    int count = 0;  
    size_t palabra_len = strlen(palabra);  
    while (fgets(linea, MAX_LINE, archivo) != NULL) {
        char *pos = linea;
        while ((pos = strstr(pos, palabra)) != NULL) {
            count++;  
            pos += palabra_len;
        }
    }
    return count;  
}

int main(int argc, char *argv[]) {

    if (argc != 3) {
        printf("Uso: %s archivo.txt key\n", argv[0]);
        return 1; 
    }
    FILE *archivo = fopen(argv[1], "r");
    if (!archivo) {
        perror("Error al abrir el archivo");  
        return 1;  
    }
    int rep = contar_coincidencias(archivo, argv[2]);
    fclose(archivo);
    printf("%s se repite %d veces en el texto.\n", argv[2], rep);
    return 0; 
}
