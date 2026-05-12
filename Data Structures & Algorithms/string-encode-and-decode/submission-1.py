class Solution:
#  Eg. ["lint","code","love","you"] will become "4#lint4#code4#love3#you" as the encoded string.

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0

        while i<len(s):
            j=i

            while s[j] !='#':
                j+=1
            length =int(s[i:j])

            j+=1

            result.append(s[j:j + length])
            i=j+length 
        return result

