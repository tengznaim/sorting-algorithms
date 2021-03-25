#DS Style
def bubble_sort(A):
    for i in range(len(A)):
        for j in range(1, len(A)):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]

#Algo Style
def bubble_sort_v2(A):
    for i in range(len(A)-1,-1,-1):
        for j in range(1,i+1):
            if A[j-1] > A[j]:
                A[j-1],A[j]=A[j],A[j-1]

A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
bubble_sort_v2(A)
print(A)