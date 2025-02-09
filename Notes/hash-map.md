**Question  :** Given a list of integers with duplicate elements, generate another list that contains only the duplicate elements. The new list should contain only the elements that appear more than once in the first list.

Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]


Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]

---
# **1. What is a HashMap?**
A **HashMap (or dictionary in Python)** is a **key-value store** that allows you to store and retrieve values efficiently.

- In Python, **dictionaries (`dict`) are implemented as HashMaps**.
- A HashMap uses a **hash function** to determine where a key should be stored in memory.

---

# **2. How Searching Works in a HashMap**
### **(a) In a Normal List (Brute Force)**
- If you want to find if `20` exists in `[10, 20, 30, 40]`, you have to **scan the entire list**.
- Worst-case scenario: If `20` is at the end, you take **O(n) time**.

### **(b) In a HashMap**
- Instead of searching through an entire list, a HashMap **directly jumps to the location** where the value is stored using a **hash function**.

#### **Step-by-Step Process**
1. **Hash Function Converts a Key to an Index**
   - Example: If our input is `[10, 20, 30, 40]`, we insert each number into a HashMap.
   - A **hash function** converts each number into a **memory index**.

2. **Direct Access Using the Index**
   - When you check if `20` exists, the HashMap directly goes to the **memory location** where `20` was stored, instead of searching the whole list.
   - This takes **O(1) time** instead of **O(n)**.

---

# **3. Why Is HashMap Lookup O(1) on Average?**
The key idea is **how hash functions distribute elements efficiently** in memory.

## **(a) Hash Function Converts a Key to an Index**
Let’s say we have this input list:
```plaintext
[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
```
When we insert elements into a HashMap, the **hash function maps each number to a unique memory slot**.

Example:
```plaintext
Key: 10  → Hash: 2  → Stored at index 2
Key: 20  → Hash: 5  → Stored at index 5
Key: 30  → Hash: 7  → Stored at index 7
Key: -20 → Hash: 3  → Stored at index 3
```
- The **hash function determines the location in constant time O(1)**.

## **(b) Lookup Uses the Same Hash Function**
Now, if we check whether `20` exists:
1. Compute the **hash of 20** → **Jump directly to index 5**.
2. Check if `20` is present → **Found in O(1) time**.

This avoids scanning the entire list.

---

# **4. Why is the Overall Approach O(n)?**
When solving our problem using a HashMap:
1. **Building the HashMap (O(n)):**
   - We go through each element **once**, inserting it into the HashMap → **O(n)**.
2. **Extracting Duplicates (O(n)):**
   - We go through the HashMap once to collect elements appearing more than once → **O(n)**.

So, the total time complexity is:
\[
O(n) + O(n) = O(n)
\]
which is much better than **O(n²)** in brute force.

---

# **5. What About Collisions?**
- Sometimes, multiple values **hash to the same index**. This is called a **collision**.
- Python handles this by using **linked lists (chaining)** or **open addressing**.
- Even with collisions, searching takes **O(1) on average**, but **O(n) in the worst case** if all keys end up in one bucket (which is rare).

---

# **6. Summary: Why is HashMap Faster?**
| Approach | Lookup Time per Element | Overall Complexity |
|----------|-------------------------|---------------------|
| **Brute Force (Nested Loops)** | O(n) | O(n²) |
| **HashMap (Dictionary)** | O(1) on average | O(n) |

- HashMap **avoids scanning the list multiple times**.
- Instead of **searching through n elements**, it **jumps directly** to the correct index.
- **On average, a HashMap lookup is O(1), making the whole approach O(n).**

---

# **7. Real-World Analogy**
### **Brute Force (O(n²)): Searching in a Notebook**
- Imagine you have a **notebook with 1,000 names**.
- To find if "Prashant" appears more than once, you **reread every name for each search**.
- This takes **a lot of time**.

### **HashMap (O(n)): Using an Index**
- Imagine you have a **dictionary** where each name has a **preassigned page number**.
- To find "Prashant", you **jump directly to its page**.
- This takes **O(1) time** instead of reading the whole book.

---

# **Final Answer: Why Is HashMap Faster?**
✅ **It avoids repeated scanning by using direct access via hashing.**  
✅ **Lookups are O(1) on average, so the overall approach is O(n).**  
✅ **Brute force requires scanning for each element, making it O(n²) and much slower.**  

---

Let me know if this makes sense! 🚀