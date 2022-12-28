----Divide and conquer-----

Divide and Conquer algorithm consists of a dispute using the following three steps.
Divide the original problem into a set of sub problems.
Conquer: Solve every subproblem individually, recursively.
Combine: Put together the solutions of the sub problems to get the solution to the whole problem.

------merge sort-----
Merge sort:Merge sort is one of the most efficient sorting techniques and it’s based on the “divide and conquer” algorithm.
It is a sorting algorithm that sorts an array by making comparisons. It starts by dividing an array into sub-array and then recursively sorts each of them. After the sorting is done, it merges them back.

----pseudo code for Merge sort---

MERGE-SORT(A, p, r)

1. if p<r
2. q = (p + r)/2
   (Find the middle point to divide the array into two halves:)
3. MERGE-SORT (A, p, q)
   (Call mergeSort for first half)
4. MERGE-SORT(A, q + 1, r)
   (Call mergeSort for second half)
5. MERGE(A, p, q, r)
   Merge the two halves sorted

   MERGE(A, p, q, r)

6. n1 = q - p + 1
7. n2 = r - q
8. let L[1....n1 + 1] and R[1....n+1} be new arrays]
9. for i = 1 to n1
10. L[i] = A[p + i -1]
11. for j = 1 to n2
12. R[j] = A[q + j]
13. L[n1+1] = infinity sign
14. R[n2 +1] = infinity sign
15. i = 1
16. j = 1
17. for k = p to r
18. if L[i]<= R[j]
19. A[k] = L[i]
20. i = i + 1
21. else A[k] =R[j]
22. j = j + 1

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20220722205737/MergeSortTutorial.png)
