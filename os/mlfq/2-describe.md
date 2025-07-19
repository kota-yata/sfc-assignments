## Fig 8.2
- Reproducing command: python3 mlfq.py --jlist 0,180,0 -q 10 -c
- Result: 2-8.2-result.txt
- What I've found: I could see the job went down the priority queue at every slice

## Fig 8.3
- Reproducing command: python3 mlfq.py --jlist 0,180,0:100,20,0 -q 10 -c
- Result: 2-8.3-result.txt
- What I've found: The first job went down the queue in the same way as the reproduction of 8.2, and the second job interrupted the first job as the figure shows

## Fig 8.4
- Reproducing command: python3 mlfq.py --jlist 0,200,0:0,20,1 -q 10 -c
- Result: 2-8.4-result.txt
- What I've found: The second job stayed at the top-priority queue until it was done

## Fig 8.6
- Reproducing command: python3 mlfq.py --jlist 0,200,0:50,100,9 -q 10 -A 1,1,0 -
- Result: 2-8.6-result.txt
- What I've found: The second job went down the queue even if I set it to throw an IO operation every 9ms (1ms before time slice period)
