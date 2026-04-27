#include <arm_neon.h>
#include <stdio.h>
#include <time.h>

#define N 10000
float A[N][N], B[N][N], C[N][N];

int main() {
  clock_t start, end;
  double seconds;

  start = clock();
  for (int j = 0; j < N; j++) {
    for (int i = 0; i < N; i+=4) {
      float32x4_t a = vld1q_f32(&A[i][j]);
      float32x4_t b = vld1q_f32(&B[i][j]);
      float32x4_t c = vaddq_f32(a, b);
      vst1q_f32(&C[i][j], c);
    }
  }
  end = clock();
  seconds = (double)(end - start) / CLOCKS_PER_SEC;
  printf("%f seconds\n", seconds);
  return 0;
}
