	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 14, 0	sdk_version 14, 0
	.globl	_alloc_matrix                   ; -- Begin function alloc_matrix
	.p2align	2
_alloc_matrix:                          ; @alloc_matrix
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	.cfi_def_cfa_offset 48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	w0, [x29, #-4]
	ldursw	x8, [x29, #-4]
	lsl	x0, x8, #3
	bl	_malloc
	str	x0, [sp, #16]
	ldur	w8, [x29, #-4]
	ldur	w9, [x29, #-4]
	mul	w9, w8, w9
                                        ; implicit-def: $x8
	mov	x8, x9
	sxtw	x8, w8
	lsl	x0, x8, #3
	bl	_malloc
	ldr	x8, [sp, #16]
	str	x0, [x8]
	mov	w8, #1
	str	w8, [sp, #12]
	b	LBB0_1
LBB0_1:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [sp, #12]
	ldur	w9, [x29, #-4]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB0_4
	b	LBB0_2
LBB0_2:                                 ;   in Loop: Header=BB0_1 Depth=1
	ldr	x8, [sp, #16]
	ldr	x8, [x8]
	ldr	w9, [sp, #12]
	ldur	w10, [x29, #-4]
	mul	w9, w9, w10
	add	x8, x8, w9, sxtw #3
	ldr	x9, [sp, #16]
	ldrsw	x10, [sp, #12]
	str	x8, [x9, x10, lsl  #3]
	b	LBB0_3
LBB0_3:                                 ;   in Loop: Header=BB0_1 Depth=1
	ldr	w8, [sp, #12]
	add	w8, w8, #1
	str	w8, [sp, #12]
	b	LBB0_1
LBB0_4:
	ldr	x0, [sp, #16]
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_free_matrix                    ; -- Begin function free_matrix
	.p2align	2
_free_matrix:                           ; @free_matrix
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	.cfi_def_cfa_offset 32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	str	x0, [sp, #8]
	ldr	x8, [sp, #8]
	ldr	x0, [x8]
	bl	_free
	ldr	x0, [sp, #8]
	bl	_free
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3, 0x0                          ; -- Begin function randomize_matrix
lCPI2_0:
	.quad	0x41dfffffffc00000              ; double 2147483647
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_randomize_matrix
	.p2align	2
_randomize_matrix:                      ; @randomize_matrix
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	.cfi_def_cfa_offset 48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	x0, [x29, #-8]
	stur	w1, [x29, #-12]
	str	wzr, [sp, #16]
	b	LBB2_1
LBB2_1:                                 ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB2_3 Depth 2
	ldr	w8, [sp, #16]
	ldur	w9, [x29, #-12]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB2_8
	b	LBB2_2
LBB2_2:                                 ;   in Loop: Header=BB2_1 Depth=1
	str	wzr, [sp, #12]
	b	LBB2_3
LBB2_3:                                 ;   Parent Loop BB2_1 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [sp, #12]
	ldur	w9, [x29, #-12]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB2_6
	b	LBB2_4
LBB2_4:                                 ;   in Loop: Header=BB2_3 Depth=2
	bl	_rand
	scvtf	d0, w0
	adrp	x8, lCPI2_0@PAGE
	ldr	d1, [x8, lCPI2_0@PAGEOFF]
	fdiv	d0, d0, d1
	ldur	x8, [x29, #-8]
	ldrsw	x9, [sp, #16]
	ldr	x8, [x8, x9, lsl  #3]
	ldrsw	x9, [sp, #12]
	str	d0, [x8, x9, lsl  #3]
	b	LBB2_5
LBB2_5:                                 ;   in Loop: Header=BB2_3 Depth=2
	ldr	w8, [sp, #12]
	add	w8, w8, #1
	str	w8, [sp, #12]
	b	LBB2_3
LBB2_6:                                 ;   in Loop: Header=BB2_1 Depth=1
	b	LBB2_7
LBB2_7:                                 ;   in Loop: Header=BB2_1 Depth=1
	ldr	w8, [sp, #16]
	add	w8, w8, #1
	str	w8, [sp, #16]
	b	LBB2_1
LBB2_8:
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_matmul                         ; -- Begin function matmul
	.p2align	2
_matmul:                                ; @matmul
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #64
	.cfi_def_cfa_offset 64
	str	x0, [sp, #56]
	str	x1, [sp, #48]
	str	x2, [sp, #40]
	str	w3, [sp, #36]
	str	wzr, [sp, #32]
	b	LBB3_1
LBB3_1:                                 ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB3_3 Depth 2
                                        ;       Child Loop BB3_5 Depth 3
	ldr	w8, [sp, #32]
	ldr	w9, [sp, #36]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB3_12
	b	LBB3_2
LBB3_2:                                 ;   in Loop: Header=BB3_1 Depth=1
	str	wzr, [sp, #28]
	b	LBB3_3
LBB3_3:                                 ;   Parent Loop BB3_1 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB3_5 Depth 3
	ldr	w8, [sp, #28]
	ldr	w9, [sp, #36]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB3_10
	b	LBB3_4
LBB3_4:                                 ;   in Loop: Header=BB3_3 Depth=2
	movi	d0, #0000000000000000
	str	d0, [sp, #16]
	str	wzr, [sp, #12]
	b	LBB3_5
LBB3_5:                                 ;   Parent Loop BB3_1 Depth=1
                                        ;     Parent Loop BB3_3 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldr	w8, [sp, #12]
	ldr	w9, [sp, #36]
	subs	w8, w8, w9
	cset	w8, ge
	tbnz	w8, #0, LBB3_8
	b	LBB3_6
LBB3_6:                                 ;   in Loop: Header=BB3_5 Depth=3
	; load A[i][k]
	ldr	x8, [sp, #56] ; sp + 56 holds pointer to A
	ldrsw	x9, [sp, #32] ; sp + 32 holds i. ldrsw casts it to int64_t and stores it in x9
	ldr	x8, [x8, x9, lsl  #3] ; x8 + x9 * 8 computes the address of A[i]
	ldrsw	x9, [sp, #12] ; sp + 12 holds k.
	ldr	d0, [x8, x9, lsl  #3]; load A[i][k]
	; load B[k][j]
	ldr	x8, [sp, #48]
	ldrsw	x9, [sp, #12]
	ldr	x8, [x8, x9, lsl  #3]
	ldrsw	x9, [sp, #28]
	ldr	d1, [x8, x9, lsl  #3]
	; sum += A[i][k] * B[k][j]
	ldr	d2, [sp, #16]
	fmadd	d0, d0, d1, d2
	str	d0, [sp, #16]
	b	LBB3_7
LBB3_7:                                 ;   in Loop: Header=BB3_5 Depth=3
	ldr	w8, [sp, #12]
	add	w8, w8, #1
	str	w8, [sp, #12]
	b	LBB3_5
LBB3_8:                                 ;   in Loop: Header=BB3_3 Depth=2
	ldr	d0, [sp, #16]
	; calculate C[i][j]
	ldr	x8, [sp, #40]
	ldrsw	x9, [sp, #32]
	ldr	x8, [x8, x9, lsl  #3]
	ldrsw	x9, [sp, #28]
	str	d0, [x8, x9, lsl  #3]
	b	LBB3_9
LBB3_9:                                 ;   in Loop: Header=BB3_3 Depth=2
	ldr	w8, [sp, #28]
	add	w8, w8, #1
	str	w8, [sp, #28]
	b	LBB3_3
LBB3_10:                                ;   in Loop: Header=BB3_1 Depth=1
	b	LBB3_11
LBB3_11:                                ;   in Loop: Header=BB3_1 Depth=1
	ldr	w8, [sp, #32]
	add	w8, w8, #1
	str	w8, [sp, #32]
	b	LBB3_1
LBB3_12:
	add	sp, sp, #64
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3, 0x0                          ; -- Begin function get_time_sec
lCPI4_0:
	.quad	0x3e112e0be826d695              ; double 1.0000000000000001E-9
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_get_time_sec
	.p2align	2
_get_time_sec:                          ; @get_time_sec
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	.cfi_def_cfa_offset 32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	mov	w0, #6
	mov	x1, sp
	bl	_clock_gettime
	ldr	d0, [sp]
	scvtf	d2, d0
	ldr	d0, [sp, #8]
	scvtf	d0, d0
	adrp	x8, lCPI4_0@PAGE
	ldr	d1, [x8, lCPI4_0@PAGEOFF]
	fmadd	d0, d0, d1, d2
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #112
	.cfi_def_cfa_offset 112
	stp	x29, x30, [sp, #96]             ; 16-byte Folded Spill
	add	x29, sp, #96
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	mov	w0, #0
	stur	wzr, [x29, #-4]
	bl	_srand
	mov	w0, #10
	str	w0, [sp, #28]                   ; 4-byte Folded Spill
	bl	_alloc_matrix
	mov	x8, x0
	ldr	w0, [sp, #28]                   ; 4-byte Folded Reload
	stur	x8, [x29, #-16]
	bl	_alloc_matrix
	mov	x8, x0
	ldr	w0, [sp, #28]                   ; 4-byte Folded Reload
	stur	x8, [x29, #-24]
	bl	_alloc_matrix
	ldr	w1, [sp, #28]                   ; 4-byte Folded Reload
	stur	x0, [x29, #-32]
	ldur	x0, [x29, #-16]
	bl	_randomize_matrix
	ldr	w1, [sp, #28]                   ; 4-byte Folded Reload
	ldur	x0, [x29, #-24]
	bl	_randomize_matrix
	movi	d0, #0000000000000000
	stur	d0, [x29, #-40]
	stur	wzr, [x29, #-44]
	b	LBB5_1
LBB5_1:                                 ; =>This Inner Loop Header: Depth=1
	ldur	w8, [x29, #-44]
	subs	w8, w8, #5
	cset	w8, ge
	tbnz	w8, #0, LBB5_4
	b	LBB5_2
LBB5_2:                                 ;   in Loop: Header=BB5_1 Depth=1
	bl	_get_time_sec
	str	d0, [sp, #40]
	ldur	x0, [x29, #-16]
	ldur	x1, [x29, #-24]
	ldur	x2, [x29, #-32]
	mov	w3, #10
	bl	_matmul
	bl	_get_time_sec
	str	d0, [sp, #32]
	ldr	d0, [sp, #32]
	ldr	d1, [sp, #40]
	fsub	d1, d0, d1
	ldur	d0, [x29, #-40]
	fadd	d0, d0, d1
	stur	d0, [x29, #-40]
	ldur	w8, [x29, #-44]
	add	w10, w8, #1
	ldr	d0, [sp, #32]
	ldr	d1, [sp, #40]
	fsub	d0, d0, d1
	mov	x8, sp
                                        ; implicit-def: $x9
	mov	x9, x10
	str	x9, [x8]
	str	d0, [x8, #8]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	bl	_printf
	b	LBB5_3
LBB5_3:                                 ;   in Loop: Header=BB5_1 Depth=1
	ldur	w8, [x29, #-44]
	add	w8, w8, #1
	stur	w8, [x29, #-44]
	b	LBB5_1
LBB5_4:
	ldur	d0, [x29, #-40]
	fmov	d1, #5.00000000
	fdiv	d0, d0, d1
	mov	x8, sp
	str	d0, [x8]
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	bl	_printf
	ldur	x0, [x29, #-16]
	bl	_free_matrix
	ldur	x0, [x29, #-24]
	bl	_free_matrix
	ldur	x0, [x29, #-32]
	bl	_free_matrix
	mov	w0, #0
	ldp	x29, x30, [sp, #96]             ; 16-byte Folded Reload
	add	sp, sp, #112
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"Trial %d (normal): %.3f sec\n"

l_.str.1:                               ; @.str.1
	.asciz	"avg time %.3f sec\n"

.subsections_via_symbols
