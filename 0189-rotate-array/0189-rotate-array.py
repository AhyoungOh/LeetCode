class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if k == 0:
            return
        k = k % len(nums)
        length = len(nums)
        ins = nums[length-k:]
        ins.extend(nums)
        del ins[length:]
        for i in range(len(nums)):
            nums[i] = ins[i]