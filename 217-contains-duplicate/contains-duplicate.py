class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)):
            if i==0:
                continue
            if nums[i-1] == nums[i]:
                return True
        
        return False
        