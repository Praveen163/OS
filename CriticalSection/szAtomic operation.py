import threading

# Simulating CAS with a lock (Python doesn't support true atomic CAS)
class AtomicCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()  # Used to simulate atomic behavior

    def compare_and_swap(self, expected, new):
        with self.lock:
            if self.value == expected:
                self.value = new
                return True
            return False

    def increment(self):
        while True:
            old_val = self.value
            # Try to set value only if it's still old_val
            if self.compare_and_swap(old_val, old_val + 1):
                break  # Successful update; exit loop

atomic_counter = AtomicCounter()

def increment_with_cas():
    for _ in range(100000):
        atomic_counter.increment()

threads = [threading.Thread(target=increment_with_cas) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final Counter with CAS Simulation:", atomic_counter.value)
