import random
import cProfile
import time

def mergeSort(A,n):
    if n>1:
        m = n//2
        l = A[:m]
        r = A[m:]

        i=0
        j=0
        k=0

        mergeSort(l,len(l))
        mergeSort(r,len(r))

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                A[k] = l[i]
                i+=1
            else:
                A[k] = r[i]
                j+=1
            k+=1

        while i < len(l):
            A[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            A[k] = r[j]
            j += 1
            k += 1


A=[]

for i in range(0,1000000):
    n = random.randint(0,1000000)
    A.append(n)


start_time = time.time()
mergeSort(A,len(A))
print(A)
print("--- %s seconds ---" % (time.time() - start_time))
