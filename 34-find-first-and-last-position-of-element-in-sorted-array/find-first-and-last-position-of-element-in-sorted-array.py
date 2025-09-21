class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        flg=0
        cnt=0
        out=[-1, -1]
        for n in nums:
            
            if(n==target):
                if(flg==0):
                    flg=1
                    out[0] = cnt
            if(n!=target):
                if(flg==1):
                    flg=0
                    out[1] = cnt-1
            
            if(cnt == len(nums)-1):
                if(flg==1):
                    out[1]=cnt
            
            

            cnt+=1
        
        return out


                

