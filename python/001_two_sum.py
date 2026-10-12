"""
1. Two Sum [Easy]

https://leetcode.com/problems/two-sum/
0(n^2) time, 0(1) space; brute force
"""

class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for outerpointer in range(length-1):
            for innerpointer in range(outerpointer + 1, length):
                if nums[outerpointer] + nums[innerpointer] == target:
                    return [outerpointer, innerpointer]


# print(Solution().twoSum([2, 7, 11, 15], 9))


"""" 

# Earlier solution (kept for reference)
# Same algorithm, manual pointer reset (without range) with while loops

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


"""