"""
Buatlah program sederhana dengan salah satu dari konsep paralel berikut ini dalam bentuk video:
Explicit paralelism / Concurrency / MPI.
Ketentuan:
1. Video harus terlihat orang dan terdengar audionya
2. Durasi video 5-10 menit
3. Jelaskan programnya dan running
4. Sertakan juga laporan untuk penjelasan programnya.
5. Upload file dalam bentuk .pdf untuk laporan, dan sertakan URL video pada google drive kalian.
"""
#Explicit Parallelism -> Threading

import threading
import time

def print_numbers():
	for i in range(1, 8):
		print(f"Printing number {i}")
		time.sleep(1)

def print_letters():
	for letter in 'paralel':
		print(f"Printing letter {letter}")
		time.sleep(1)
		
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished.")