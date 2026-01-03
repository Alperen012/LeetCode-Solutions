class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if(s==""): return True
        ls = len(s)
        lt = len(t)
        if(ls>lt): return False
        k=0
        for i in range(lt):
            if(t[i]==s[k]):
                k+=1
                if(ls == k):return True
        
        return lt == k
            