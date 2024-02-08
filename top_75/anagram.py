# basic bootforce

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)

        if len(s) ==len(t):
            set_s, set_t = {}, {}
            for i in range(len(s)):
                val =s[i]
                if val in set_s:
                    count = set_s[val]
                    set_s[val] = count +1
                else:
                    set_s[val] = 1 

                val2 =t[i]
                if val2 in set_t:
                    count = set_t[val2]
                    set_t[val2] = count +1
                else:
                    set_t[val2] = 1  
            
            for j in set_s:
                if j in set_t:
                    if set_s[j] != set_t[j]:
                        return False
                else:
                    return False

            return True

            
                  
        else:
            return False
            
            
            
    # clean code
    def another(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        set_s, set_t = {}, {}
        for i in range(len(s)):
            set_s[s[i]] = 1 + set_s.get(s[i], 0)
            set_t[t[i]] = 1 + set_t.get(t[i], 0)
        
        for j in set_s:
            if set_s[j] != set_t.get(j, 0):
                return False
        return True
        
            
            