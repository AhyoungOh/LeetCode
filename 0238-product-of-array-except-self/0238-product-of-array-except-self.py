class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [0] * length
        
        res[0] = 1
        for i in range(1, length):

            res[i] = nums[i - 1] * res[i - 1]
        
        right = 1
        for i in reversed(range(length)):
            
            res[i] = res[i] * right
            right *= nums[i]
        
        return res
