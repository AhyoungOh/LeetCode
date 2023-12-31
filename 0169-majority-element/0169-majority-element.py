class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        t = 0
        for i in nums:
            if i != m:
                if t < nums.count(i):
                    t = nums.count(i)
                    m = i
        return m