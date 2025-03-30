class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashmap_s = dict()
        hashmap_t = dict()

        for i in range(0,len(s)):
            key = s[i]
            # print(key)
            if s[i] in hashmap_s:
                hashmap_s[key] = hashmap_s[key]+1
            else:
                hashmap_s[key] = 1
            
            if t[i] in hashmap_t:
                hashmap_t[t[i]] = hashmap_t[t[i]]+1
            else:
                hashmap_t[t[i]] = 1

        for char in hashmap_s:
            if hashmap_s[char] != hashmap_t.get(char, 0):
                return False
            # return hashmap_s == hashmap_t

        return True


program = Solution()
# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"

print(program.isAnagram(s=s,t=t))


