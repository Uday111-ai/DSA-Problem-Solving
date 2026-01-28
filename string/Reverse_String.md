# 🧩 LeetCode 344 – Reverse String

**Difficulty:** Easy  
**Category:** Two Pointers, String  
**Platform:** LeetCode  

---

## 🔗 Problem Link
https://leetcode.com/problems/reverse-string/

---

## 📝 Problem Statement
Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array **in-place** with **O(1)** extra memory.

---

## 💡 Approach: Two Pointer

We use two pointers:
- `l` starting from the beginning
- `r` starting from the end

The characters at these pointers are swapped, and the pointers move inward until they meet.

---

# ⏱️ Complexity Analysis

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(1)** |


---

# 🧠 Key Interview Insight

This problem tests understanding of in-place array manipulation.
Using a temporary variable for swapping avoids extra memory usage and ensures constant space complexity.
