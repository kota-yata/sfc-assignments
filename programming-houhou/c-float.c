#include <stdio.h>

int main(void) {
    double a = 0.11;
    double b = 0.81;
    double c = 0.92;

    double sum = a + b;

    printf("a + b = %.10f\n", sum);
    printf("c     = %.10f\n", c);

    if (sum == c)
        printf("Equal\n");
    else
        printf("Not equal\n");

    return 0;
}
