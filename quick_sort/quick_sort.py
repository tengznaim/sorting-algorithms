
def partition(A, start, end):
    pivot_val = A[start]
    i = start
    for j in range(i+1, end):
        if A[j] <= pivot_val:
            A[i+1], A[j] = A[j], A[i+1]
            i += 1
            j += 1
        else:
            j += 1

    A[start], A[i] = A[i], A[start]
    return i


def quick_sort(A, start, end):
    if start < end:
        pivot_index = partition(A, start, end)
        quick_sort(A, start, pivot_index)
        quick_sort(A, pivot_index + 1, end)


A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
print("Original List:", A)
quick_sort(A, 0, len(A))
print("Sorted List", A)
