.data // data section (defining space for variables)
.align 3
// A*B=C
// .word is 32bit int
A: .word 1, 2, 3, 4, 5, 6, 7, 8, 9
B: .word 9, 8, 7, 6, 5, 4, 3, 2, 1
C: .zero 36

.text
.global _start // specifies the entry point

_start:
  // at this point A, B and C are in memory and have their addresses
  // loading those addresses into registers for later use
  ldr x0, =A
  ldr x1, =B
  ldr x2, =C
  mov x3, #3 // N = 3
  // initialize the loop counters
  mov x4, #0 // i = 0

i_loop:
  mov x5, #0 // j = 0

j_loop:
  mov x6, #0 // k = 0
  mov w7, #0 // clear accumulator

k_loop:
  // loading A[i][k]
  mul x8, x4, x3 // i * N (specifying the row)
  add x8, x8, x6 // i * N + k (specifying the column)
  lsl x8, x8, #2 // multiply by 4 (size of int)
  ldr w9, [x0, x8] // load A[i][k] into w9
  // loading B[k][j]
  mul x8, x6, x3
  add x8, x8, x5
  lsl x8, x8, #2
  ldr w10, [x1, x8]
  // multiply
  madd w7, w9, w10, w7
  // k++
  add x6, x6, #1
  // loop if k < N else end the k loop
  cmp x6, x3
  b.lt k_loop

k_loop_end:
  // calculating C[i][j]
  mul x8, x4, x3
  add x8, x8, x5
  lsl x8, x8, #2
  str w7, [x2, x8]
  // j++
  add x5, x5, #1
  // loop if j < N else end the j loop
  cmp x5, x3
  b.lt j_loop

j_loop_end:
  add x4, x4, #1
  cmp x4, x3
  b.lt i_loop
  // exit
  mov x8, #93
  mov x0, #0
  svc #0
