import threading
import time
import random

def worker(name, delay):
    print(f"Thread {name} mulai.")
    time.sleep(delay)
    print(f"Thread {name} selesai.")

def create_threads(jumlah_thread):
    threads = []
    
    for i in range(jumlah_thread):
        delay = random.uniform(0.5, 2.0)
        t = threading.Thread(target=worker, args=(f"{i+1}", delay))
        threads.append(t)
        t.start()
        
        time.sleep(0.5)

    return threads

def main():
    jumlah_thread = random.randint(2, 7)
    print(f"Membuat {jumlah_thread} thread.")
    
    threads = create_threads(jumlah_thread)
    
    for t in threads:
        t.join()
    
    print("Semua thread selesai.")

if __name__ == "__main__":
    main()
