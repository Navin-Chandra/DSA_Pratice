
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =   defaultdict(list)

        for s in strs:
            count =[0]*26 # a ...... z for all letter 0 count initially

            for c in s:
                # count[ord(s) - ord("a")] +=1
                count[ord(c) - ord("a")] += 1


            res[tuple(count)].append(s)
        
        print(res)

        return list(res.values())

program = Solution()
strs =["eat","tea","tan","ate","nat","bat"]

print(program.groupAnagrams(strs=strs))