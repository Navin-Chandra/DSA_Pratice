class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""

        for s in strs:
            res += str(len(s)) + "#" +s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here

        res, i = [], 0
        
        while i < len(str):
            j = i
            print(str[j])

            while str[j] != "#":
                j += 1

            print(str[i:j])
            length = int(str[i:j])

            print(str[j+1 : j+1 + length])
            res.append(str[j+1 : j+1 + length])
            i = j + 1 + length
        
        return res



s = Solution()

Input= ["lint","code","love","you"]
Output= ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

encode_out =  s.encode(Input)
# print(encode_out)

out_decode =  s.decode(encode_out)
print(out_decode)
print(encode_out[2:6])
print(encode_out[8:12])

print("\n #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\n")
# Input= ["we", "say", ":", "yes"]
# Output= ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"


# encode_out =  s.encode(Input)
# print(encode_out)

# out_decode =  s.decode(encode_out)
# print(out_decode)
