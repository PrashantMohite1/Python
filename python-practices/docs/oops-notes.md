# Python OOP — Short Notes

**OOP (Object-Oriented Programming)** = a way to structure code around **objects** (real-world
entities) instead of just functions. It bundles **data** + **behavior** together.

> Key idea: model your program as interacting objects, each with its own data (attributes) and
> actions (methods).

---

## Core building blocks


| Term           | One-liner                                                                                | Example                          |
| -------------- | ---------------------------------------------------------------------------------------- | -------------------------------- |
| **Class**      | A blueprint/template for creating objects                                                | `class Dog:`                     |
| **Object**     | A real instance made from a class (has its own data)                                     | `d = Dog()`                      |
| **Attribute**  | Data stored on an object                                                                 | `self.name`                      |
| **Method**     | A function defined inside a class                                                        | `def bark(self):`                |
| `**self**`     | Reference to the current object inside a method                                          | `self.name = name`               |
| `**__init__**` | Constructor — runs automatically when object is created                                  | `def __init__(self):`            |
| **ABC**        | Abstract Base Class — a blueprint you can't instantiate; can mix abstract + real methods | `class Shape(ABC):`              |
| **Interface**  | A pure contract — only method names, no implementation (a class promises to have these)  | ABC with only `@abstractmethod`s |


```python
class Dog:                     # class = blueprint
    def __init__(self, name):  # constructor
        self.name = name       # attribute

    def bark(self):            # method
        print(f"{self.name}: Woof!")

d = Dog("Tommy")   # object (instance)
d.bark()           # Tommy: Woof!
```

---

## The 4 pillars of OOP

### 1. Encapsulation

**Bundle data + methods in a class, and hide internal state.** Access private data only through
controlled methods (getters/setters).

- `name` → public
- `_name` → protected (convention, "internal use")
- `__name` → private (name-mangled to `_Class__name`)

```python
class Account:
    def __init__(self):
        self.__balance = 0          # private

    def deposit(self, amt):         # controlled access + validation
        if amt > 0:
            self.__balance += amt
```

### 2. Inheritance

**Create a new class from an existing one** to reuse its code. Child (derived) gets parent's
(base) attributes & methods.

```python
class Animal:              # base / parent
    def eat(self): print("eating")

class Dog(Animal):         # derived / child
    def bark(self): print("Woof")

Dog().eat()   # inherited from Animal
```

- Use `super()` to call the parent's version.
- Python supports **multiple inheritance**: `class C(A, B):`.

### 3. Polymorphism

**Same interface, different behavior** depending on the object ("many forms").

```python
class Dog:
    def sound(self): print("Woof")
class Cat:
    def sound(self): print("Meow")

for a in [Dog(), Cat()]:
    a.sound()   # same call, different result
```

Forms in Python: **duck typing**, **method overriding**, **operator overloading** (via dunders like
`__add__`), and built-ins like `len()`.

### 4. Abstraction

**Hide complex details, expose only the essentials.** Define *what* must be done, not *how*. Done
via abstract base classes (`abc` module).

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...      # must be implemented by subclasses

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2

# Shape()  -> ERROR: can't instantiate abstract class
Circle(5).area()            # 78.5
```

---

## Encapsulation vs Abstraction

Both involve "hiding" — but they hide **different things** for **different reasons**.


|                     | **Encapsulation**                        | **Abstraction**                            |
| ------------------- | ---------------------------------------- | ------------------------------------------ |
| What it hides       | **Data / internal state**                | **Implementation / complexity**            |
| How                 | `__private` vars, getters/setters        | abstract classes & methods (`abc`)         |
| Question it answers | *"Who can change this data?"*            | *"What can it do (without showing how)?"*  |
| Level               | Object-level (protect one object's data) | Design-level (define a blueprint/contract) |
| Slogan              | *Hide the data, expose safe methods*     | *Show what it does, hide how it does it*   |


```python
class Account(ABC):
    def __init__(self):
        self.__balance = 0      # ENCAPSULATION: data hidden/protected

    def deposit(self, amt):     # ENCAPSULATION: controlled, validated access
        if amt > 0:
            self.__balance += amt

    @abstractmethod
    def interest(self):         # ABSTRACTION: WHAT must exist, not HOW
        pass
```

**Car analogy:** the sealed engine you can't poke at = *encapsulation* (protects data);
the steering wheel + pedals you're given to drive = *abstraction* (simple interface over
complex internals).

---

## Method types


| Type                | First param | Decorator       | Works on   | Use for                                     |
| ------------------- | ----------- | --------------- | ---------- | ------------------------------------------- |
| **Instance method** | `self`      | none            | the object | normal behavior using instance data         |
| **Class method**    | `cls`       | `@classmethod`  | the class  | alternate constructors, class-level data    |
| **Static method**   | none        | `@staticmethod` | nothing    | utility/helper functions grouped in a class |


```python
class Circle:
    pi = 3.14                       # class attribute

    def __init__(self, r):
        self.r = r                  # instance attribute

    def area(self):                 # instance method
        return Circle.pi * self.r ** 2

    @classmethod
    def unit(cls):                  # class method (alt constructor)
        return cls(1)

    @staticmethod
    def info():                     # static method
        return "A circle is round"
```

---

## Quick glossary

- **Instance attribute** — unique per object (`self.x`).
- **Class attribute** — shared across all objects (defined directly in the class body).
- **Method overriding** — child redefines a parent method.
- **Name mangling** — `__x` becomes `_ClassName__x` to discourage outside access.
- **Dunder methods** — special `__x__` methods Python calls automatically (see `dunder-methods.md`).

---

## One-line summary of the pillars


| Pillar        | Slogan                                    |
| ------------- | ----------------------------------------- |
| Encapsulation | *Hide the data, expose safe methods.*     |
| Inheritance   | *Reuse code from a parent class.*         |
| Polymorphism  | *One interface, many behaviors.*          |
| Abstraction   | *Show what it does, hide how it does it.* |


