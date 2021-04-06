# Sorting Algorithms

This is a repository for sorting algorithms I wrote and played around with as additional exercise for WIA2005 - Algorithm Design and Analysis.

These algorithms were either written from understanding (and hence may have issues with different inputs or can be implemented in a more efficient manner) or based on provided pseudocodes during lectures.

Future ideas for this repository include enhancing the algorithms and documentation on the algorithms to help understanding.

## Algorithms Currently Implemented

## Iterative

- Bubble Sort
  - Version 1 - Based on a previous Data Structure course and theoretically has a complexity of **O(n^2)**
  - Version 2 - Based on a current Algorithm Design and Analysis course and theoretically has a complexity **lower than O(n^2)** since the length of loop j decreases each iteration of i.
- Counting Sort
- Bucket Sort
  - Version 1 - Assumes a bucket size of 10.
  - Version 2 - Assumes the number of buckets to be the size of the input array. (Theoretically keeping the time complexity at **O(n)**)
  - Note: These may need further testing to prove functional for varying input.
- Shell Sort
- Radix Sort
  - Version 1 - Hacked together method that does not work properly but explores the use of string indexes.
  - Version 2 - Functional version based on the GFG guide.
  - Version 3 - Uses a hacked together bucket sort implementation. (Idea: Store the values directly rather than their indexes)
- Insertion Sort (Two versions, 1 from DS and another from Algo)

## Recursive

- Quick Sort

## References

1. Radix Sort - https://www.geeksforgeeks.org/radix-sort/
