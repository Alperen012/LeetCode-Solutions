class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        b=0
        for i in range(len(x)):
            if x[b]==x[len(x)-b-1]:
                b+=1
            else:
                return False
        return True
            