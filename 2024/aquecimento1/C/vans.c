#include <stdio.h>

int main(void) {
    int tamanho_percurso, velocidade_van, duracao_corrida;
    scanf("%d %d %d", &tamanho_percurso, &velocidade_van, &duracao_corrida);

    float tamanho_percurso_km = tamanho_percurso / 1000.0f;

    int percursos_completos = (int)(duracao_corrida * velocidade_van / tamanho_percurso_km);
    printf("%d", percursos_completos); 

    return 0;
}