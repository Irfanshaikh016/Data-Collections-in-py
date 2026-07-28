# 🐍 Python Built-in Data Collections

A beginner-friendly Python project demonstrating the four built-in data collection types:

- 📋 List
- 📦 Tuple
- 🎯 Set
- 📖 Dictionary

This repository contains explanations, examples, and common methods for each collection type.

---

## 📚 Table of Contents

- Introduction
- List
- Tuple
- Set
- Dictionary
- Comparison Table
- Requirements
- How to Run
- License

---

# Introduction

Python provides several built-in data structures for storing and organizing data efficiently.

The four most commonly used collections are:

| Collection | Description |
|------------|-------------|
| List | Ordered, mutable collection |
| Tuple | Ordered, immutable collection |
| Set | Unordered collection of unique elements |
| Dictionary | Key-value pair collection |

---

# List

A **List** is an ordered and mutable collection that allows duplicate values.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)

fruits.append("Orange")

print(fruits)
```

### Output

```
['Apple', 'Banana', 'Mango']
['Apple', 'Banana', 'Mango', 'Orange']
```

### Common Methods

- append()
- insert()
- extend()
- remove()
- pop()
- sort()
- reverse()
- clear()

---

# Tuple

A **Tuple** is an ordered and immutable collection.

```python
numbers = (10, 20, 30)

print(numbers)
print(numbers[1])
```

### Output

```
(10, 20, 30)
20
```

### Common Methods

- count()
- index()

---

# Set

A **Set** is an unordered collection of unique values.

```python
colors = {"Red", "Green", "Blue", "Red"}

print(colors)
```

### Output

```
{'Blue', 'Green', 'Red'}
```

### Common Methods

- add()
- update()
- remove()
- discard()
- pop()
- clear()

---

# Dictionary

A **Dictionary** stores data as key-value pairs.

```python
student = {
    "name": "Irfan",
    "age": 20,
    "course": "AI & ML"
}

print(student["name"])
```

### Output

```
Irfan
```

### Common Methods

- get()
- keys()
- values()
- items()
- update()
- pop()
- clear()

---

# Comparison Table

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| Ordered | ✅ | ✅ | ❌ | ✅ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicate Values | ✅ | ✅ | ❌ | Values ✅ |
| Unique Keys | ❌ | ❌ | ✅ | Keys ✅ |
| Indexing | ✅ | ✅ | ❌ | By Key |

---

# When to Use

## List

- Store ordered data
- Modify elements
- Allow duplicates

## Tuple

- Store fixed data
- Faster than lists
- Protect data from modification

## Set

- Remove duplicate values
- Fast membership testing
- Perform set operations

## Dictionary

- Store data as key-value pairs
- Fast lookups by key
- Represent structured objects

---

# Project Structure

```
python-builtin-collections/
│
├── README.md
├── list_example.py
├── tuple_example.py
├── set_example.py
├── dict_example.py
└── comparison.py
```

---

# Requirements

- Python 3.8+
- No external libraries required

---

# Run

Clone the repository:

```bash
git clone https://github.com/your-username/python-builtin-collections.git
```

Go to the project directory:

```bash
cd python-builtin-collections
```

Run any example:

```bash
python list_example.py
python tuple_example.py
python set_example.py
python dict_example.py
```

---

# Learning Outcomes

After completing this project, you will understand:

- Python built-in collections
- Creating and modifying collections
- Common methods
- Differences between collection types
- When to use each data structure

---

# License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
