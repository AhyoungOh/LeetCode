class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = 0
        maxi = 1
        result = 0
        while maxi < len(prices):
            if prices[mini] < prices[maxi]:
                result = max(prices[maxi] - prices[mini], result)
            else:
                mini = maxi
            maxi += 1
        return result