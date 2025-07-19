#include <stdio.h>
#include <math.h>
#include <float.h>

int main() {
    float max_f = 1.0f;
    while (!isinf(max_f * 2.0f)) {
        max_f *= 2.0f;
    }
    printf("Approx max float: %e\n", max_f);

    double max_d = 1.0;
    while (!isinf(max_d * 2.0)) {
        max_d *= 2.0;
    }
    printf("Approx max double: %e\n", max_d);

    float min_f = 1.0f;
    while (min_f / 2.0f > 0.0f) {
        min_f /= 2.0f;
    }
    printf("Approx min float: %e\n", min_f);
    
    double min_d = 1.0;
    while (min_d / 2.0 > 0.0) {
        min_d /= 2.0;
    }
    printf("Approx min double: %e\n", min_d);

    return 0;
}
