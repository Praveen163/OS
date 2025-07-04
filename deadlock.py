import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print("Thread 1 acquired Lock 1")
        # Simulate delay
        import time; time.sleep(1)
        with lock2:
            print("Thread 1 acquired Lock 2")

def thread2():
    with lock2:
        print("Thread 2 acquired Lock 2")
        import time; time.sleep(1)
        with lock1:
            print("Thread 2 acquired Lock 1")

# Start both threads
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()
t1.join()
t2.join()








# Deadlock Prevention – Break one of the four conditions:

# No mutual exclusion (use shared resources)

# No hold-and-wait (require all resources at once)

# Allow preemption

# Impose ordering on resources

# Deadlock Avoidance – Use algorithms like:

# Banker’s Algorithm

# Deadlock Detection and Recovery

# Allow deadlocks but detect them and recover by:

# Killing one or more processes

# Forcibly taking resources back

