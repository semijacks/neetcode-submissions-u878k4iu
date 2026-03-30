class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        # min_buy = 0
        left = 1

        while left < len(prices):
            sell = prices[left]
            buy = prices[left - 1]
            min_buy = min(min_buy, buy)
            profit = sell - min_buy
            max_profit = max(max_profit, profit)
            left += 1

        return max_profit
        