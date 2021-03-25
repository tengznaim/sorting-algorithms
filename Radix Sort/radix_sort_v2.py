def counting_sort(A,exp):
    ans_array = [0]*len(A)
    count_array = [0]*10

    for i in A:
        index = (i // exp) % 10
        count_array[index] += 1
    
    for i in range(1,len(count_array)):
        count_array[i] += count_array[i-1]
    
    for i in range(len(A)-1,-1,-1):
        index = (A[i] // exp) % 10
        ans_array[count_array[index]-1] = A[i]
        count_array[index] -= 1

    return ans_array

def radix_sort(A):
    max_dig = len(str(max(A)))
    exp = 1
    for i in range(0, max_dig):
        A = counting_sort(A,exp)
        exp *= 10
    
    return A

A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
A = radix_sort(A)
print(A)