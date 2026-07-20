# Python Dunder (Magic) Methods — Quick Reference

**Dunder** = **D**ouble **UNDER**score, e.g. `__init__`. These are special method names that
**Python already knows about**. You rarely call them yourself — Python calls them **automatically**
when a matching event happens (creating an object, printing it, adding two objects, etc.).

> Key idea: The double underscores are just a **naming convention**. A name is only "magic" if it is
> on Python's official list. Inventing your own like `__pm__` does nothing — Python never calls it.

---

## Summary table

| Dunder | Triggered by | Purpose | Must return |
|--------|--------------|---------|-------------|
| `__init__` | `Obj()` (creating an object) | Set up initial attributes (constructor) | `None` |
| `__new__` | `Obj()` (before `__init__`) | Actually creates the object (advanced) | the new object |
| `__del__` | object destroyed / garbage collected | Cleanup (close files, connections) | `None` |
| `__str__` | `print(obj)`, `str(obj)`, f-strings | Friendly, human-readable text | `str` |
| `__repr__` | `repr(obj)`, REPL echo, debugger | Unambiguous developer/debug text | `str` |
| `__len__` | `len(obj)` | Report a length/size | `int` |
| `__bool__` | `if obj:`, `bool(obj)` | Truthiness of the object | `bool` |
| `__eq__` | `obj == other` | Define equality | `bool` |
| `__ne__` | `obj != other` | Define inequality | `bool` |
| `__lt__` / `__le__` | `obj < other` / `obj <= other` | Less-than / less-or-equal (sorting) | `bool` |
| `__gt__` / `__ge__` | `obj > other` / `obj >= other` | Greater-than / greater-or-equal | `bool` |
| `__hash__` | `hash(obj)`, use as dict key / set item | Make object hashable | `int` |
| `__add__` | `obj + other` | Define `+` | any |
| `__sub__` | `obj - other` | Define `-` | any |
| `__mul__` | `obj * other` | Define `*` | any |
| `__truediv__` | `obj / other` | Define `/` | any |
| `__getitem__` | `obj[key]` | Read by index/key | any |
| `__setitem__` | `obj[key] = value` | Write by index/key | `None` |
| `__delitem__` | `del obj[key]` | Delete by index/key | `None` |
| `__contains__` | `x in obj` | Membership test | `bool` |
| `__iter__` | `for x in obj:` | Return an iterator (make it loopable) | iterator |
| `__next__` | each loop step | Return the next item / raise `StopIteration` | any |
| `__call__` | `obj()` (calling the object like a function) | Make an object callable | any |
| `__enter__` / `__exit__` | `with obj:` | Context manager setup / cleanup | varies |
| `__getattr__` | `obj.missing` (attribute not found) | Fallback for missing attributes | any |
| `__setattr__` | `obj.attr = value` | Intercept attribute assignment | `None` |

---

## The essentials (with examples)

### `__init__` — the constructor
Runs automatically when you create an object. Sets up starting attributes.

```python
class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

c = Computer("Dell", 90000)   # __init__ runs here automatically
```

### `__str__` — friendly text for humans
Runs on `print(obj)`, `str(obj)`, and f-strings. Must **return a string**.
Without it, printing shows an ugly default like `<__main__.Card object at 0x...>`.

```python
class Card:
    def __init__(self, number):
        self.__number = number          # private (hidden) full number

    def __str__(self):
        return "XXXX XXXX XXXX {}".format(self.__number[-4:])

print(Card("1234567890122134"))   # -> XXXX XXXX XXXX 2134
```

**Why not just a normal method like `display()`?**
Because `print()`, f-strings, `logging`, and other libraries are hard-wired to call `__str__`
**automatically**. A custom method only runs if you remember its exact name every time.

### `__repr__` — text for developers/debugging
Goal: unambiguous, ideally something you could paste back to recreate the object.
Used by the REPL, the debugger, and as a fallback when `__str__` is missing.

```python
class Card:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return "Card('{}')".format(self.number)

repr(Card("123"))   # -> "Card('123')"
```

> Rule of thumb: `__str__` = readable for users, `__repr__` = precise for developers.
> If you only write one, write `__repr__` (it also acts as the fallback for `__str__`).

### `__len__` — support `len(obj)`
```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

len(Playlist(["a", "b", "c"]))   # -> 3
```

### `__eq__` — define what "equal" means
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

Point(1, 2) == Point(1, 2)   # -> True
```

### `__add__` — define the `+` operator
```python
class Money:
    def __init__(self, rupees):
        self.rupees = rupees

    def __add__(self, other):
        return Money(self.rupees + other.rupees)

    def __str__(self):
        return "Rs {}".format(self.rupees)

print(Money(100) + Money(50))   # -> Rs 150
```

### `__getitem__` — support indexing `obj[key]`
```python
class Week:
    def __init__(self):
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __getitem__(self, i):
        return self.days[i]

Week()[0]   # -> "Mon"
```

### `__iter__` — make an object usable in a `for` loop
```python
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n          # yield makes this an iterator
            n -= 1

for x in Countdown(3):
    print(x)                 # -> 3, 2, 1
```

### `__call__` — make an object behave like a function
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
double(10)   # -> 20   (calling the object like a function)
```

### `__enter__` / `__exit__` — the `with` block (context manager)
```python
class Timer:
    def __enter__(self):
        print("start")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("stop")

with Timer():        # __enter__ runs, then body, then __exit__
    print("working")
# -> start / working / stop
```

---

## Rules that apply to ALL dunders

1. **Name must be exact.** Only names on Python's official list are magic (`__init__`, `__str__`, ...).
   Made-up names like `__pm__` are just ordinary methods — Python never calls them for you.
2. **Each has its own trigger.** `__init__` fires on creation, `__str__` on print, `__add__` on `+`.
   Using the right name at the wrong moment won't work.
3. **Each has a contract.** e.g. `__str__` / `__repr__` must return a **string**; `__len__` must return an **int**.
4. **You usually don't call them directly.** Prefer the built-in that triggers them:
   use `len(obj)` not `obj.__len__()`, `print(obj)` not `obj.__str__()`.

---

## Related: the OTHER double-underscore feature (not a dunder!)

A double underscore **prefix only** (like `__number`, not `__number__`) is a **different** feature
called **name mangling** — it makes an attribute "private" (hidden from outside the class).

```python
class Card:
    def __init__(self, number):
        self.__number = number     # private: outside code cannot read card.__number

    def __str__(self):
        return "XXXX XXXX XXXX {}".format(self.__number[-4:])
```

| Pattern | Name | Example | Meaning |
|---------|------|---------|---------|
| `__name__` (both sides) | dunder | `__init__`, `__str__` | Special hook Python calls automatically |
| `__name` (front only) | name mangling | `__number` | "Private" — hidden from outside the class |
