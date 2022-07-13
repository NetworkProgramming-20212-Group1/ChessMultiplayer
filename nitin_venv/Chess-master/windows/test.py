from threading import Thread
import time

class A:
    queue = []

a = A()

def thread2(threadname, q):
    a = 0
    for _ in range(10):
        a += 1
        q.append(a)
        time.sleep(1)
    q.put(None) # Poison pill


thread2 = Thread( target=thread2, args=("Thread-2", a.queue) )

thread2.start()
while 1:
    print(a.queue)