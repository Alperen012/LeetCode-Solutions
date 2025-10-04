class Solution:
    def maxArea(self, height: List[int]) -> int:
        lenght = len(height)

        i = 0
        j = lenght-1
        max_o = 0
        while(i<j):
            temp = min(height[i],height[j])*(j-i)
            if(temp>max_o):
                max_o = temp
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_o

        