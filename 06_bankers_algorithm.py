# Experiment 6: Banker's Algorithm (Safety Check)

n = int(input("Number of processes: "))
m = int(input("Number of resource types: "))

print("Enter Allocation matrix:")
alloc = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]

print("Enter Max matrix:")
maximum = [list(map(int, input(f"P{i}: ").split())) for i in range(n)]

available = list(map(int, input("Enter Available resources: ").split()))
need = [[maximum[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

finish = [False] * n
safe = []

while len(safe) < n:
    found = False
    for i in range(n):
        if not finish[i] and all(need[i][j] <= available[j] for j in range(m)):
            available = [available[j] + alloc[i][j] for j in range(m)]
            finish[i] = True
            safe.append(i)
            found = True
    if not found:
        break

if len(safe) == n:
    print("System is in SAFE state.")
    print("Safe sequence:", " -> ".join("P" + str(i) for i in safe))
else:
    print("System is NOT in a safe state.")
