#include <stdio.h>
#include <stdlib.h>

int initialized_global = 132;
int uninitalized_global;

int adder(int a, int b)
{
  return a+b;
}

int main(int argc, char *argv[]) {
	// HOMEWORK 1: print the location of main()
	printf("%p\n", (void *)main);
	// HOMEWORK 2: print the location of adder()
	printf("%p\n", (void *)adder);
	// HOMEWORK 3: use malloc() and print the result to find the heap
	printf("location of heap : %p\n", (void *)malloc(sizeof(int)));
	int x = 3;
	printf("location of stack: %p\n", &x);
	printf("initialized_global address: %p\n",&initialized_global);
	printf("uninitalized_global address: %p\n",&uninitalized_global);
	int y = adder(3,4);
	// HOMEWORK 4: add some code here to print local variable addresses and
	// assess whether the stack grows up or down
	int a = 5;
	int b = 6;
	int c = 7;
	printf("local variable a address: %p\n", (void *)&a);
	printf("local variable b address: %p\n", (void *)&b);
	printf("local variable c address: %p\n", (void *)&c);
	return 0;
}
