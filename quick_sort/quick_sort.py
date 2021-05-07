import random


def partition(A, start, end):
    pivot_val = A[start]
    i = start
    for j in range(i+1, end):
        if A[j] >= pivot_val:
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


# test_list = [9, 20, 61, 3, 6, 55, 12, 4]
# quick_sort(test_list, 0, len(test_list))
success = 0

for i in range(1, 101):
    test_list = [random.randint(0, 101) for j in range(0, 11)]
    sort_list = test_list.copy()
    sort_list.sort()
    print("Test {i}".format(i=i), test_list)
    quick_sort(test_list, 0, len(test_list))
    if sort_list == test_list:
        print("Test Succeeded".format(i=i))
        success += 1
    else:
        print("Test Failed")

print("Success Rate: {success}/100".format(success=success))
