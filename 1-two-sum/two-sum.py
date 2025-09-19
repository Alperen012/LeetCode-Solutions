class Solution(object):
    def twoSum(self, nums, target):
        x=[]
        a=-1
        for i in nums:
            a+=1
            nums.pop(a)
            if (target-i) in nums:
                x.append(a)
            nums.insert(a,i)
        return x