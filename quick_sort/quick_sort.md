# Quick Sort

The algorithm here is written based on the pseudocode below:
![image](https://user-images.githubusercontent.com/63803360/113714276-ced5e400-971a-11eb-8ee8-06acffa2ddf6.png)

The idea here is to get a pivot value and place all values smaller than the pivot to the left of the pivot and those larger to the right of the pivot. Once this is done, we return the index of the pivot for use in the next recursion calls where the sublists to be sorted would be from:

**start -> pivot_index, [this is where the pivot is], pivot_index+1 -> end**

Through observation, I believe this keeps taking the leftmost value as the pivot value. Hence, I personally think this algorithm could be improved upon.

\*Note that this algorithm requires further testing and I do not particularly know if it is 100% functional all the time.
