# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    out_put = {}
    for wrd in strs:
        print(wrd)
        key =''.join(sorted(wrd))
        # print(key)
        # if key_to_check in my_dict.keys():
        if key in out_put.keys():
            out_put[key].append(wrd)

        else:
            out_put[key]= [wrd]


#  top submission:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    combos = {}
    for i in strs:
        letters = []
        for j in i:
            letters.append(j)
        letters.sort()
        key = ''.join(letters)
        if key in combos:
            combos[key].append(i)
        else:
            combos[key] = [i]
    output = []
    for i in combos:
        output.append(combos[i])
    return output


# neet code way
#  top submission:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for s in strs:
        count =[0]*26 # a ...... z for all letter 0 count initially

        for c in s:
            count[ord(s) - ord("a")] +=1

        res[tuple(count)].append(s)
    
    print(res)

    return res.values()