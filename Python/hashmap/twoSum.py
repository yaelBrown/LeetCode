class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = k = len(nums) - 1
        # [2,7,11,15]
        while i != k:
            if (nums[i] + nums[j]) == target:
                return [i,j]
            else: 
                j = j - 1
                if j is i:
                    i = i + 1
                    j = k
            