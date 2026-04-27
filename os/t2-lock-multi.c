/* Threads with enough work to hopefully have something interesting happen. */

#include <stdio.h>
#include <assert.h>
#include <pthread.h>
#include <stdlib.h>

#define NUM_THREADS 10
#define NUM_GLOBAL 100000000

int gcounter = NUM_GLOBAL;

typedef struct {
    char thread_id;
    int lcounter;
} thread_data_t;

pthread_mutex_t master_lock = PTHREAD_MUTEX_INITIALIZER;

void *mythread(void *arg) {
    thread_data_t *data = (thread_data_t *)arg;
    printf("%c: start\n", data->thread_id);
    printf("%c: lcounter: %d\n", data->thread_id, data->lcounter);
    while (data->lcounter) {
	    if (gcounter % 10000000 == 0)
		    printf("%c: %d\n", data->thread_id, gcounter);
	    pthread_mutex_lock(&master_lock); // wrapper; exits on failure
	    gcounter--;
	    pthread_mutex_unlock(&master_lock);
	    data->lcounter--;
    }
    printf("lcounter: %d\n", data->lcounter);
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t threads[NUM_THREADS];
    int rc;
    printf("main: begin\n");
    for (int i = 0 ; i < NUM_THREADS ; i++ ) {
        thread_data_t *data = malloc(sizeof(thread_data_t));
        data->thread_id = 'A' + i; // Assign a unique character for each thread
        data->lcounter = NUM_GLOBAL / NUM_THREADS;
	    rc = pthread_create(&threads[i], NULL, mythread, data); assert(rc == 0);
    }
    // join waits for the threads to finish
    printf("Okay, main() (our original thread) now waiting...\n");
    for (int i = 0 ; i < NUM_THREADS ; i++ ) {
	    rc = pthread_join(threads[i], NULL); assert(rc == 0);
    }
    printf("gcounter: %d\n",gcounter);
    printf("main: end\n");
    return 0; 
}
