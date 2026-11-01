# Experiment 9: Disk Scheduling Algorithms

requests = list(map(int, input("Enter disk requests: ").split()))
head = int(input("Initial head position: "))
size = int(input("Disk size (e.g. 200): "))
direction = input("Direction for SCAN/LOOK (L or R): ").upper()

def result(name, order):
    movement = abs(head - order[0]) if order else 0
    for a, b in zip(order, order[1:]):
        movement += abs(b - a)
    print(name, "order:", order, "| Total head movement:", movement)

# FCFS
result("FCFS", requests)

# SSTF
left = requests[:]
pos, order = head, []
while left:
    nxt = min(left, key=lambda x: abs(x - pos))
    order.append(nxt)
    left.remove(nxt)
    pos = nxt
result("SSTF", order)

left = sorted(x for x in requests if x < head)
right = sorted(x for x in requests if x >= head)

# SCAN
if direction == "R":
    scan = right + ([size - 1] if right or left else []) + left[::-1]
else:
    scan = left[::-1] + ([0] if left or right else []) + right
result("SCAN", scan)

# C-SCAN
if direction == "R":
    cscan = right + ([size - 1, 0] if left else []) + left
else:
    cscan = left[::-1] + ([0, size - 1] if right else []) + right[::-1]
result("C-SCAN", cscan)

# LOOK
look = right + left[::-1] if direction == "R" else left[::-1] + right
result("LOOK", look)

# C-LOOK
clook = (right + left) if direction == "R" else (left[::-1] + right[::-1])
result("C-LOOK", clook)
