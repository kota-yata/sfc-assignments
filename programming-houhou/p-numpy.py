import numpy as np
import time

N = 10000
A = np.ones((N, N), dtype=np.float32)
B = np.ones((N, N), dtype=np.float32) * 2

start = time.perf_counter()
C = A + B
end = time.perf_counter()
print(f"{end - start} seconds")

