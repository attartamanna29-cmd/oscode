# Experiment 2: FCFS and Non-preemptive Priority Scheduling

n = int(input("Number of processes: "))
p = []
for i in range(n):
    bt = int(input(f"Burst time of P{i+1}: "))
    pr = int(input(f"Priority of P{i+1} (smaller = higher): "))
    p.append([i+1, bt, pr])

def show(processes, title):
    time = 0
    wt, tat = {}, {}
    for pid, bt, pr in processes:
        wt[pid] = time
        time += bt
        tat[pid] = time
    print("\n", title)
    print("Process   Waiting   Turnaround")
    for pid, bt, pr in processes:
        print(f"P{pid:<8}{wt[pid]:<10}{tat[pid]}")
    print("Average waiting time:", sum(wt.values()) / len(p))
    print("Average turnaround time:", sum(tat.values()) / len(p))

show(p[:], "FCFS")
show(sorted(p, key=lambda x: x[2]), "Priority Scheduling")
