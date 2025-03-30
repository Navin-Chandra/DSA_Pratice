from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        
        for i, n in enumerate(nums):
            rem = target - n
            if rem in check:
                return[check[rem], i]
            else:
                check[n]=i
        
        return

program = Solution()        
nums = [2,7,11,15]
target = 9

print(program.twoSum(nums=nums, target=target))