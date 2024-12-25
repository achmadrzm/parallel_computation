import threading
import time
def func():
    print("ran\n")
    time.sleep(3)
    print("done")
    print("Thread aktif:", threading.active_count())

x = threading.Thread(target=func)
x.start()