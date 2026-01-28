# 🧩 LeetCode 125 – Valid Palindrome

Difficulty: Easy

Category: Two Pointers, String

Platform: LeetCode

# 🔗 Problem Link

https://leetcode.com/problems/valid-palindrome/

# 📝 Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

# 💡 Approach: Two Pointer

We use two pointers starting from both ends of the string. Non-alphanumeric characters are skipped, and the remaining characters are compared in lowercase. If all corresponding characters match while moving inward, the string is a valid palindrome.

# ⏱️ Complexity Analysis

| Metric           | Value    |
| ---------------- | -------- |
| Time Complexity  | **O(n)** |
| Space Complexity | **O(1)** |

# 🧠 Key Interview Insight

Although filtering and reversing the string is straightforward, it requires **O(n)** extra space. The **Two Pointer** approach is more optimal, as it compares characters in-place from both ends while skipping non-alphanumeric characters, achieving **O(1)** space complexity.
