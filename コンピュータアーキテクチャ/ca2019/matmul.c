#define MAT_SIZE 4

int main() {
  int a[MAT_SIZE][MAT_SIZE] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12},
    {13, 14, 15, 16}
  };
  int b[MAT_SIZE][MAT_SIZE] = {
    {16, 15, 14, 13},
    {12, 11, 10, 9},
    {8, 7, 6, 5},
    {4, 3, 2, 1}
  };
  int c[MAT_SIZE][MAT_SIZE] = {0};

  for (int i = 0; i < MAT_SIZE; i++) {
    for (int j = 0; j < MAT_SIZE; j++) {
      for (int k = 0; k < MAT_SIZE; k++) {
        c[i][j] += a[i][k] * b[k][j];
      }
    }
  }

  return c[0][0];
}
