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
    

    def isAnagram_2(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashmap_s,  hashmap_t = {}, {}

        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i],0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i],0)

        for char in hashmap_s:
            if hashmap_s[char] != hashmap_t.get(char, 0):
                return False

        return True


program = Solution()
# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"

print(program.isAnagram_2(s=s,t=t))


