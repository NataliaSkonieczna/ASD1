
# x, y = y, x = swap
import random
import time

def partition(A,p,r):

    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j]<=x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quickSort(A,p,r):

    if (p < r):
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


A = []

for i in range(0,1000000):
    n = random.randint(0,1000000)
    A.append(n)


start_time = time.time()
quickSort(A,0,len(A)-1)
print(A)
print("--- %s seconds ---" % (time.time() - start_time))

