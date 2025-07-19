### Fairness Metric Choice
For calculating fairness in a round-robin multitasking environment, I used turnaround time normalized for variable-length jobs. Normalized turnaround time is calculated with the original turnaround time / its job length. A perfectly fair system would give all jobs the same normalized turnaround time.

See mlfq-fairness.py for the actual implementation
