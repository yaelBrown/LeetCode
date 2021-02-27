class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
          return 0
        
        map = {}
        
        for i in nums: 
          if i not in map:
            map[i] = 1
          else: 
            map[i] += 1
          
        sum = 0
        for val in map.values():
          sum += (val * (val - 1 ) / 2)
          
        return int(sum)