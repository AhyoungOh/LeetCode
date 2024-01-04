class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current_position = 0
        final_position = len(nums) - 1
        steps = nums[0]

        if not nums:
            return False
        for i in range(0, final_position):
            steps -= 1
            if nums[i] <= nums[i+1] and steps >= 0 and nums[i+1]!=0:
                steps = max(steps, nums[i+1])
            if steps < 0:
                return False 
        return True
        