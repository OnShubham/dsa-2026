--

## 1) Basic Idea of Hashing (Number → Index)

### Example: Simple Hash Function

Suppose we have a hash table of size **10**, and we use this hash function:

**Hash function:**
[
\text{index} = \text{key} \bmod 10
]

### Insert Numbers

Keys to insert: **23, 45, 12, 36**

| Key | Hash Calculation | Index |
| --- | ---------------- | ----- |
| 23  | 23 % 10          | 3     |
| 45  | 45 % 10          | 5     |
| 12  | 12 % 10          | 2     |
| 36  | 36 % 10          | 6     |

So the hash table looks like:

```
Index:  0 1 2 3 4 5 6 7 8 9
Value:  - -12 23 -45 36 - - -
```

**Key takeaway:**

* Hash function converts a key into an index
* This makes searching very fast: **O(1) average time**

---

## 2) Collision Example (Very Important)

A **collision** happens when two keys map to the same index.

### Example

Keys: **23** and **33**

```
23 % 10 = 3
33 % 10 = 3
```

Both go to index **3** → collision.

### Method: Chaining

We store multiple values in a list at the same index.

```
Index 3 → 23 → 33
```

Visual:

```
Index:  0 1 2 3        4 5 6 7 8 9
Value:  - - - [23,33]  - - - - - -
```

**This method is called:**

* **Separate Chaining**

---

## 3) Real-Life DSA Example — Count Frequency of Elements

Very common in exams and coding interviews.

### Problem

Count how many times each number appears.

**Input:**

```
arr = [1, 2, 2, 3, 1, 4]
```

### Using Hashing

We store counts in a hash map.

```
1 → 2
2 → 2
3 → 1
4 → 1
```

### Python Example

```python
arr = [1, 2, 2, 3, 1, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
```

Output:

```
{1: 2, 2: 2, 3: 1, 4: 1}
```

Time Complexity:

```
O(n)
```

---

## 4) Basic Hash Table Operations

### Insert

```
Insert(23)
index = 23 % 10 = 3
store at index 3
```

### Search

```
Search(23)
index = 23 % 10 = 3
check index 3
```

### Delete

```
Delete(23)
find index 3
remove value
```

---

## 5) Very Common Beginner DSA Problem — Check Duplicate

### Problem

Check if array contains duplicates.

**Input:**

```
[1, 2, 3, 4, 2]
```

### Solution Using Hashing

```python
arr = [1, 2, 3, 4, 2]

seen = set()

for num in arr:
    if num in seen:
        print("Duplicate found")
        break
    seen.add(num)
```

Time Complexity:

```
O(n)
```

---

## 6) Another Classic Example — Find First Non-Repeating Character

**Input:**

```
"swiss"
```

**Steps using hashing:**

```
s → 3
w → 1
i → 1
```

First non-repeating:

```
w
```

---

## Quick Exam Revision Notes 🧠

**Hashing is used for:**

* Searching
* Counting frequency
* Removing duplicates
* Fast lookup
* Dictionaries / Maps
* Sets

**Average Time Complexity:**

```
Insert  → O(1)
Search  → O(1)
Delete  → O(1)
```

**Collision Handling Methods:**

1. Chaining
2. Linear Probing
3. Quadratic Probing
4. Double Hashing

---

If you'd like, I can next provide:

* **Hashing programs in C / C++ / Java**
* **Practice problems for exams or interviews**
* **Visual step-by-step collision examples**
