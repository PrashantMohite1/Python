"""
 Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.

Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.

Note: If there is no intersection then return an empty array.

Examples:

Input: arr1[] = [1, 2, 3, 4], arr2[] = [2, 4, 6, 7, 8]
Output: [2, 4]
Explanation: 2 and 4 are only common elements in both the arrays.

Input: arr1[] = [1, 2, 2, 3, 4], arr2[] = [2, 2, 4, 6, 7, 8]
Output: [2, 4]
Explanation: 2 and 4 are the only common elements.

Input: arr1[] = [1, 2], arr2[] = [3, 4]
Output: []
Explanation: No common elements.

"""
---

### **Understanding the Problem Statement**  
We are given two **sorted** arrays, and we need to find the **intersection** of these arrays. The intersection means the elements that appear in **both** arrays **without duplicates**. If no such element exists, we return an empty array.





## **Approach 1: Brute Force Approach**
### **Idea**
- Take each element from the first array.
- Check if it is present in the second array.
- Store the common elements in a result array.
- Ensure we do not store duplicates.


### **Time Complexity**
- Checking each element in `arr2` takes **O(N)** time.  
- Since we do this for every element in `arr1`, the total time complexity is **O(M * N)**, where **M** is the size of `arr1` and **N** is the size of `arr2`.  

🔴 **This is not optimal because it takes too much time.**  

---

## **Approach 2: Using a HashSet**
### **Idea**
- Store all elements of `arr1` in a **set** (which allows fast lookup).
- Iterate through `arr2` and check if the element exists in the set.
- Store the common elements in a result set to avoid duplicates.

### **Understanding Hashing: How Does Python Store Sets?**

A **hash function** takes an input (like a number or string) and generates a **fixed-size value** (called a hash). This hash determines where the element will be stored in memory.

### **Example:**
Let’s take a simple hash function (not the real one used by Python) to understand:

#### **Assume this hash function:**  
\[
\text{hash}(x) = x \mod 10
\]
This means that any number `x` will be placed in **index (x % 10) of an array**.

Now, let’s insert elements into a **set**:
```plaintext
hash_set = {12, 25, 36, 40}
```
Applying our hash function:
- `hash(12) = 12 % 10 = 2` → Store `12` at **index 2**.
- `hash(25) = 25 % 10 = 5` → Store `25` at **index 5**.
- `hash(36) = 36 % 10 = 6` → Store `36` at **index 6**.
- `hash(40) = 40 % 10 = 0` → Store `40` at **index 0**.

**Final memory layout (hash table representation):**
```
Index:  0   1   2   3   4   5   6   7   8   9  
Value: 40  --  12  --  --  25  36  --  --  --
```
✅ The elements are stored **at fixed positions** based on their hash values.


### **Time Complexity**
- Converting `arr1` into a set: **O(M)**
- Checking each element of `arr2`: **O(N)**
- Overall complexity: **O(M + N)**

🟢 **This is much faster than the brute-force approach.**

---

## **Approach 3: Two Pointer Technique (Best Approach)**
### **Idea**
Since both arrays are **sorted**, we can take advantage of this and use the **two-pointer technique**:
- Start with two pointers, one for `arr1` and one for `arr2`.
- Compare the elements at both pointers:
  - If they are **equal**, add to the result and move both pointers forward.
  - If `arr1[i] < arr2[j]`, move the pointer in `arr1` forward.
  - If `arr1[i] > arr2[j]`, move the pointer in `arr2` forward.
- This ensures that each array is **traversed only once**.

### **Step-by-step Explanation**
#### Example:  
**arr1 = [1, 2, 3, 4]**, **arr2 = [2, 4, 6, 7, 8]**  

1. **Start with two pointers:**  
   - `i = 0` (points to `1` in `arr1`)  
   - `j = 0` (points to `2` in `arr2`)  

2. **Compare `arr1[i]` and `arr2[j]`:**  
   - `1 < 2` → Move `i` to `1`.  

3. **Compare `arr1[i]` and `arr2[j]`:**  
   - `2 == 2` → Add `2` to result, move both `i` and `j` forward.  

4. **Compare `arr1[i]` and `arr2[j]`:**  
   - `3 < 4` → Move `i` to `3`.  

5. **Compare `arr1[i]` and `arr2[j]`:**  
   - `4 == 4` → Add `4` to result, move both `i` and `j` forward.  

6. **Now `i = 4` (out of bounds), so stop.**  

### **Step-by-Step Execution**
We compare `arr1[i]` and `arr2[j]` and move the pointer accordingly.

| Step | i (arr1) | j (arr2) | arr1[i] | arr2[j] | Comparison | Action |
|------|---------|---------|---------|---------|------------|---------|
| 1    | 0       | 0       | **1**   | **2**   | 1 < 2      | Move `i` to 1 |
| 2    | 1       | 0       | **2**   | **2**   | 2 == 2     | Add `2` to result, move both `i` and `j` forward |
| 3    | 2       | 1       | **3**   | **4**   | 3 < 4      | Move `i` to 3 |
| 4    | 3       | 1       | **4**   | **4**   | 4 == 4     | Add `4` to result, move both `i` and `j` forward |
| 5    | 4       | 2       | Out of bounds | 6 | - | Stop |

### **Final Result: `[2, 4]`**

### **Time Complexity**
- We only traverse both arrays **once**, so the time complexity is **O(M + N)**.  
- **No extra space is required**, making this the most **optimized approach**.

---

## **Final Conclusion**
| Approach | Time Complexity | Space Complexity | Notes |
|----------|---------------|-----------------|-------|
| Brute Force | O(M * N) | O(1) | Very slow |
| HashSet | O(M + N) | O(M) | Faster but needs extra space |
| Two Pointers | O(M + N) | O(1) | **Best approach** |

✅ **The Two Pointer approach is the most optimized solution because it runs in O(M + N) time and does not use extra space.**  

Would you like me to explain another example in this approach? 😊
---



