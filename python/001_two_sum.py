"""
1. Two Sum [Easy]

https://leetcode.com/problems/two-sum/
0(n^2) time, 0(1) space; brute force
"""

class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        outerpointer = 0
        innerpointer = 1

        while outerpointer < length - 1:
            if nums[outerpointer] + nums[innerpointer] == target:
                return [outerpointer, innerpointer]

            innerpointer += 1

            if innerpointer == length:
                outerpointer += 1
                innerpointer = outerpointer + 1