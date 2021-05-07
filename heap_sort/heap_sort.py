'''
Heap Sort Algorithm for sorting in increasing order: 
1. Build a max heap from the input data. 
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree. 
3. Repeat step 2 while size of heap is greater than 1.
'''

'''
If the parent node is stored at index I, the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).
'''


def max_heapify_loop(A):

    i = len(A) // 2

    while i > -1:

        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(A) and A[left] > A[largest]:
            largest = left
        if right < len(A) and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[largest], A[i] = A[i], A[largest]
            i = largest
        else:
            i -= 1

    print("Max Heap Loop:", A)


def max_heapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[largest] < A[left]:
        largest = left

    if right < n and A[largest] < A[right]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def heap_sort(A):
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, n, i)

    print("Max Heap Recursive", A)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)


A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
A_test = A.copy()
heap_sort(A)
max_heapify_loop(A_test)
print(A)
