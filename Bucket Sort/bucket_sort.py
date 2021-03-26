from math import *
import random

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

def bucket_sort(A):
    bucket_num = ceil(max(A)/10)    #Assumes a bucket size of 10, eg. with range 0-9, 10-19...
    buckets = {}
    for i in range(bucket_num + 1): #Adding 1 overcomes issue of missing numbers that are multiples of 10
        buckets[i] = []
    
    for i in A:
        idx = floor(i/10)
        buckets[idx].append(i)
    
    for key in buckets:
        if buckets[key]:    #Added a check to avoid calling insertion sort if the list is empty.
            insertion_sort(buckets[key])
    
    ans_arr = []
    for key in buckets:
        ans_arr.extend(buckets[key])

    return ans_arr

#Follows lecture pseudocode which assumes number of bucket = n
def bucket_sort_v2(A):
    bucket_num = len(A)
    buckets = {}

    for i in range(0,bucket_num):
        buckets[i] = []

    divider = ceil((max(A) + 1) / (bucket_num)) #Divider formula

    for i in A:
        idx = floor(i / divider)
        buckets[idx].append(i)
    
    for key in buckets:
        if buckets[key]:
            insertion_sort(buckets[key])

    ans_array = []
    
    for key in buckets:
        ans_array.extend(buckets[key])
    
    return ans_array

success = 0
fail = 0

for i in range(1,101):
    A_test = [random.randint(1,1000) for i in range(0,100)]
    A_compare = A_test.copy()
    A_test = bucket_sort_v2(A_test)
    A_compare.sort()    #Using in-built sort to guarantee that this is properly sorted
    if A_test == A_compare:
        print("Test {i} Passed. The lists are equal".format(i=i))
        success += 1
    else:
        print("Test {i} Failed. The lists are not equal".format(i=i))
        fail += 1
    
rate = (success + fail) / 100 * 100
print("Success Rate: {rate}%".format(rate=rate))