import random
import time
# x, y = y, x = swap

def heapify(A, n, i):
    l = 2 * i+1
    r = 2 * i+2
    largest = i
    if l < n and A[l]> A[largest]:
        largest = l
    if r < n and A[r]> A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def heapSort(A):
    n = len(A)

    for i in range(n//2-1,-1,-1):
        heapify(A, n, i)

    for i in range(n-1,0,-1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)


A = []

for i in range(0,100000):
    n = random.randint(0,100000)
    A.append(n)


start_time = time.time()
heapSort(A)
print(A)
print("--- %s seconds ---" % (time.time() - start_time))
#posortowana rosnaco

