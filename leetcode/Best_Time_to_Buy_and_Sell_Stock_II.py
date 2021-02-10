class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_gain = 0
        
        for i in range( len(prices)-1 ):
            
            if prices[i] < prices[i+1]:
                
                price_gain=price_gain+( prices[i+1]- prices[i])
                
        return ( price_gain )