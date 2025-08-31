# 📍 Day 1: Big-O Notation

## 1️⃣ Why Big-O?

Big-O is used to describe how fast an algorithm grows with input size **(n)**.  
It doesn’t measure actual execution time, only **how it scales**.

---

## 2️⃣ Common Complexities

| Complexity | Name         | Example                                |
|------------|-------------|----------------------------------------|
| **O(1)**   | Constant     | Accessing `arr[0]`, HashMap lookup     |
| **O(log n)** | Logarithmic | Binary Search                         |
| **O(n)**   | Linear       | Looping through an array               |
| **O(n log n)** | Linearithmic | MergeSort, QuickSort              |
| **O(n²)**  | Quadratic    | Nested loops (Bubble Sort)             |
| **O(2ⁿ)**  | Exponential  | Fibonacci (naive recursion)            |
| **O(n!)**  | Factorial    | Traveling Salesman brute force         |

---

## 3️⃣ Examples in Python

```python
O(1) – Constant
def get_first(arr):
    return arr[0]   # always takes same time

O(n) – Linear
def print_all(arr):
    for x in arr:
        print(x)

O(n²) – Quadratic
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

O(log n) – Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

4️⃣ Exercise for Today

Write these 3 functions in Python:

O(1) → Return the last element of an array.

O(n) → Find the maximum element in an array.

O(n²) → Print all pairs from an array.

5️⃣ Interview Tip

When interviewer asks: “What’s the complexity?” →
👉 Always answer with Big-O (worst case), unless they ask for best/average.

Day 1 Practice Problems
1️⃣ Two Sum (LeetCode #1)

Problem:
Given an array of integers nums and a target value, return indices of the two numbers that add up to the target.

Example:

nums = [2,7,11,15]
target = 9
# Output: [0,1]  because nums[0] + nums[1] = 9

📌 Complexity Thinking:

Brute force → try all pairs → O(n²)

Optimized → use HashMap to check complement → O(n)

2️⃣ Best Time to Buy and Sell Stock (LeetCode #121)

Problem:
You are given an array prices where prices[i] is the price of a stock on day i.
Find the max profit (buy one day, sell later).

Example:

prices = [7,1,5,3,6,4]
# Output: 5  (buy at 1, sell at 6)

📌 Complexity Thinking:

Brute force → check all pairs → O(n²)

Optimized → track min price + max profit in one pass → O(n)


---

Would you like me to also **add solutions in Python** for the 3 practice functions (`O(1), O(n), O(n²)`) and the **Two Sum & Stock Problem** so the GitHub file becomes a mini learning + coding notebook