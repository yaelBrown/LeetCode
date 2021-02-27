class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2: 
          return 0
        
        if len(set(nums)) == 1:
          return [0 for x in range(len(nums))]
        
        temp = []
        for i in nums: 
          temp.append(i)
        
        temp.sort()
        
        out = []
        
        for i in nums:
          out.append(temp.index(i))
          
        return out