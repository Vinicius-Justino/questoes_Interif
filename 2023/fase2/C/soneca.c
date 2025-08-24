#include <stdio.h>

int main(void) {
    int quantidade_guerreiros, duracao_turno;
    scanf("%d %d", &quantidade_guerreiros, &duracao_turno);

    int furtividade_monstro, atraso_ataque;
    scanf("%d %d", &furtividade_monstro, &atraso_ataque);

    int audicoes[quantidade_guerreiros];
    for (int i = 0; i < quantidade_guerreiros; i++) {
        scanf("%d", &audicoes[i]);
    }

    int duracao_ciclo = duracao_turno * quantidade_guerreiros;
    int sentinela = (atraso_ataque % duracao_ciclo) / duracao_turno;

    if (furtividade_monstro > audicoes[sentinela]) {
        printf("O vilarejo do Faz-de-contIF foi devorado\n");
    } else {
        printf("O vilarejo do Faz-de-contIF foi alertado\n");
    }

    return 0;
}