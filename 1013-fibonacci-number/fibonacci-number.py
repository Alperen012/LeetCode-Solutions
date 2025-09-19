class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a=[1,2]
        
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        elif n==3:
            return 2
        
        
        for i in range(n-3):
            a.append(a[0]+a[1])
            a.pop(0)
                  
        return a[1]
        
        