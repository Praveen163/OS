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
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads completed.")
