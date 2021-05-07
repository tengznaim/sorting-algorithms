
def merge(A, start, middle, end):

    left_subarray = A[start:middle + 1]
    right_subarray = A[middle + 1:end + 1]

    curr_index = start

    while len(left_subarray) > 0 and len(right_subarray) > 0:
        if left_subarray[0] < right_subarray[0]:
            A[curr_index] = left_subarray.pop(0)
        else:
            A[curr_index] = right_subarray.pop(0)
        curr_index += 1

    while len(left_subarray) > 0:
        A[curr_index] = left_subarray.pop(0)
        curr_index += 1

    while len(right_subarray) > 0:
        A[curr_index] = right_subarray.pop(0)
        curr_index += 1


def merge_sort(A, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(A, start, middle)
        merge_sort(A, middle+1, end)
        merge(A, start, middle, end)


A = [38, 27, 43, 3, 9, 82, 10]
merge_sort(A, 0, len(A))
print(A)
