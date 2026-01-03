class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if(s==""): return True
        if(len(s)>len(t)): return False
        
        k=0
        l = len(s)
        for i in range(len(t)):
            if(t[i]==s[k]):
                k+=1
                if(l == k):return True
        
        return len(s) == k
            