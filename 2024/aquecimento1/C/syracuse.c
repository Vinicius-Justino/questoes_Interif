#include <stdio.h>

int main(void) {
    int numero;

    while (scanf("%d", &numero) != -1) {
        int cont_passos = 0;

        for (; numero > 1; cont_passos++) {
            if (numero % 2 == 0) {
                numero /= 2;
            } else {
                numero *= 3;
                numero++;
            }
        }

        printf("%d\n", cont_passos);
    }

    return 0;
}