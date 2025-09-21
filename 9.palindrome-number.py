#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## Full reversal int algo
        
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        # reversed = 0
        # original = x
        # while x > 0:
        #     reversed = reversed * 10 + (x % 10)
        #     x //= 10

        # return original == reversed
        
        ## Simplest solution that comes to mind for python
        
        # s = str(x)
        # return s == s[::-1]
        
        ## Two Pointers approach for better stat:
        #         Accepted
        # 11511/11511 cases passed (0 ms)
        # Your runtime beats 100 % of python3 submissions
        # Your memory usage beats 20.04 % of python3 submissions (18 MB)
        
        if x < 0:
            return False
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
# @lc code=end
