class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
          return 0
        if n == 1 or n == 2: 
          return 1

        aa = [0, 1, 1, 2]

        cnt = 3

        while cnt <= n:
          if cnt == n:
            return aa[3]
          _ = aa[1] + aa[2] + aa[3]
          aa[0], aa[1], aa[2], aa[3] = aa[1], aa[2], aa[3], _
          cnt = cnt + 1

soln = Solution()


# print(soln.tribonacci(0))
# print(soln.tribonacci(1))
# print(soln.tribonacci(2))
print(soln.tribonacci(4))
print(soln.tribonacci(25))