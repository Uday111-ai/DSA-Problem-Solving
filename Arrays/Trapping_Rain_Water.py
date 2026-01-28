"""
LeetCode: Trapping Rain Water (Hard)
Link: https://leetcode.com/problems/trapping-rain-water/
Approach: Two Pointer, DP
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def trap(self, h: list[int]) -> int:
        n = len(h)
        l = 0
        r = n-1
        left_Max  = 0
        right_Max = 0
        ans =0

        while(l<r):
            if(h[l]<h[r]):
                if(h[l] <left_Max):
                    ans += (left_Max - h[l])
                    l+=1
                
                else:
                    left_Max = h[l]
                    l+=1
            else:
                if(h[r]<right_Max):
                    ans += right_Max - h[r]
                    r-=1
                
                else:
                    right_Max = h[r]
                    r-=1

        return ans
