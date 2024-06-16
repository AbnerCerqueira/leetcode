# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [3], nums2 = [-2,-1]
# Output: -1.00000
# Explanation: merged array = [-2,-1, 3] and median is -1.

# Example 2:
# Input: nums1 = [1,2], nums2 = [2,7]
# Output: 2.50000
# Explanation: merged array = [1,2,3,7] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l = []
        l += nums1 + nums2
        l.sort()
        m = int(len(l) // 2) # m significa meio
        return l[m] if len(l) % 2 == 1 else (l[m - 1] + l[m]) / 2

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays([1, 3], [2, 7]))
    print(Solution().findMedianSortedArrays([3], [-2, -1]))
