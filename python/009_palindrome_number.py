'''
9. Palindrome Number [Easy]
https://leetcode.com/problems/palindrome-number/
O(n) time, O(n) space; string reverse
'''

class Solution:
    def isPalindrome(self, x):
        return str(x)[::-1] == str(x)

print(Solution().isPalindrome(1001))