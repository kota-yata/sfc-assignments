## Random variable-length jobs with I/O (seed=1)
Command: python3 mlfq-fairness.py -j 4 -s 1 -c

Job specifications:
- Job 0: 14 time units, I/O every 8 units
- Job 1: 76 time units, I/O every 3 units  
- Job 2: 50 time units, I/O every 5 units
- Job 3: 65 time units, I/O every 8 units

Results:
- Job 0: turnaround 43, normalized turnaround 3.07
- Job 1: turnaround 269, normalized turnaround 3.54
- Job 2: turnaround 153, normalized turnaround 3.06
- Job 3: turnaround 170, normalized turnaround 2.62

Fairness: 98.9% fair (Jain's index: 0.989)

## Manual variable-length jobs without I/O
Command: python3 mlfq-fairness.py -l 0,10,0:0,40,0:0,60,0 -c

Job specifications:
- Job 0: 10 time units, no I/O
- Job 1: 40 time units, no I/O
- Job 2: 60 time units, no I/O

Results:
- Job 0: turnaround 10, normalized turnaround 1.0
- Job 1: turnaround 80, normalized turnaround 2.0
- Job 2: turnaround 110, normalized turnaround 1.83

Fairness: 93.1% fair (Jain's index: 0.931)

## Random variable-length jobs with frequent I/O (seed=42)
Command: python3 mlfq-fairness.py -j 5 -s 42 -c

Job specifications:
- Job 0: 64 time units, I/O every 1 unit
- Job 1: 28 time units, I/O every 3 units
- Job 2: 73 time units, I/O every 7 units
- Job 3: 89 time units, I/O every 1 unit
- Job 4: 42 time units, I/O every 1 unit

Results:
- Job 0: turnaround 353, normalized turnaround 5.52
- Job 1: turnaround 128, normalized turnaround 4.57
- Job 2: turnaround 191, normalized turnaround 2.62
- Job 3: turnaround 365, normalized turnaround 4.10
- Job 4: turnaround 284, normalized turnaround 6.76

Fairness: 83.0% fair (Jain's index: 0.830)
