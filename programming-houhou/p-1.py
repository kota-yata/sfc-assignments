import time

N = 10000

A = [[1 for _ in range(N)] for _ in range(N)]
B = [[2 for _ in range(N)] for _ in range(N)]
C = [[0 for _ in range(N)] for _ in range(N)]

start = time.perf_counter()
for i in range(N):
    for j in range(N):
        C[i][j] = A[i][j] + B[i][j]
end = time.perf_counter()
print(f"{end - start} seconds")
