




**List - Basics**
A **list** in Python is a collection of items stored in a single variable. Lists are **ordered**, **changeable (mutable)**, and allow **duplicate** values.

Example:

```python
my_list = [1, 2, 3, "hello", 5.5]
print(my_list)  # Output: [1, 2, 3, 'hello', 5.5]
```

---

**Access Element from Multi-Dimensional List**
A **multi-dimensional list** is a list inside another list (nested list). We can access elements using multiple indices.

Example:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6 (row index 1, column index 2)
```

Example 2:
```python
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]

# Accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing an element from a Multi-Dimensional list")
print(List[0][1])  # Output: 'For'
print(List[1][0])  # Output: 'Geeks'
```

---

**Take Input in List**
We can take multiple inputs and store them in a list using `input().split()`.

Example 1:
```python
nums = list(map(int, input("Enter numbers: ").split()))
print(nums)
```
Input:
```
1 2 3 4 5
```
Output:
```
[1, 2, 3, 4, 5]
```

Example 2:
```python
string = input("Enter elements (Space-Separated): ")
# Split the strings and store them in a list
lst = string.split()
print('The list is:', lst)
```

---

**Built-in Functions (BIF) for Lists**

- **append()** - Adds an item at the end of the list.
  ```python
  lst = [1, 2]
  lst.append(3)
  print(lst)  # Output: [1, 2, 3]
  ```

- **insert()** - Inserts an item at a specific position.
  ```python
  lst.insert(1, "hello")
  print(lst)  # Output: [1, 'hello', 2, 3]
  ```

- **remove()** - Removes the first occurrence of a specified value.
  ```python
  lst.remove(2)
  print(lst)  # Output: [1, 'hello', 3]
  ```

- **reverse()** - Reverses the list.
  ```python
  lst.reverse()
  print(lst)  # Output: [3, 'hello', 1]
  ```

- **pop()** - Removes and returns the last item (or item at the given index).
  ```python
  lst.pop()
  print(lst)  # Output: [3, 'hello']
  ```

---

**List Slicing**
List slicing allows extracting parts of a list using `start:stop:step`.

Example:
```python
nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])  # Output: [20, 30, 40]
print(nums[:3])   # Output: [10, 20, 30]
print(nums[::2])  # Output: [10, 30, 50]
```

---

**List Comprehension**
List comprehension provides a **shorter** and more **readable** way to create lists.

Example:
```python
squares = [x*x for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```
Example with condition:
```python
even_nums = [x for x in range(10) if x % 2 == 0]
print(even_nums)  # Output: [0, 2, 4, 6, 8]
```

---
These are the basics of Python lists and their operations.

