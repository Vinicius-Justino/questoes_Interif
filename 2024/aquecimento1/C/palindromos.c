#include <stdio.h>

int main(void) {
    char palavra[51];
    scanf("%s", palavra);

    int contador_letras[26];
    for (int i = 0; i < 26; i++) {
        contador_letras[i] = 0;
    }

    for (int i = 0; palavra[i] != '\0'; i++) {
        int letra = palavra[i] | 32;

        contador_letras[letra - 'a']++;
    }

    int cont_impares = 0;
    for (int i = 0; i < 26; i ++) {
        cont_impares += contador_letras[i] % 2;
    }

    if (cont_impares <= 1) {
        printf("1\n");
    } else {
        printf("0\n");
    }

    return 0;
}

/*
'A' = 65 = 01000001
'a' = 97 = 01100001
           00100000 = 32

or bitwise:
01100001 = 97
00100000 = 32
*/

