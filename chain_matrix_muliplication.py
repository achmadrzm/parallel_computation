import numpy as np
import multiprocessing

def multiply_matrices(A, B, result_queue):
    result = np.dot(A, B)
    result_queue.put(result)

def chained_matrix_multiplication():
    A = np.array([[1, 2, 3, 4, 5],
                  [5, 4, 3, 2, 1],
                  [1, 1, 1, 1, 1],
                  [2, 3, 4, 5, 6],
                  [6, 5, 4, 3, 2]])

    B = np.array([[2, 4, 6, 8, 10],
                  [1, 3, 5, 7, 9],
                  [2, 2, 2, 2, 2],
                  [3, 3, 3, 3, 3],
                  [4, 4, 4, 4, 4]])

    C = np.array([[1, 0, 0, 0, 1],
                  [0, 1, 0, 1, 0],
                  [0, 0, 1, 0, 0],
                  [1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 1]])

    D = np.array([[2, 1, 2, 1, 2],
                  [1, 2, 1, 2, 1],
                  [2, 1, 2, 1, 2],
                  [1, 2, 1, 2, 1],
                  [2, 1, 2, 1, 2]])

    E = np.array([[3, 1, 4, 1, 5],
                  [9, 2, 6, 5, 3],
                  [5, 8, 9, 7, 9],
                  [3, 2, 3, 8, 4],
                  [6, 2, 7, 9, 5]])

    F = np.array([[8, 5, 9, 7, 9],
                  [3, 2, 3, 8, 4],
                  [6, 2, 7, 9, 5],
                  [3, 1, 4, 1, 5],
                  [9, 2, 6, 5, 3]])

    G = np.array([[5, 4, 3, 2, 1],
                  [1, 2, 3, 4, 5],
                  [9, 8, 7, 6, 5],
                  [5, 6, 7, 8, 9],
                  [0, 1, 2, 3, 4]])

    H = np.array([[1, 1, 1, 1, 1],
                  [2, 2, 2, 2, 2],
                  [3, 3, 3, 3, 3],
                  [4, 4, 4, 4, 4],
                  [5, 5, 5, 5, 5]])

    result_queue = multiprocessing.Queue()

    # Multiproses pertama (A x B, C x D, E x F, G x H)
    p1 = multiprocessing.Process(target=multiply_matrices, args=(A, B, result_queue))
    p2 = multiprocessing.Process(target=multiply_matrices, args=(C, D, result_queue))
    p3 = multiprocessing.Process(target=multiply_matrices, args=(E, F, result_queue))
    p4 = multiprocessing.Process(target=multiply_matrices, args=(G, H, result_queue))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    AB = result_queue.get()
    CD = result_queue.get()
    EF = result_queue.get()
    GH = result_queue.get()

    # Multiproses kedua (AB x CD, EF x GH)
    p5 = multiprocessing.Process(target=multiply_matrices, args=(AB, CD, result_queue))
    p6 = multiprocessing.Process(target=multiply_matrices, args=(EF, GH, result_queue))

    p5.start()
    p6.start()

    p5.join()
    p6.join()

    ABCD = result_queue.get()
    EFGH = result_queue.get()

    # Proses terakhir (ABCD x EFGH)
    p7 = multiprocessing.Process(target=multiply_matrices, args=(ABCD, EFGH, result_queue))

    p7.start()
    p7.join()

    Y = result_queue.get()

    print("Matriks Y:")
    print(Y)

if __name__ == "__main__":
    chained_matrix_multiplication()
