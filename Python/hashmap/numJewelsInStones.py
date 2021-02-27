class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """      
        if len(jewels) == 0: 
          return 0
        if len(stones) == 0:
          return 0
        
        cnt = 0
        
        for i in stones:
          if i in jewels:
            cnt += 1
            
        return cnt