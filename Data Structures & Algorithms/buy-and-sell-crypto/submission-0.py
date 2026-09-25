class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s=0,1
        maxp = 0
        for i in range(len(prices)-1):
            if prices[b]<prices[s]:
                profit = prices[s]-prices[b]
                maxp = max(profit,maxp)
            else: 
                b=s
            s+=1
        return maxp

        