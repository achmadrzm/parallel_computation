import threading
import time

def check_value_in_list(x, i, number_of_threading):
    max_number_to_check_to = 10**8
    lower = int(i * max_number_to_check_to / number_of_threading)
    upper = int((i + 1) * max_number_to_check_to / number_of_threading)
    number_of_hits = 0
    for j in range(lower, upper):
        if j in x:
            number_of_hits += 1

    print(f'Between {lower} and {upper} number of hits is {number_of_hits}')

def main():
    start_time = time.time()
    comparison_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_of_threading = 4
    threads = []

    for i in range(number_of_threading):
        t = threading.Thread(target=check_value_in_list, args=(comparison_list, i, number_of_threading))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    print(f'Process time is {time.time() - start_time}')

if __name__ == '__main__':
    main()
