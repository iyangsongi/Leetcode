class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice = 0
        for i in range(len(prices)):
            if i == len(prices) - 1:
                print(i)
                return maxprice
            if prices[i + 1] > prices[i]:
                maxprice += prices[i + 1] - prices[i]
        return maxprice
        