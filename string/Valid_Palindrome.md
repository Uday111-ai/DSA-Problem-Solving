# 🧩 LeetCode 125 – Valid Palindrome

Difficulty: Easy

Category: Two Pointers, String

Platform: LeetCode

# 🔗 Problem Link

https://leetcode.com/problems/valid-palindrome/

# 📝 Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

# 💡 Approach: Filter and Reverse

We traverse the string once, keeping only alphanumeric characters and converting them to lowercase.
Then, we check if the new string is fundamentally the same as its reverse.

# ⏱️ Complexity Analysis

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(n)** |

# 🧠 Key Interview Insight

While filtering creates a new string (O(n) space), a **Two Pointer** approach can also solve this in **O(1)** space by traversing from both ends and skipping non-alphanumeric characters.
