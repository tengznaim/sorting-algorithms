def shell_sort(A):
    n = len(A)
    gap = len(A) // 2
    while gap > 0:
        print("Gap: ", gap)
        for i in range(gap, n):
            curr = A[i]
            print(A, "Current Value at Index {i}:".format(i=i),curr)
            j = i
            while j >= gap and A[j] < A[j-gap]:
                print(A[j],"is smaller than",A[j-gap],". Swap Occurs")
                print(A[j],"is inserted at index",j-gap,",",A[j-gap],"is inserted at index",j)
                A[j],A[j-gap] = A[j-gap],A[j]
                j -= gap
            A[j] = curr
        gap = gap // 2
        print()
        
    print("Sorted Array:",A)

shell_sort([154, 56, 77, 134, 186, 56, 94, 24, 13, 83, 95, 143])