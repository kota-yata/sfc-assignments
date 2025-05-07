#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 10
#define TRIALS 5

double** alloc_matrix(int n) {
    double **m = malloc(n * sizeof(double*));
    m[0] = malloc(n * n * sizeof(double));
    for(int i = 1; i < n; i++)
        m[i] = m[0] + i * n;
    return m;
}

void free_matrix(double **m) {
    free(m[0]);
    free(m);
}

void randomize_matrix(double **m, int n) {
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            m[i][j] = (double)rand() / RAND_MAX;
}

void matmul(double **A, double **B, double **C, int n) {
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++) {
            double sum = 0;
            for(int k=0; k<n; k++)
                sum += A[i][k] * B[k][j];
            C[i][j] = sum;
        }
}

double get_time_sec() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec*1e-9;
}

int main() {
    srand(0);

    double **A = alloc_matrix(N);
    double **B = alloc_matrix(N);
    double **C = alloc_matrix(N);

    randomize_matrix(A, N);
    randomize_matrix(B, N);

    double time_normal = 0;
    for(int t=0; t<TRIALS; t++) {
        double start = get_time_sec();
        matmul(A, B, C, N);
        double end = get_time_sec();
        time_normal += (end - start);
        printf("Trial %d (normal): %.3f sec\n", t+1, end - start);
    }
    printf("avg time %.3f sec\n", time_normal / TRIALS);

    free_matrix(A);
    free_matrix(B);
    free_matrix(C);

    return 0;
}
