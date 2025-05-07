import random
import timeit

def matmul(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum_ = 0
            for k in range(n):
                sum_ += A[i][k] * B[k][j]
            C[i][j] = sum_
    return C

def matmul_transposed(A, B_T):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum_ = 0
            for k in range(n):
                sum_ += A[i][k] * B_T[j][k]  # 転置したBを行優先アクセス
            C[i][j] = sum_
    return C

# 行列サイズ (例えば 500x500)
n = 500

# ランダムな行列生成
A = [[random.uniform(-1, 1) for _ in range(n)] for _ in range(n)]
B = [[random.uniform(-1, 1) for _ in range(n)] for _ in range(n)]
B_T = [list(col) for col in zip(*B)]

# 測定（5回の繰り返しを3セット実施）
t_no_transpose = timeit.repeat("matmul(A,B)", 
                               setup="from __main__ import matmul, A, B",
                               repeat=3, number=5)

t_transpose = timeit.repeat("matmul_transposed(A,B_T)", 
                            setup="from __main__ import matmul_transposed, A, B_T",
                            repeat=3, number=5)

print("転置なし平均時間:", min(t_no_transpose)/5)
print("転置あり平均時間:", min(t_transpose)/5)
