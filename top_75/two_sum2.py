# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# this solution without any extra memory without hashmap and array is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1   
            else:
                return [l+1,r+1]           
        return


#  with Hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_hash = {}
        for i in range(len(nums)):
            
            diff = target-nums[i]
            if diff in my_hash:
                return [my_hash[diff], i]
            else:
                my_hash[nums[i]] = i
            
        return
