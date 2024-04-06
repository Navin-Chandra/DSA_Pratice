# def maxProfit(prices):

#         profit = 0
#         my_hash = {}
#         l, r = 0, len(prices)-1
#         print(l,r)
#         while l < r:
#             if prices[l] > prices[r]:
#                 l +=1
#             else:
#                 diff = prices[r] - prices[l]

#                 my_hash[diff] = {prices[l], prices[r]}

#                 r -=1
#                 if diff > profit:
#                     profit = diff
        

#         return profit
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        mini = prices[0]
        maxi = 0
        for i in prices:
            maxi = max(maxi, i - mini)
            mini = min(mini, i)
        return maxi

prices = [7,1,5,3,6,4]

my = Solution()
print(my.maxProfit(prices))