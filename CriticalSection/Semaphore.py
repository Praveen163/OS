import threading

counter = 0  # Shared resource
semaphore = threading.Semaphore(1)  # Allows only 1 thread (acts like a mutex)

def increment_with_semaphore():
    global counter
    for _ in range(100000):
        semaphore.acquire()  # Wait for permission to enter
        # Critical Section
        counter += 1
        semaphore.release()  # Release permission

threads = [threading.Thread(target=increment_with_semaphore) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final Counter with Semaphore:", counter)
