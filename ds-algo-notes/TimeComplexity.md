**Time complexity** is a way of expressing how the running time of an algorithm grows as the size of the input increases. It provides an upper bound on the amount of time an algorithm takes to complete as a function of the input size. Time complexity helps in analyzing the efficiency of an algorithm, particularly for large inputs.

### Common Time Complexities

1. **Constant Time - O(1)**:
   - The algorithm takes the same amount of time regardless of the size of the input.
   - **Example**: Accessing an element in an array by index.
     ```python
     def get_element(arr, index):
         return arr[index]
     ```
     Here, no matter how large the array is, the operation takes constant time.

2. **Linear Time - O(n)**:
   - The running time grows directly in proportion to the size of the input.
   - **Example**: A loop that iterates through all elements of a list.
     ```python
     def print_elements(arr):
         for element in arr:
             print(element)
     ```
     If the array has \( n \) elements, the algorithm will perform \( n \) operations.

3. **Quadratic Time - O(n²)**:
   - The running time grows in proportion to the square of the size of the input.
   - **Example**: A nested loop that processes each pair of elements in an array.
     ```python
     def print_pairs(arr):
         for i in arr:
             for j in arr:
                 print(i, j)
     ```
     If the array has \( n \) elements, the outer loop runs \( n \) times, and for each iteration of the outer loop, the inner loop also runs \( n \) times, leading to \( n^2 \) operations.

4. **Logarithmic Time - O(log n)**:
   - The running time grows logarithmically as the input size increases. This usually happens when the problem is divided in half at each step (e.g., binary search).
   - **Example**: Binary search in a sorted array.
     ```python
     def binary_search(arr, target):
         low, high = 0, len(arr) - 1
         while low <= high:
             mid = (low + high) // 2
             if arr[mid] == target:
                 return mid
             elif arr[mid] < target:
                 low = mid + 1
             else:
                 high = mid - 1
         return -1
     ```
     In a sorted array of size \( n \), the algorithm repeatedly divides the search range in half, so the time complexity is \( O(\log n) \).

5. **Linearithmic Time - O(n log n)**:
   - The running time grows proportionally to \( n \) times the logarithm of \( n \). This is typical in more efficient sorting algorithms like Merge Sort or Quick Sort.
   - **Example**: Merge sort.
     ```python
     def merge_sort(arr):
         if len(arr) <= 1:
             return arr
         mid = len(arr) // 2
         left = merge_sort(arr[:mid])
         right = merge_sort(arr[mid:])
         return merge(left, right)
     ```
     Merge sort divides the array into halves recursively, and then merges them back together, leading to a time complexity of \( O(n \log n) \).

6. **Exponential Time - O(2^n)**:
   - The running time grows exponentially with the size of the input. This typically occurs in algorithms that solve problems by brute force.
   - **Example**: Generating all subsets of a set (power set).
     ```python
     def generate_subsets(arr):
         subsets = []
         def backtrack(start, path):
             subsets.append(path)
             for i in range(start, len(arr)):
                 backtrack(i + 1, path + [arr[i]])
         backtrack(0, [])
         return subsets
     ```
     The number of subsets of a set with \( n \) elements is \( 2^n \), so this algorithm has a time complexity of \( O(2^n) \).

---

### How to Calculate Time Complexity

To calculate time complexity:

- Identify loops: The number of iterations an algorithm performs is a key factor. Each loop adds complexity.
- Look for recursive calls: For recursive algorithms, consider the depth of recursion and the work done at each level.
- Analyze nested operations: For nested loops, multiply the complexities of the loops.

### Example

Consider the following code:

```python
def example(arr):
    n = len(arr)
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            print(i, j)
    for k in range(n):  # O(n)
        print(k)
```

- The first part (nested loops) runs \( n \times n = n^2 \) times.
- The second part (single loop) runs \( n \) times.

Thus, the overall time complexity is \( O(n^2 + n) \), but we simplify this to **O(n²)** because, for large \( n \), the \( n^2 \) term dominates.

---

### Conclusion

Time complexity provides a high-level understanding of how an algorithm performs as the input size increases. By knowing the time complexity, you can make decisions about the efficiency and scalability of algorithms, especially when working with large data sets.
