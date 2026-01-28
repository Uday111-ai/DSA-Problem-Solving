# 🧩 LeetCode 42 – Trapping Rain Water

**Difficulty:** Hard  
**Category:** Arrays, Two Pointers, Greedy  
**Platform:** LeetCode  

---

## 🔗 Problem Link
https://leetcode.com/problems/trapping-rain-water/

---

## 📝 Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much rainwater can be trapped after raining.

---

## 💡 Approach: Two Pointer (Optimized)

We use two pointers starting from both ends of the array.

- Maintain `leftMax` and `rightMax`
- Always move the pointer with smaller height
- Water trapped depends on the minimum boundary height


**Formula:** water = min(leftMax, rightMax) - height[i]


---

## ⏱️ Complexity Analysis

| Metric | Value |
|------|------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

---

## 🧠 Interview Insight

This approach avoids extra prefix and suffix arrays and calculates trapped water on the fly, reducing space complexity from **O(n)** to **O(1)**.
