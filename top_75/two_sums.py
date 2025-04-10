class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ar_len = len(nums)
        for i in range(ar_len):
            # elm = List[i]
            for j in range(i+1, ar_len):
                if target == nums[i] + nums[j]:
                    return [i,j]

        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in my_hash:
                return [my_hash[diff], i]
            my_hash[n] = i
        return  


# # using hashmap
# def twoSumHash(nums,  target ):
    
#     my_hash = {} # val : index

#     for i, n in enumerate(nums):
#         diff = target - n
#         if diff in my_hash:
#             return [my_hash[diff], i]
#         my_hash[n] = i
#     return  

# nums = [2,7,11,15]
# target = 9

# Solution.twoSumHash(nums=nums,target=target)