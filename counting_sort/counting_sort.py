def counting_sort(A):
    max_num = max(A)
    count_array = [0]*(max_num+1)

    for i in A:
        count_array[i] += 1

    for i in range(1, max_num+1):
        count_array[i] += count_array[i-1]

    ans_array = [0]*len(A)

    for i in A:
        idx = count_array[i]
        ans_array[idx-1] = i
        count_array[i] -= 1

    return ans_array


A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
A = counting_sort(A)
print(A)
