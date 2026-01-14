/*
LeetCode: 33. Search in Rotated Sorted Array
Difficulty: Medium
Category: Arrays, Binary Search
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Approach:
- Modified Binary Search
- Identify which half is sorted
- Narrow search space accordingly

Time Complexity: O(log n)
Space Complexity: O(1)
*/

class Solution {
    public int search(int[] arr, int target) {
        int st = 0, end = arr.length - 1, mid;

        while (st <= end) {
            mid = (st + end) / 2;

            if (arr[mid] == target) {
                return mid;
            }
            // Left half is sorted
            else if (arr[mid] >= arr[st] && target >= arr[st]) {
                if (arr[mid] > target) {
                    end = mid - 1;
                } else {
                    st = mid + 1;
                }
            }
            else if (arr[mid] >= arr[st] && target < arr[st]) {
                st = mid + 1;
            }
            // Right half is sorted
            else if (arr[mid] < arr[st] && target >= arr[st]) {
                end = mid - 1;
            }
            else {
                if (arr[mid] > target) {
                    end = mid - 1;
                } else {
                    st = mid + 1;
                }
            }
        }
        return -1;
    }
}
