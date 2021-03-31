import random


def counting_sort(A, exp):
    ans_array = [0]*len(A)
    count_array = [0]*10

    for i in A:
        index = (i // exp) % 10
        count_array[index] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i-1]

    for i in range(len(A)-1, -1, -1):
        index = (A[i] // exp) % 10
        ans_array[count_array[index]-1] = A[i]
        count_array[index] -= 1

    return ans_array


def radix_sort(A):
    max_dig = len(str(max(A)))
    exp = 1
    for i in range(0, max_dig):
        A = counting_sort(A, exp)
        exp *= 10

    return A

# A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
# A = radix_sort(A)
# print(A)


success = 0
fail = 0

for i in range(1, 101):
    A_test = [random.randint(1, 1000) for i in range(0, 100)]
    A_compare = A_test.copy()
    A_test = radix_sort(A_test)
    A_compare.sort()  # Using in-built sort to guarantee that this is properly sorted
    if A_test == A_compare:
        print("Test {i} Passed. The lists are equal".format(i=i))
        success += 1
    else:
        print("Test {i} Failed. The lists are not equal".format(i=i))
        fail += 1

rate = (success + fail) / 100 * 100
print("Success Rate: {rate}%".format(rate=rate))
