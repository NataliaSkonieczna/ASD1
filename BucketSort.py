#len(str(123))
import random
import time

def bucketSort(A,n):
    C = [0,0,0,0,0,0,0,0,0,0]
    B = A
    for i in range(n):

        digit = A[i]
        a=1
        b=1
        nlen = len(str(n))

        for j in range(nlen):
            a=a*10

        if A[i]>=a:
            digit = int(repr(A[i])[-b])


        for m in range (digit,10):
            C[m] +=1

    A = A[::-1]

    for k in range(n):
        for l in range(10):
            if A[k] == l:
                B[C[l]-1]=A[k]
                C[l] -= 1
    print(B)





A = []

for i in range(0,1000000):
    n = random.randint(0,9)
    A.append(n)


start_time = time.time()
bucketSort(A,len(A))
print("--- %s seconds ---" % (time.time() - start_time))
#posortowana rosnaco