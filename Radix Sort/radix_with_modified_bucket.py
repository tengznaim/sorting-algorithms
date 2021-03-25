def modified_bucket(A,exp):
    bucket = {}
    for i in range(0,10):
        bucket[i] = []
    
    for i in A:
        index = (i // exp) % 10
        bucket[index].append(i)

    ans_array = []
    
    for key,value in bucket.items():
        ans_array.extend(value)
    
    return ans_array

def radix_sort(A):
    max_dig = len(str(max(A)))
    exp = 1
    for i in range(0, max_dig):
        A = modified_bucket(A,exp)
        exp *= 10
    
    return A

A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
A = radix_sort(A)
print(A)