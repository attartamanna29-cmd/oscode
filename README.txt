OPERATING SYSTEM PRACTICALS - PYTHON
===================================

Files included:
1. Linux command practice
2. FCFS and Priority scheduling
3. SJF scheduling
4. Round Robin scheduling
5. Dining Philosophers
6. Banker's deadlock-avoidance algorithm
7. FIFO, LRU and Optimal page replacement
8. Contiguous, Linked and Indexed file allocation
9. FCFS, SSTF, SCAN, C-SCAN, LOOK and C-LOOK disk scheduling
10. Advanced OS case-study study aid

HOW TO RUN IN VS CODE
---------------------
1. Extract this ZIP folder.
2. Open the extracted folder in VS Code.
3. Open a Python file.
4. Open Terminal > New Terminal.
5. Run: python filename.py
   Example: python 02_fcfs_priority.py

Use Python 3. No extra libraries are required.
For programs that ask for multiple values in one line, separate values with spaces.

NOTES
-----
- In Priority Scheduling, a smaller priority number means higher priority.
- SJF, FCFS and Priority examples are non-preemptive.
- Round Robin uses the time quantum entered by you.
- Banker's algorithm expects one row per process in Allocation and Max matrices.
- The disk scheduling program assumes cylinders are numbered 0 to (disk size - 1).
- Experiment 10 is a case study/theory topic, so there is no single standard algorithm.
  The included menu is a small study aid; prepare real-world examples and advantages
  for your viva as well.
- Experiment 1 uses Python equivalents so it can run in Windows VS Code too.
  The actual Linux commands are pwd, ls, mkdir, touch, cat, date and whoami.