class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        _m=999999
        sum=0
        for i in tasks:
            sum = i[0] + i[1]
            if(sum<_m):
                   _m=sum
            sum=0
        return _m
        