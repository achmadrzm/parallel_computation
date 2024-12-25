import threading
import time

def worker(name, delay):
    print(f"Thread {name} mulai.")
    time.sleep(delay)
    print(f"Thread {name} selesai.")

thread1 = threading.Thread(target=worker, args=("1", 2))
thread2 = threading.Thread(target=worker, args=("3", 1))

thread1.start()
thread2.start()

thread1.join()
thread2.join()