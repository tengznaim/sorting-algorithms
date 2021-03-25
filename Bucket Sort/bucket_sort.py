from math import *

#Algo Style
def insertion_sort(A):
    for i in range(1, len(A)):
        curr = A[i]
        j = i-1
        while j >= 0 and A[j] > curr:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = curr

#DS Style
def insertion_sort_v2(A):
    for i in range(1, len(A)):
        stop = 0
        for j in range(i):
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]
                stop = j
                break
        for j in range(stop+1,i):
            A[j],A[i] = A[i],A[j]

#Main bedal, may be inaccurate for certain test cases
def bucket_sort(A):
    bucket_num = ceil(max(A)/10)
    buckets = {}
    for i in range(bucket_num):
        buckets[i] = []
    
    for i in A:
        idx = floor(i/10)
        buckets[idx].append(i)
    
    for key in buckets:
        insertion_sort(buckets[key])
    
    ans_arr = []
    for key in buckets:
        ans_arr.extend(buckets[key])

A = [154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143]
bucket_sort(A)
print(A)