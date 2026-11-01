# Experiment 4: Round Robin CPU Scheduling

n = int(input("Number of processes: "))
bt = [int(input(f"Burst time of P{i+1}: ")) for i in range(n)]
q = int(input("Time quantum: "))

remaining = bt[:]
ct = [0] * n
time = 0

while any(x > 0 for x in remaining):
    for i in range(n):
        if remaining[i] > 0:
            run = min(q, remaining[i])
            time += run
            remaining[i] -= run
            if remaining[i] == 0:
                ct[i] = time

print("\nProcess   Burst   Waiting   Turnaround")
total_wt = total_tat = 0
for i in range(n):
    tat = ct[i]
    wt = tat - bt[i]
    total_wt += wt
    total_tat += tat
    print(f"P{i+1:<8}{bt[i]:<8}{wt:<10}{tat}")

print("Average waiting time:", total_wt / n)
print("Average turnaround time:", total_tat / n)
