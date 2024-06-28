# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        # slide window
        # o i representa indice que está correndo na frente e j o indice de trás
        # j vai guardar o indice onde tem repetição 
        res = 0
        memo = {}
        j = 0
        for i in range(len(s)):   
            char = s[i]
            if char in memo:
                j = max(memo[char], j)
            res = max(res, i - j + 1)
            memo[char] = i + 1
        return res  

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring('pwwkew'))
    print(sol.lengthOfLongestSubstring('bbbbb'))
    print(sol.lengthOfLongestSubstring('abcabcbb'))
    print(sol.lengthOfLongestSubstring('dvdf'))
