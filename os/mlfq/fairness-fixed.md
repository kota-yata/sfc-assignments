## Four identical jobs (20 time units each) arriving at time 0
Command: python3 mlfq-fairness.py -l 0,20,0:0,20,0:0,20,0:0,20,0 -c

Results:
- Job 0: turnaround 50, normalized turnaround 2.5
- Job 1: turnaround 60, normalized turnaround 3.0  
- Job 2: turnaround 70, normalized turnaround 3.5
- Job 3: turnaround 80, normalized turnaround 4.0

Fairness: 97.1% fair (Jain's index: 0.971)

## Three identical jobs (30 time units each) with staggered arrivals at times 0, 5, and 10
Command: python3 mlfq-fairness.py -l 0,30,0:5,30,0:10,30,0 -c

Results:
- Job 0: turnaround 70, normalized turnaround 2.33
- Job 1: turnaround 75, normalized turnaround 2.50
- Job 2: turnaround 80, normalized turnaround 2.67

Fairness: 99.7% fair (Jain's index: 0.997)

## Four identical jobs with priority boost every 40 time units
Command: python3 mlfq-fairness.py -l 0,20,0:0,20,0:0,20,0:0,20,0 -B 40 -c

Results:
- Job 0: turnaround 50, normalized turnaround 2.5
- Job 1: turnaround 60, normalized turnaround 3.0
- Job 2: turnaround 70, normalized turnaround 3.5
- Job 3: turnaround 80, normalized turnaround 4.0

Fairness: 97.1% fair (Jain's index: 0.971)
