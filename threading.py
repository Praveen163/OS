import threading  # Module to create and manage threads
import time        # For simulating delays (to observe context switching)

# Function that will run in a thread\
count = 0
def print_numbers(name):
    for i in range(5):
        global count
        count += 2
        print(f"Thread {name} printing: {i}")
        time.sleep(0.1)  
        print(count)
        # Sleep to simulate I/O or computation delay
        # This sleep allows other threads to get CPU time (context switch)

# Create two threads
thread1 = threading.Thread(target=print_numbers, args=("A",))
thread2 = threading.Thread(target=print_numbers, args=("B",))

# Start the threads
print("Starting Threads...")
thread1.start() #new thread banake k background m fhek do...main programe ko chalne do
thread2.start()

# Wait for both threads to finish
thread1.join() #main programe ko roko tab tak ye thread complete nhi hoti
thread2.join()

print("Both threads completed.")











#using lock ......... no context switching at that point...only one thread to enter at a time
lock = threading.Lock()
shared_counter = 0
def increment():
    global shared_counter
    for _ in range(100000):
        lock.acquire()
        shared_counter += 1
        lock.release()

#using semaphore ... N threads allow to enter at a time
sem = threading.Semaphore(3)
def worker():
    with sem:
        # at most 3 threads here
        do_work()
