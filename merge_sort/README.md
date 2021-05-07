# Merge Sort

![image](https://user-images.githubusercontent.com/63803360/117429594-c9f29300-af59-11eb-8c10-5ad67649d232.png)

Merge sort looks at dividing the array into equal parts until it cannot be divided anymore (the elements are standalone as seen in the diagram at level 3). The merge() function then merges the subarrays back into their sorted orders, ending up with an overall sorted version of the input array.

merge_sort()

- This is the recursive function that continuously finds the middle and divides the array into smaller sections while start < end.

merge()

- This function takes in the start, middle and end indexes and creates the left subarray and right subarray for the current call.
- The function then merges the two by sorting and placing the elements back in the original array.

The running time for this algorithm is theoretically T(N/2) + n where N/2 occurs due to recursion and n comes from the linear nature of the merge function. The time complexity is hence O(nlogn) - based on the master theorem.
