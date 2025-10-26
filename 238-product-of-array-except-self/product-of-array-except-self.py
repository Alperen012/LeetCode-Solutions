class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        for i in nums:
            mul *= i
        r=[]
        for i in range(len(nums)):
            if(nums[i] == 0):
                m=1
                flg=0
                z_cnt=0
                for j in nums:
                    if(j==0):z_cnt+=1
                    else:
                        flg=1
                        m *= j
                if(z_cnt>1):r.append(0)
                else:r.append(m*flg)
            else:
                r.append(mul // nums[i]) 
        
        return r