#Algo Style
def insertion_sort(A):
    for i in range(1, len(A)):
        curr = A[i]
        j = i-1
        while j >= 0 and A[j] > curr:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = curr

#DS Style
def insertion_sort_v2(A):
    for i in range(1, len(A)):
        stop = 0
        for j in range(i):
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]
                stop = j
                break
        for j in range(stop+1,i):
            A[j],A[i] = A[i],A[j]

A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
insertion_sort(A)
print(A)