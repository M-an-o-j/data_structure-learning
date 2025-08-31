# 📘 Arrays – Notes

## 1. What is an Array?
- An **array** is a collection of elements stored in **contiguous memory locations**.
- Elements are usually of the **same data type** (e.g., integers, strings).
- Each element is accessed using an **index** (starting from `0` in most languages like Python, C, Java).

---

## 2. Array Representation
- Example in Python:
  ```python
  arr = [10, 20, 30, 40]

Here:

arr[0] = 10

arr[1] = 20

arr[2] = 30

arr[3] = 40

3. Key Properties

Fixed size (in low-level languages like C)

You must define size at creation.

Dynamic size (in Python, Java, JS, etc.)

Arrays can grow or shrink (called Lists in Python).

Random Access

Any element can be accessed in O(1) using its index.

Sequential Memory

Elements are stored next to each other in memory.

4. Basic Operations

Traversal: Visiting each element one by one (O(n)).

Insertion:

At end: O(1) (amortized in Python).

At middle: O(n) (shifts required).

Deletion:

From end: O(1).

From middle: O(n) (shifts required).

Search:

Linear Search: O(n).

Binary Search (only on sorted arrays): O(log n).

5. Advantages

Fast random access (O(1)).

Easy to implement.

Contiguous memory improves cache locality (better performance).

6. Disadvantages

Fixed size in some languages (C/C++).

Insertion/Deletion in the middle is costly (O(n)).

Wasted memory if size is overestimated.

Need resizing if array grows beyond capacity (dynamic arrays).

7. Real-world Examples

Storing marks of students.

Image pixels in a 2D array.

Handling data streams (queues, stacks use arrays under the hood).