"""
https://neetcode.io/problems/buy-and-sell-crypto
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_profit = 0
        for price in prices:
            # print(low, max_profit)
            if price < low:
                low = price
            diff = price - low
            if diff > max_profit:
                max_profit = diff
        return max_profit
