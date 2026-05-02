class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count=[0]*26

        for i in s:
            count[ord(i)- ord("a")]+=1
        for j in t:
            idx= ord(j)-ord("a")
            count[idx]-=1
            if count[idx]<0:
                return False
        return True
