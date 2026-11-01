# Experiment 5: Dining Philosophers using semaphores

import threading
import time

N = 5
forks = [threading.Semaphore(1) for _ in range(N)]
room = threading.Semaphore(N - 1)  # prevents deadlock

def philosopher(i):
    left = i
    right = (i + 1) % N

    for _ in range(2):
        print(f"Philosopher {i+1} is thinking")
        time.sleep(0.3)

        room.acquire()
        forks[left].acquire()
        forks[right].acquire()

        print(f"Philosopher {i+1} is eating")
        time.sleep(0.3)

        forks[right].release()
        forks[left].release()
        room.release()

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("All philosophers finished.")
