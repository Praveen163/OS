#cook counterTop waiter -- counterTop limit-3

import threading
import time

buffer = []
BUFFER_SIZE = 5

def producer():
    for i in range(10):
        while len(buffer) == BUFFER_SIZE:
            pass  # wait if buffer is full

        buffer.append(i)
        print("Produced:", i)
        time.sleep(0.5)

def consumer():
    for i in range(10):
        while not buffer:
            pass  # wait if buffer is empty

        item = buffer.pop(0)
        print("Consumed:", item)
        time.sleep(1)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
