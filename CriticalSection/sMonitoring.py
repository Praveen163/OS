import threading

# Encapsulating shared state and locking logic into a class (monitor)
class CounterMonitor:
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)  # Lock + condition variable

    def increment(self):
        with self.condition:  # This acquires the lock
            # Critical Section
            self.counter += 1
            # No need to use wait/notify in this case

monitor = CounterMonitor()

def thread_with_monitor():
    for _ in range(100000):
        monitor.increment()

threads = [threading.Thread(target=thread_with_monitor) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final Counter with Monitor:", monitor.counter)



#new learning
import threading

class CounterMonitor:
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:   # monitor lock
            self.counter += 1

counter = CounterMonitor()

def worker():
    for _ in range(100000):
        counter.increment()

threads = [threading.Thread(target=worker) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter.counter)  # Always correct

