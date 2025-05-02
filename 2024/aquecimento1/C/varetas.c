#include <stdio.h>

#define true 1
const int VALORES_VARETAS[5] = {5, 10, 15, 20, 50};

int main(void) {
    int cont_rodadas = 1;

    while (true) {
        int jogador_atual;
        scanf("%d", &jogador_atual);
        if (jogador_atual == -1) {
            break;
        }

        jogador_atual--;
        int pontuacoes[3] = {0, 0, 0};
        while (true) {
            int vareta_retirada;
            scanf("%d", &vareta_retirada);
            if (vareta_retirada == -1) {
                break;
            }

            if (vareta_retirada == 0) {
                jogador_atual = (jogador_atual + 1) % 3;
                continue;
            }

            pontuacoes[jogador_atual] += VALORES_VARETAS[vareta_retirada - 1];
        }

        int maior_pontuacao = pontuacoes[0];
        for (int jogador = 0; jogador < 3; jogador++) {
            maior_pontuacao = (pontuacoes[jogador] > maior_pontuacao) ? pontuacoes[jogador] : maior_pontuacao;
        }
        
        int vencedores[3] = {0, 0, 0};
        int cont_vencedores = 0;
        for (int jogador = 0; jogador < 3; jogador++) {
            if (pontuacoes[jogador] == maior_pontuacao) {
                vencedores[cont_vencedores] = jogador + 1;
                cont_vencedores++;
            }
        }
        
        if (cont_rodadas > 1) {
            printf("\n");
        }
        printf("RODADA %d\n", cont_rodadas);
        printf("%s com %d pontos\n", ((vencedores[1] == 0) ? "Ganhador" : "Empate"), maior_pontuacao);
        printf("Jogador %d", vencedores[0]);
        for (int jogador = 1; vencedores[jogador] != 0; jogador++) {
            printf(", Jogador %d", vencedores[jogador]);
        }
        printf("\n");

        cont_rodadas++;
    }

    return 0;
}