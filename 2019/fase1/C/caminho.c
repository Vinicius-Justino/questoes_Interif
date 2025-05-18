#include <stdio.h>

typedef struct vertice {
    char vizinhanca[99];
    char grau;
} cidade;

int SITIOLANDIA, BIRIGUI;
char existe_caminho = 0;
void caminha(cidade mapa[], char cidade_atual, char tamanho_passeio, char max_tamanho);

int main(void) {
    int cidades, pontes;
    scanf("%d %d", &cidades, &pontes);

    scanf("%d %d", &SITIOLANDIA, &BIRIGUI);
    SITIOLANDIA--;
    BIRIGUI--;

    cidade mapa[cidades];
    for (char cidade = 0; cidade < cidades; cidade++) {
        mapa[cidade].grau = 0;
    }

    for (char i = 0; i < pontes; i++) {
        int origem, destino;
        scanf("%d %d", &origem, &destino);
        origem--;
        destino--;

        mapa[origem].vizinhanca[mapa[origem].grau] = destino;
        mapa[origem].grau++;

        mapa[destino].vizinhanca[mapa[destino].grau] = origem;
        mapa[destino].grau++;
    }

    caminha(mapa, SITIOLANDIA, 0, cidades);
    if(existe_caminho) {
        printf("HA CAMINHO ATE BIRIGUI\n");
    } else {
        printf("NAO EXISTE CAMINHO\n");
    }
    return 0;
}

void caminha(cidade mapa[], char cidade_atual, char tamanho_passeio, char max_tamanho) {
    if (tamanho_passeio == max_tamanho) {
        return;
    } else if (cidade_atual == BIRIGUI) {
        existe_caminho = 1;
        return;
    }

    for (char vizinho = 0; vizinho < mapa[cidade_atual].grau; vizinho++) {
        caminha(mapa, mapa[cidade_atual].vizinhanca[vizinho], tamanho_passeio + 1, max_tamanho);
    }
}