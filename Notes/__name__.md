

## **What is `__name__`?**

- The `__name__` variable is a special built-in variable in Python.
- It holds the **name of the current module** that is being executed or imported.

---

### **Scenario 1: When the script is **run directly****

- **`__name__` is set to `'__main__'`** when the Python script is executed directly.
- This allows us to control the flow of the program using `if __name__ == '__main__':`.

#### Example: **Running the script directly**

**File: `script1.py`**

```python
# script1.py

print("Value of __name__ in script1.py:", __name__)

def function_in_script1():
    print("This is a function in script1.")

if __name__ == '__main__':
    print("This code runs when script1 is executed directly.")
    function_in_script1()
```

- **Explanation**:
  - When you run `python script1.py`, Python sets `__name__` to `'__main__'`.
  - This causes the `if __name__ == '__main__':` block to execute, printing the message and calling `function_in_script1()`.

- **Output (when you run `python script1.py` directly):**

```bash
Value of __name__ in script1.py: __main__
This code runs when script1 is executed directly.
This is a function in script1.
```

---

### **Scenario 2: When the script is **imported as a module** into another script**

- **`__name__` is set to the **module's name** (the name of the file without the `.py` extension)** when the Python file is imported as a module into another script.

#### Example: **Importing the script as a module**

**File: `script1.py`**

```python
# script1.py

print("Value of __name__ in script1.py:", __name__)

def function_in_script1():
    print("This is a function in script1.")
```

**File: `script2.py`**

```python
# script2.py

import script1  # Import script1 into script2

print("Value of __name__ in script2.py:", __name__)

# Calling the function from script1
script1.function_in_script1()
```

- **Explanation**:
  - When `script2.py` is run and imports `script1`, Python sets `__name__` in `script1.py` to `'script1'` (the name of the module).
  - The code inside the `if __name__ == '__main__':` block in `script1.py` is **not executed** because `__name__` is not equal to `'__main__'`.
  - In `script2.py`, the value of `__name__` is `'__main__'` since it's the script being executed.

- **Output (when you run `python script2.py`):**

```bash
Value of __name__ in script2.py: __main__
Value of __name__ in script1.py: script1
This is a function in script1.
```

---

### **Key Takeaways:**

1. **When running a script directly:**
   - `__name__` is set to `'__main__'` in the file that is executed.
   - You can use `if __name__ == '__main__':` to place code that should only run when the file is executed directly.

2. **When importing a script as a module:**
   - `__name__` is set to the **name of the module** (i.e., the file name without `.py` extension).
   - Code inside `if __name__ == '__main__':` will **not run** because `__name__` will be the name of the module (not `'__main__'`).

---

### **Full Example in Action:**

#### **File: `script1.py`**

```python
# script1.py

print("Value of __name__ in script1.py:", __name__)

def function_in_script1():
    print("This is a function in script1.")

if __name__ == '__main__':
    print("This code runs when script1 is executed directly.")
    function_in_script1()
```

#### **File: `script2.py`**

```python
# script2.py

import script1  # Import script1 into script2

print("Value of __name__ in script2.py:", __name__)

# Calling the function from script1
script1.function_in_script1()
```

---

### **Results:**

1. **Running `python script1.py` directly:**
   ```
   Value of __name__ in script1.py: __main__
   This code runs when script1 is executed directly.
   This is a function in script1.
   ```

2. **Running `python script2.py` (importing `script1`):**
   ```
   Value of __name__ in script2.py: __main__
   Value of __name__ in script1.py: script1
   This is a function in script1.
   ```

---

### **Summary:**

- **`__name__`** is a built-in variable in Python that tells you if a script is being run directly or imported as a module.
- **When the script is run directly**, `__name__` is set to `'__main__'`.
- **When the script is imported**, `__name__` is set to the **name of the module** (e.g., `'script1'`).
- Use `if __name__ == '__main__':` to control code that should only run when the script is executed directly.

---

I hope this summary helps you with your notes! Let me know if you need any further clarification or examples. 😊
