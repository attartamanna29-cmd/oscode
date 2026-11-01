# Experiment 3: Non-preemptive SJF Scheduling

n = int(input("Number of processes: "))
p = []
for i in range(n):
    bt = int(input(f"Burst time of P{i+1}: "))
    p.append((i+1, bt))

p.sort(key=lambda x: x[1])
time = 0
total_wt = total_tat = 0

print("\nProcess   Burst   Waiting   Turnaround")
for pid, bt in p:
    wt = time
    tat = wt + bt
    print(f"P{pid:<8}{bt:<8}{wt:<10}{tat}")
    total_wt += wt
    total_tat += tat
    time += bt

print("Average waiting time:", total_wt / n)
print("Average turnaround time:", total_tat / n)
