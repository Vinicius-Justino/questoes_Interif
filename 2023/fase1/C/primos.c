#include <stdio.h>

int main(void) {
    int teto;
    scanf("%d", &teto);
    
    if (teto == 1) {
        putchar('\n');
        return 0;
    }

    int primos[teto], primos_encontrados = 1;
    primos[0] = 2;

    putchar('2');
    for (int numero = 3; numero <= teto; numero++) {
        char eh_primo = 1;
        for (int i = 0; eh_primo && i < primos_encontrados; i++) {
            eh_primo = (numero % primos[i] != 0);
        }

        if (eh_primo) {
            printf(" %d", numero);
            primos[primos_encontrados] = numero;
            primos_encontrados++;
        }
    }
    
    putchar('\n');
    return 0;
}