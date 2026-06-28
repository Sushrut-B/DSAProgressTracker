class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        mini=prices[0]
        for i in range(len(prices)):
            profit=prices[i]-mini
            max_profit=max(max_profit,profit)
            mini=min(mini,prices[i])
        return max_profit