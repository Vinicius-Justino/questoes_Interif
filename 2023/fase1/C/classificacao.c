#include <stdio.h>

#define VOLTA_INVALIDA 700000

int main(void) {
    int quantidade_pilotos, total_voltas, voltas_invalidas;
    scanf("%d %d %d", &quantidade_pilotos, &total_voltas, &voltas_invalidas);

    int voltas_por_piloto = total_voltas / quantidade_pilotos;

    typedef struct t {
        char nome[100];
        int tempos[voltas_por_piloto];
        int voltas_registradas;
    } entrada;

    entrada placar[quantidade_pilotos];
    for (char piloto = 0; piloto < quantidade_pilotos; piloto++) {
        scanf("%s", &placar[piloto].nome);
        placar[piloto].voltas_registradas = 0;
    }

    for (int volta = 0; volta < total_voltas; volta++) {
        char sigla[4];
        int minutos, segundos, milissegundos;
        scanf("%s %d:%d.%d", &sigla, &minutos, &segundos, &milissegundos);

        sigla[1] |= 32;
        sigla[2] |= 32;
        int tempo = (minutos * 60 + segundos) * 1000 + milissegundos;

        for (char piloto = 0; piloto < quantidade_pilotos; piloto++) {
            char piloto_errado = 0;
            for (char letra = 0; letra < 3; letra++) {
                piloto_errado += placar[piloto].nome[letra] - sigla[letra];
            }

            if (piloto_errado == 0) {
                placar[piloto].tempos[placar[piloto].voltas_registradas] = tempo;
                placar[piloto].voltas_registradas++;
                break;
            }
        }
    }

    for (int volta = 0; volta < voltas_invalidas; volta++) {
        char sigla[4];
        int minutos, segundos, milissegundos;
        scanf("%s %d:%d.%d", &sigla, &minutos, &segundos, &milissegundos);

        sigla[1] |= 32;
        sigla[2] |= 32;
        int tempo = (minutos * 60 + segundos) * 1000 + milissegundos;

        for (char piloto = 0; piloto < quantidade_pilotos; piloto++) {
            char piloto_errado = 0;
            for (char letra = 0; letra < 3; letra++) {
                piloto_errado += placar[piloto].nome[letra] - sigla[letra];
            }

            if (piloto_errado == 0) {
                for (int i = 0; i < voltas_por_piloto; i++) {
                    if (placar[piloto].tempos[i] == tempo) {
                        placar[piloto].tempos[i] = VOLTA_INVALIDA;
                        break;
                    }
                }
            }
        }
    }

    char colocados[quantidade_pilotos];
    for (char piloto = 0; piloto < quantidade_pilotos; piloto++) {
        colocados[piloto] = 0;
    }

    for (char colocacao = 0; colocacao < quantidade_pilotos; colocacao++) {
        int indice_vencedor, volta_menor_tempo = voltas_por_piloto + 1, menor_tempo = VOLTA_INVALIDA;

        for (char piloto = 0; piloto < quantidade_pilotos; piloto++) {
            if (colocados[piloto]) {
                continue;
            }

            for (int volta = 0; volta < voltas_por_piloto; volta++) {
                if (placar[piloto].tempos[volta] < menor_tempo) {
                    menor_tempo = placar[piloto].tempos[volta];
                    volta_menor_tempo = volta;
                    indice_vencedor = piloto;
                } else if (placar[piloto].tempos[volta] == menor_tempo && volta < volta_menor_tempo) {
                    menor_tempo = placar[piloto].tempos[volta];
                    volta_menor_tempo = volta;
                    indice_vencedor = piloto;
                }
            }
        }

        int milissegundos = menor_tempo % 1000;
        menor_tempo /= 1000;
        int minutos = menor_tempo / 60, segundos = menor_tempo % 60;
        printf("%d %s %d:%d.%d\n", colocacao + 1, placar[indice_vencedor].nome, minutos, segundos, milissegundos);

        colocados[indice_vencedor] = 1;
    }
    return 0;
}