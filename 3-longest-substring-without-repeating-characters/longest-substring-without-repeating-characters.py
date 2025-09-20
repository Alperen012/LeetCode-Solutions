class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {chr(i): -1 for i in range(128)}

        my_sub=sub.copy()
        cnt=0
        cnt_max=0
        i=0
        while(i<len(s)):
            if(my_sub[s[i]]==-1):
                my_sub[s[i]]=i
                cnt+=1
            else:

                i = my_sub[s[i]]+1

                my_sub=sub.copy()
                if(cnt>cnt_max):
                    cnt_max=cnt
                cnt=0
                my_sub[s[i]]=i
                cnt+=1
            i+=1
        if(cnt>cnt_max):
            cnt_max=cnt
        
        return cnt_max
            

        