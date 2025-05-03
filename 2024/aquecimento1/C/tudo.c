#include <stdio.h>

int main(void) {
    int quantidade_canais, tamanho_slot, bytes_por_canal;
    scanf("%d %d\n%d", &quantidade_canais, &tamanho_slot, &bytes_por_canal);

    int quadros[quantidade_canais][bytes_por_canal];
    int canal_atual = quantidade_canais - 1;
    for (int indice_byte_atual = 0, slots_enviados = 0; indice_byte_atual < (bytes_por_canal * quantidade_canais); slots_enviados = (++indice_byte_atual) / bytes_por_canal) {
        if (indice_byte_atual % tamanho_slot == 0) {
            canal_atual = (canal_atual + 1) % quantidade_canais;
        }

        scanf("%d", &quadros[canal_atual][(tamanho_slot * slots_enviados) + (indice_byte_atual % tamanho_slot)]);
    }

    for (int canal = 0; canal < quantidade_canais; canal++) {
        int codigo_erro = 0;
        for (int i = 0; i < bytes_por_canal; i++) {
            int byte = quadros[canal][i];
            codigo_erro += byte;
            printf("%d\n", byte);
        }

        printf("%d\n", (codigo_erro % 256));
    }
}