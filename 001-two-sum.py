# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    # solução força bruta
    def twoSum(self, l, target):
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == target:
                    return [i, j]
                
    # solução mais otimizada
    # faz subtração para achar o resultado
    def twoSum2(self, l, target):
        memo = {}
        for i, n in enumerate(l):
            if target - n in memo.keys():
                return [memo[target - n], i]
            memo[n] = i

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    result = Solution().twoSum2(nums, target)
    print(result)
