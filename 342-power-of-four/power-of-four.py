class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        elif n==1:
            return True
        while n>=4:
            if n%4!=0:
                return False
            if n==4:
                return True
            print(n/4)
            n = n/4
            
        return False