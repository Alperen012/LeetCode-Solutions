class Solution(object):
    def reverse(self, x):
        """
        :type x: intdior
        dir
        dir
        a
        
        :rtype: int
        """
        a=0
        c=x
        b=1

        if c<0:
            x=-x
            
        for i in range(len(str(x))):
            i=int(str(x)[i])
            a=a+(b*i)
            b=b*10
                
        if c<0:
            a=-a
        
        if -(2147483648)<a<2147483648:
            return a
        else:
            return 0
            
        
