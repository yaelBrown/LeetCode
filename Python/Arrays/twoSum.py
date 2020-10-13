def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    idx1 = 0
    idx2 = 0

    cnt = 1
    for n in nums: 
        if (cnt+1) > len(nums):
            continue
        if n + nums[cnt] == target:
            idx1 = nums.index(n)
            idx2 = cnt
            return [idx1, idx2]
        cnt = cnt+1

    # n and cnt are the same value

        
a = [2,7,11,15]
a2 = [3,3]
a3 = [3,2,3]
b = 9
b2 = 6
b3 = 6

# print(twoSum(a,b))
# print(twoSum(a2,b2))
print(twoSum(a3,b3))