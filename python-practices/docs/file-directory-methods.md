# File & Directory Methods — Quick Notes

Summary of important Python methods for working with files and directories (`open`, `os`, `shutil`).

---

## 1. Opening files — `open()`

```python
file = open(path, mode='r', encoding='utf-8')
```

| Mode | Meaning | Notes |
| ---- | ------- | ----- |
| `'r'` | Read only | Default. File must exist |
| `'w'` | Write only | Creates file / **overwrites** existing |
| `'a'` | Append only | Writes at end. Creates if missing |
| `'x'` | Exclusive create | Fails if file already exists |
| `'r+'` | Read + write | File must exist |
| `'w+'` | Write + read | Overwrites / creates |
| `'a+'` | Append + read | Writes at end |
| `'b'` | Binary | Combine e.g. `'rb'`, `'wb'` |
| `'t'` | Text | Default. Combine e.g. `'rt'` |

**Path tip (Windows):** use raw string `r'C:\...'`, double slash `'C:\\...'`, or forward slash `'C:/...'` — a single `\` in a normal string is an escape (`\t` = tab).

**Preferred style:**

```python
with open(path, 'r', encoding='utf-8') as f:
    data = f.read()
# file auto-closes after the block
```

---

## 2. File object methods

| Method | What it does | Example |
| ------ | ------------ | ------- |
| `read()` | Read whole file as one string | `f.read()` |
| `read(n)` | Read next `n` characters | `f.read(10)` |
| `readline()` | Read one line | `f.readline()` |
| `readlines()` | Read all lines → list | `f.readlines()` |
| `write(s)` | Write a string | `f.write("hello")` |
| `writelines(list)` | Write a list of strings | `f.writelines(lines)` |
| `seek(pos)` | Move cursor to position | `f.seek(0)` → start |
| `tell()` | Current cursor position | `f.tell()` |
| `flush()` | Force write buffer to disk | `f.flush()` |
| `close()` | Close the file | `f.close()` |

**Cursor reminder:** after `write()`, the cursor is at the end. Call `seek(0)` before `read()` if the same handle is opened with `'w+'` / `'r+'`.

---

## 3. Directory methods — `os`

| Method | What it does | Notes |
| ------ | ------------ | ----- |
| `os.getcwd()` | Get current working directory | — |
| `os.chdir(path)` | Change working directory | — |
| `os.listdir(path)` | List files/folders in path | Returns list of names |
| `os.mkdir(path)` | Create **one** directory | Fails if parent missing |
| `os.makedirs(path)` | Create directory + parents | Like `mkdir -p` |
| `os.rename(src, dst)` | Rename / move file or dir | — |
| `os.remove(path)` | Delete a **file** | Not for directories |
| `os.rmdir(path)` | Delete an **empty** directory | Fails if not empty |
| `os.path.exists(path)` | Check if path exists | `True` / `False` |
| `os.path.isfile(path)` | Is it a file? | — |
| `os.path.isdir(path)` | Is it a directory? | — |
| `os.path.join(a, b)` | Join path parts safely | Prefer over string `+` |
| `os.path.basename(path)` | Last part of path | `'a/b/c.txt'` → `'c.txt'` |
| `os.path.dirname(path)` | Directory part of path | `'a/b/c.txt'` → `'a/b'` |

---

## 4. High-level copy / delete — `shutil`

| Method | What it does | Notes |
| ------ | ------------ | ----- |
| `shutil.copy(src, dst)` | Copy a file | Metadata may differ |
| `shutil.copy2(src, dst)` | Copy file + metadata | Prefer when keeping timestamps |
| `shutil.copytree(src, dst)` | Copy whole directory tree | — |
| `shutil.move(src, dst)` | Move file or directory | — |
| `shutil.rmtree(path)` | Delete directory **with contents** | Dangerous — no recycle bin |

```python
import shutil
shutil.rmtree(r'C:\path\to\folder')   # deletes folder + everything inside
```

---

## 5. Delete cheat sheet

| Goal | Method |
| ---- | ------ |
| Delete a file | `os.remove(path)` |
| Delete empty folder | `os.rmdir(path)` |
| Delete folder + contents | `shutil.rmtree(path)` |

---

## 6. Tiny examples

```python
import os
import shutil

# navigate
print(os.getcwd())
os.chdir(r'C:\Users\mohit\personal-mydata\git\python-practices\docs')
print(os.listdir('.'))

# create
os.mkdir('temp')
os.makedirs(r'temp\nested\deep')

# write + read
with open('temp.txt', 'w', encoding='utf-8') as f:
    f.write('hello\n')

with open('temp.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# rename / remove
os.rename('temp.txt', 'renamed.txt')
os.remove('renamed.txt')
shutil.rmtree('temp')
```

---

## 7. Related notes

- Encoding details → see `file-encoding.md`
- Prefer `with open(...)` so files always close, even on errors
- Prefer `os.path.join()` over hardcoding `\` or `/` when building paths
