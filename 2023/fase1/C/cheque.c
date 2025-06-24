#include <stdio.h>

typedef unsigned long int dinheiro;

int main(void) {
    int tipos_cedulas;
    scanf("%d", &tipos_cedulas);

    int valores_cedulas[tipos_cedulas];
    for (char i = 0; i < tipos_cedulas; i++) {
        scanf("%d", &valores_cedulas[i]);
    }

    dinheiro valor_sacado;
    scanf("%lu", &valor_sacado);

    dinheiro cedulas_sacadas = 0;
    while (valor_sacado > 0) {
        char indice_maior = 0;
        for (char i = 1; i < tipos_cedulas; i++) {
            if (valores_cedulas[i] > valores_cedulas[indice_maior]) {
                indice_maior = i;
            }
        }

        int maior_valor = valores_cedulas[indice_maior];
        cedulas_sacadas += valor_sacado / maior_valor;
        valor_sacado -= (valor_sacado / maior_valor) * maior_valor;

        valores_cedulas[indice_maior] = 0;
    }

    printf("%lu\n", cedulas_sacadas);
    return 0;
}
