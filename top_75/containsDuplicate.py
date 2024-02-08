class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set =set()

        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)
        
        return False

        # found = False
        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             found =True

        # return found


        