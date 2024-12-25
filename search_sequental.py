import time

def check_value_in_list(x):
    max_number_to_check_to = 10**9
    number_of_hits = 0
    for j in range(max_number_to_check_to):
        if j in x:
            number_of_hits += 1

    print(f'Between 0 and {max_number_to_check_to} number of hits is {number_of_hits}')

def main():
    start_time = time.time()
    comparison_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    check_value_in_list(comparison_list)
    print(f'Process time is {time.time() - start_time}')

if __name__ == '__main__':
    main()