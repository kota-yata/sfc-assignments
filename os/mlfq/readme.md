2. Do problem 1 from Ch. 8.    *Describe* what you found, and include the output of each run as a separate file.
  -> **Description in 1-describe.txt. The result in 1-result.txt**

3. For problem 2 from Ch. 8: configure mlfq.py to reproduce Figs. 8.2, 8.3, 8.4, and 8.6.  Run it.  *Describe* what you found, and include the output of each run as a separate file.
  -> **Description in 2-describe.md. Result files are 2-*.result.txt**

4. Make sure you understand fairness. See The 2019 lecture notes on schedulingLinks to an external site. for a discussion of Jain's definition of fairness.

The program mlfq.py already reports average completion time (the "turnaround" above).  Extend the program to report fairness also.  This is a bit of a big deal; you will have to think about how to calculate fairness when there are jobs of varying lengths.

  a. Write a description of how you would calculate this in a round-robin multitasking environment.  (That is, the job doesn't "own" the CPU; it shares it round-robin fashion.  The simulator already _does_ this, but it doesn't report the fairness, and you may need to adapt the definition of fairness.) (It's okay if you find a suggestion on the web, but indicate where you got it, if so!)
    -> **fairness.md**

  b. Add it into the program, *with comments in the code*.
    -> **mlfq-fairness.py**

  c. Run this with a set of fixed-length (not random length) jobs and report the fairness achieved.
    -> **fairness-fixed.md**

  d. Rerun the problems for the same set of figures above and report the fairness achieved.  (So this includes variable-length jobs.)
    -> **fairness-variable.md**