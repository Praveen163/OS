import threading
import time

# SpinLock manually checks lock status without sleeping the thread
class SpinLock:
    def __init__(self):
        self.locked = False
        self.lock = threading.Lock()  # Internal mutex to protect the flag

    def acquire(self):
        # Busy waiting until the lock becomes available
        while True:
            with self.lock:
                if not self.locked:
                    self.locked = True
                    return
            time.sleep(0)  # Yield control to reduce CPU load

    def release(self):
        with self.lock:
            self.locked = False  # Mark the lock as available

counter = 0
spinlock = SpinLock()

def increment_with_spinlock():
    global counter
    for _ in range(100000):
        spinlock.acquire()   # Busy wait until lock is acquired
        counter += 1         # Critical Section
        spinlock.release()   # Release lock

threads = [threading.Thread(target=increment_with_spinlock) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final Counter with Spinlock:", counter)
