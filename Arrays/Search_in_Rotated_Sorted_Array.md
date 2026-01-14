# LeetCode 33 – Search in Rotated Sorted Array

**Difficulty:** Medium  
**Category:** Arrays, Binary Search  

---

## 🔍 Problem Statement
Given a rotated sorted array of distinct integers and a target value, return the index of the target if it exists. Otherwise, return `-1`.

The algorithm must run in **O(log n)** time.

---

## 💡 Key Idea
Even though the array is rotated, **at least one half is always sorted**.

Using this property, we apply **modified binary search**:
- Identify the sorted half
- Check if the target lies within that half
- Narrow the search range accordingly

---

## 🧠 Approach (Modified Binary Search)

1. Initialize two pointers: `start` and `end`
2. Calculate `mid`
3. If `arr[mid] == target`, return `mid`
4. Determine which half is sorted:
   - Left half sorted OR right half sorted
5. Decide whether to move left or right based on target position
6. Repeat until found or range is exhausted

---

## ⏱️ Complexity Analysis

| Metric | Complexity |
|------|------------|
| Time Complexity | **O(log n)** |
| Space Complexity | **O(1)** |

---


