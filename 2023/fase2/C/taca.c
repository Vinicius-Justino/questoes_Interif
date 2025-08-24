#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n1, n2, n;
    scanf("%d %d", &n1, &n2);

    char buffer[6];
    for (scanf("%s", &buffer); buffer[0] != 'X'; scanf("%s", &buffer)) {
        n = atoi(buffer);
    }

    printf("%d\n", n * (n2 / n1));
    return 0;
}