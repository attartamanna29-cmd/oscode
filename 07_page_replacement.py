# Experiment 7: FIFO, LRU and Optimal Page Replacement

pages = list(map(int, input("Enter page reference string: ").split()))
size = int(input("Number of frames: "))

def fifo():
    frames, faults = [], 0
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) == size:
                frames.pop(0)
            frames.append(page)
    return faults

def lru():
    frames, recent, faults = [], [], 0
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) == size:
                old = recent.pop(0)
                frames.remove(old)
            frames.append(page)
        else:
            recent.remove(page)
        recent.append(page)
    return faults

def optimal():
    frames, faults = [], 0
    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) == size:
                future = pages[i+1:]
                distances = [future.index(x) if x in future else float("inf")
                             for x in frames]
                frames.pop(distances.index(max(distances)))
            frames.append(page)
    return faults

print("FIFO page faults:", fifo())
print("LRU page faults:", lru())
print("Optimal page faults:", optimal())
