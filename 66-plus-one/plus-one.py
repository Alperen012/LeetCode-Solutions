class Solution(object):
    def plusOne(self, digits):
        if len(digits)==1:
            if digits[0]<9:
                digits[0] = digits[0]+1
                return digits
            else:
                return [1,0]
        else:
            for i in range(len(digits)):
                i=i+1
                if digits[-i]<9:
                    digits[-i]= digits[-i]+1
                    return digits
                else:
                    digits[-i] = 0
            digits.insert(0,1)
            return digits
        