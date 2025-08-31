#include <stdio.h>

float melhor_divisao(int pedacos_restantes, float precos[]);

int main(void) {
    int total_pedacos;
    scanf("%d", &total_pedacos);

    float precos[total_pedacos];
    for (int i = 0; i < total_pedacos; i++) {
        scanf("%f", &precos[i]);
    }

    printf("%.2f\n", melhor_divisao(total_pedacos, precos));
    return 0;
}

float melhor_divisao(int pedacos_restantes, float precos[]) {
    if (pedacos_restantes == 1) {
        return precos[0];
    }

    int menor_preco = precos[pedacos_restantes - 1];
    for (int parcela = 1; parcela < pedacos_restantes; parcela++) {
        int divisao_possivel = precos[parcela - 1] + melhor_divisao(pedacos_restantes - parcela, precos);
        menor_preco = (divisao_possivel < menor_preco) ? divisao_possivel : menor_preco;
    }

    return menor_preco;
}