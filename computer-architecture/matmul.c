#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 3000
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

void matmul_transposed(double **A, double **B_T, double **C, int n) {
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++) {
            double sum = 0;
            for(int k=0; k<n; k++)
                sum += A[i][k] * B_T[j][k];
            C[i][j] = sum;
        }
}

void transpose(double **src, double **dst, int n) {
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            dst[j][i] = src[i][j];
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
    double **B_T = alloc_matrix(N);
    double **C = alloc_matrix(N);

    randomize_matrix(A, N);
    randomize_matrix(B, N);
    transpose(B, B_T, N);

    double time_normal = 0;
    for(int t=0; t<TRIALS; t++) {
        double start = get_time_sec();
        matmul(A, B, C, N);
        double end = get_time_sec();
        time_normal += (end - start);
        printf("Trial %d (normal): %.3f sec\n", t+1, end - start);
    }
    printf("平均時間 (転置なし): %.3f sec\n", time_normal / TRIALS);

    // 転置した行列積の計測
    double time_transposed = 0;
    for(int t=0; t<TRIALS; t++) {
        double start = get_time_sec();
        matmul_transposed(A, B_T, C, N);
        double end = get_time_sec();
        time_transposed += (end - start);
        printf("Trial %d (transposed): %.3f sec\n", t+1, end - start);
    }
    printf("平均時間 (転置あり): %.3f sec\n", time_transposed / TRIALS);

    free_matrix(A);
    free_matrix(B);
    free_matrix(B_T);
    free_matrix(C);

    return 0;
}
