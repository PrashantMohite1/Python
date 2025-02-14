


### heterogeneous and homegeneouse

In programming, "heterogeneous" refers to a data structure or collection where elements are of different data types, meaning you can store various kinds of values like integers, strings, booleans, or even objects from different classes within the same collection, unlike a "homogeneous" collection which would only contain elements of the same type



## **Ordered and Unordered Collection**:

In **ordered collections**, the **order of elements is preserved**. This means that the order in which you insert the items is the order in which you'll access them.

#### **Example 1: Ordered List**
```python
my_list = [10, 20, 30]
print(my_list[0])  # Output: 10
print(my_list[1])  # Output: 20
print(my_list[2])  # Output: 30
```
- In a **list**, the order is preserved. The first element added (`10`) is at index 0, the second element (`20`) is at index 1, and so on. If you access them by their index, you get them in the same order.

#### **Example 2: Ordered Dictionary (Python 3.7+)**
```python
my_dict = {"name": "Alice", "age": 25, "city": "Pune"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Pune'}
```
- In a **dictionary** (from Python 3.7+), the order of the key-value pairs is maintained. You get the same sequence of keys and values as when you inserted them.

---

#### **Unordered Collection**:

In **unordered collections**, the **order of elements is not preserved**. The order in which items are inserted is not guaranteed when you access them.

#### **Example 1: Unordered Set**
```python
my_set = {10, 20, 30}
print(my_set)  # Output: {10, 20, 30} (but could be in any order)
```
- **Sets** do not guarantee any specific order. Even if you add `10, 20, 30`, when you print the set, the order might be different (like `{30, 10, 20}`), and you cannot rely on the order.

#### **Example 2: Unordered Dictionary (Before Python 3.7)**
```python
my_dict = {"name": "Alice", "age": 25, "city": "Pune"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Pune'} (Order not guaranteed)
```
- In **older versions of Python (before 3.7)**, **dictionaries were unordered**, meaning even though you inserted the items in a certain order, the dictionary might return them in a different order when printed.  



## data structures in python 


1. **List** – An ordered, changeable (mutable) collection that allows duplicate values.  
   **Syntax:** `my_list = [1, 2, 3, 4]`


   - Why List is mutable 

    Lists use contiguous memory – A list is stored in a continuous block of memory, but it holds references (pointers) to actual values stored elsewhere.

    Modifying an element – When we change a value at an index, Python only updates the reference to point to a new memory location. The list structure remains unchanged.

    Adding elements:

    If extra space exists, Python adds the reference to the next empty slot.
    If no space is left, Python allocates a bigger block, copies elements, and appends the new value.
    Removing elements – Python removes the reference and shifts elements left to maintain contiguous memory. The old value remains in memory until garbage collection





2. **Set** – An unordered collection of unique values (no duplicates allowed).  
   **Syntax:** `my_set = {1, 2, 3, 4}`

   - specific reason why a set is mutable lies in how it is implemented in Python:

    Sets are implemented as hash tables (or similar data structures) under the hood. This allows for dynamic memory allocation, which means the set can grow and shrink in size as elements are added or removed.

    In contrast to tuples, which have a fixed size due to their immutability, sets can adjust their size because they are designed to store a dynamic collection of unique items. because of this dynamic memory allocation set is mutable.

    #### IMP Built in methods of set

    -  union(): Used to find union() between two sets. It performs this using '|' operator.

    -   intersection(): Used to find intersection() between two sets. It performs this using '&' operator.

    -   difference(): Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly for B - A holds the same.


3. **Tuple** – An ordered, unchangeable (immutable) collection that allows duplicates.  
   **Syntax:** `my_tuple = (1, 2, 3, 4)`

   - A tuple is immutable because once it is created, its memory structure is fixed, and its elements cannot be changed, added, or removed. This is due to how Python stores tuples in memory.

        **How Tuples Are Stored in Memory**
        Unlike lists, tuples do not store references that can be changed.
        
        Instead, a tuple directly stores the memory addresses of its elements in a fixed block.
        Python allocates a fixed amount of memory for a tuple at creation, making modifications impossible.



4. **Dictionary (map in other programming)**

    A dictionary in Python is an unordered, mutable collection of key-value pairs. It allows you to store and retrieve data in an effic ient way. Dictionaries are often used when you need to associate a value with a unique key and want fast lookups, additions, and deletions. in other programming languages we have map data structure which is like dict in python.

    Note - Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly. 

    Values in a dictionary can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable. 

    Addition of elements can be done in multiple ways. One value at a time can be added to a Dictionary by defining value along with the key e.g. Dict[Key] = 'Value'. Updating an existing value in a Dictionary can be done by using the built-in update() method. Nested key values can also be added to an existing Dictionary. 


    A dictionary in Python works like a "hash map" where each key is mapped to a value. Python uses a process called hashing to generate a "hash value" for each key to locate the value associated with that key efficiently. If a key were mutable (like a list), its hash value could change, which would mess up the lookup process. That's why immutable objects (like numbers, strings, and tuples) are used as dictionary keys.


    ### Understanding Dictionary Data Structure in Python (Based on Memory & Mutability Aspects)

    A **dictionary (`dict`) in Python is mutable** and is implemented using a **hash table**. It allows fast access, insertion, and deletion of key-value pairs. Let’s break it down based on the aspects we discussed earlier:  

    ---

    #### **1. How Dictionaries Are Stored in Memory?**  

    - A dictionary in Python is **not stored in a contiguous memory block like lists**.  
    - Instead, it uses a **hash table**, which means elements are **spread across memory** based on their hash values.  
    - Each **key-value pair is stored in a separate memory location** with a reference maintained in the dictionary.  

    📌 **Example:**  
    ```python
    my_dict = {"name": "Alice", "age": 25, "city": "Pune"}
    ```
    🔹 **Internal Representation in Memory:**  

    | Hash Key | Memory Address (Dictionary Slot) | Key Reference | Value Reference |
    |----------|-------------------------------|--------------|----------------|
    | `hash("name")` | 1000 | → "name" (2000) | → "Alice" (3000) |
    | `hash("age")` | 1004 | → "age" (2004) | → 25 (3004) |
    | `hash("city")` | 1008 | → "city" (2008) | → "Pune" (3008) |

    - **Keys are hashed** using a hashing function, which helps in **quick lookup**.  
    - Each key points to a **memory address where its corresponding value is stored**.  

    ---

    #### **2. Why Are Dictionaries Mutable?**  

    ✔ **Reason 1: Direct Reference Updates**  
    - Since dictionaries store references to values, modifying a value **only updates the reference, not the structure itself**.  
    - Example:  
        ```python
        my_dict["age"] = 30  # Changing value
        ```
        - **Only the reference to `25` is updated to `30`**, keeping the dictionary intact.  

    ✔ **Reason 2: Hash Table Allows Dynamic Resizing**  
    - If a new key-value pair is added, Python **finds an empty slot** in memory (or resizes the table if full).  
    - Example:  
        ```python
        my_dict["country"] = "India"
        ```
        - Python computes `hash("country")`, finds an empty memory slot, and **stores the new key-value pair dynamically**.  

    ✔ **Reason 3: Deletion Works by Marking Slots as Empty**  
    - Removing an entry (`del my_dict["age"]`) **does not shift elements like lists**. Instead, it **marks the slot as empty**, which can be reused later.  
