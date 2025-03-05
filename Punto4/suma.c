#include <stdio.h>
#include <time.h>

int main() {
    clock_t start1, end1, start2, end2, start3, end3;
    double time1, time2, time3;
    
    start1 = clock();
    
    long long sum1 = 0;
    for (int i = 1; i <= 99999; i++) {
        sum1 += i;
    }
    
    end1 = clock();
    time1 = ((double) (end1 - start1)) / CLOCKS_PER_SEC;
    
    printf("Tiempo de ejecución en C de la suma de 1 a 99999: %f segundos\n", time1);

    start2 = clock();
    
    long long sum2 = 0;
    for (int i = 1; i <= 999999; i++) {
        sum2 += i;
    }
    
    end2 = clock();
    time2 = ((double) (end2 - start2)) / CLOCKS_PER_SEC;
    
    printf("Tiempo de ejecución en C de la suma de 1 a 999999: %f segundos\n", time2);

    start3 = clock();
    
    long long sum3 = 0;
    for (int i = 1; i <= 9999999; i++) {
        sum3 += i;
    }
    
    end3 = clock();
    time3 = ((double) (end3 - start3)) / CLOCKS_PER_SEC;
    
    printf("Tiempo de ejecución en C de la suma de 1 a 9999999: %f segundos\n", time3);


    return 0;
}
