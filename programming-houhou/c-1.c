#include <stdio.h>
#include <time.h>

#define N 10000
int A[N][N], B[N][N], C[N][N];

int main() {
  clock_t start, end;
  double seconds;

  start = clock();
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      C[i][j] = A[i][j] + B[i][j];
    }
  }
  end = clock();
  seconds = (double)(end - start) / CLOCKS_PER_SEC;
  printf("%f seconds\n", seconds);
  return 0;
}
