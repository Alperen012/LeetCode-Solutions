class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        
        a=[0,1,1]
        
        for i in range(n-2):
            a.append(a[0]+a[1]+a[2])
            a.pop(0)
                  
        return a[2]