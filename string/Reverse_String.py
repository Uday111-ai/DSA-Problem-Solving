"""
LeetCode: Reverse String (Easy)
Link: https://leetcode.com/problems/reverse-string/
Approach: Two Pointer
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1
        while l<r:
            temp=s[l]
            s[l]=s[r]
            s[r]=temp
            l+=1
            r-=1
        
