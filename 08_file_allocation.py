# Experiment 8: File Allocation Techniques
# Demonstrates contiguous, linked and indexed allocation.

disk_size = 20
print("Disk blocks: 0 to", disk_size - 1)
start = int(input("Starting block for file: "))
count = int(input("Number of blocks required: "))

# Contiguous allocation
if 0 <= start and start + count <= disk_size:
    print("Contiguous:", list(range(start, start + count)))
else:
    print("Contiguous: Not enough consecutive space.")

# Linked allocation (illustrative block chain)
if count <= disk_size:
    linked = [(start + i) % disk_size for i in range(count)]
    print("Linked chain:", " -> ".join(map(str, linked)))
else:
    print("Linked: File is larger than disk.")

# Indexed allocation (first block is used as index block)
if count + 1 <= disk_size:
    data = [(start + i + 1) % disk_size for i in range(count)]
    print("Index block:", start)
    print("Indexed data blocks:", data)
else:
    print("Indexed: Not enough blocks.")
