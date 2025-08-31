#include <stdio.h>
#include <math.h>

#define MAIUSCULO 0

int main(void) {
    char cifra[2501];
    fgets(cifra, sizeof(cifra), stdin);

    char mensagem[313];
    char letra_atual = 0;
    int letras_decifradas = 0, bit_atual = 7;
    for (int char_atual = 0; cifra[char_atual] != '\0'; char_atual++) {
        if (bit_atual == -1) {
            if (letra_atual != 0) {
                mensagem[letras_decifradas] = letra_atual;
                letras_decifradas++;
            } 

            letra_atual = 0;
            bit_atual = 7; 
        }

        char char_cifra = cifra[char_atual];
        if (!('a' <= (char_cifra | 32) && (char_cifra | 32) <= 'z')) {
            continue;
        }

        char case_char_cifra = char_cifra & 32;
        letra_atual |= (char)(pow(2, bit_atual)) * (case_char_cifra == MAIUSCULO);
        bit_atual--;
    }

    mensagem[letras_decifradas] = '\0';
    printf("%s\n", mensagem);
    return 0;
}