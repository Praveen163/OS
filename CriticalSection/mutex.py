
import threading
#Peterson’s algorithm
counter = 0  # Shared resource
lock = threading.Lock()  # A lock to control access

def increment_with_lock():
    global counter
    for _ in range(100000):
        # Only one thread can acquire the lock at a time
        with lock:
            # Critical Section: only one thread allowed here
            counter += 1

# Create 5 threads that try to increment the counter
threads = [threading.Thread(target=increment_with_lock) for _ in range(5)]

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Final Counter with Lock:", counter)
