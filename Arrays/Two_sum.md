# 🧩 LeetCode 1 – Two Sum

Difficulty: Easy

Category: Arrays, Hashing

Platform: LeetCode

# 🔗 Problem Link

https://leetcode.com/problems/two-sum/

# 📝 Problem Statement

Given an array of integers **nums** and an integer **target**, return indices of the two numbers such that they add up to the given target.
Each input has exactly one solution, and the same element cannot be used twice.

# 💡 Approach: Hash Map

We traverse the array once while storing each element’s index in a hash map.
For each element, we check if target - current_element already exists in the map.
If it does, we return the stored index along with the current index.

# ⏱️ Complexity Analysis

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(n)** |

# 🧠 Key Interview Insight

Using a hash map allows us to reduce the problem from **O(n²)** to **O(n)** by trading space for time — a common interview optimization technique.
