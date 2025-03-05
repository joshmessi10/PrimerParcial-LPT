%{
#include <stdio.h>
%}

lambda [a-zA-Z_][a-zA-Z0-9_]*[ \t]*=[ \t]*lambda[ \t]*[a-zA-Z_][a-zA-Z0-9_]*([ \t]*,[ \t]*[a-zA-Z_][a-zA-Z0-9_]*)*[ \t]*:[ \t]*.+

%%

^{lambda}$ { printf("ACEPTA");}

^.*$ { printf("NO ACEPTA"); }

%%

int main(int argc, char *argv[]) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            printf("Error al abrir el archivo %s\n", argv[1]);
            return 1;
        }
    }

    yylex();  // Ejecutar el análisis léxico

    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1;
}

