#!/usr/bin/awk -f

BEGIN {
    suma = "SUMA";
    incr = "INCR";
    entero = "ENTERO";
    real = "REAL";
}

{
    for (i = 1; i <= NF; i++) {
        if ($i ~ /^\+$/) {
            print suma;
        } else if ($i ~ /^\+\+$/) {
            print incr;
        } else if ($i ~ /^[0-9]+$/) {
            print entero;
        } else if ($i ~ /^[0-9]+\.[0-9]+$/) {
            print real;
        }
    }
}

