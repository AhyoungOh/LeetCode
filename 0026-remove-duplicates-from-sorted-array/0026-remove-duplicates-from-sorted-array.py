class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        num = len(nums) -1
        while i < num:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
                num -= 1
                i -= 1
            i += 1
        return len(nums)