from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        check_dup = set()
        for num in nums:
            if num in check_dup:
                return True
            check_dup.add(num)
        return False


program = Solution()
nums = [1, 2, 3, 1]
# nums = [1, 2, 3, 3]
# nums = [1,2,3,4]

print(program.containsDuplicate(nums=nums))