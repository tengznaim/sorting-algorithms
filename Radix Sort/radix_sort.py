#This version is not currently working

from math import *

def counting_sort(A):
    max_num = max(A)
    count_array = [0]*(max_num+1)

    for i in A:
        count_array[i] += 1
    
    for i in range(1,max_num+1):
        count_array[i] += count_array[i-1]
    
    print(count_array)
    
    ans_array = [0]*len(A)

    for i in A:
        idx = count_array[i]
        print(idx)
        ans_array[idx-1] = i
        count_array[i] -= 1
    
    return ans_array

#One digit only
def radix_sort(A):
	index_count = {}
	max_digit = len(str(max(A)))
	
	for i in range(0,10):
		index_count[i] = []
	
	for i in A:
		num_conv = str(i)
			
		digit = int(num_conv[len(num_conv) - 1])
		print(digit)
		index_count[digit].append(i)
	
	ans_arr = []
	for key in index_count:
		ans_arr.extend(index_count[key])
	
	print(ans_arr)

A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
radix_sort(A)
print(A)