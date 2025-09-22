class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        max_freq = 0
        for count in freq.values():
            if count > max_freq:
                max_freq = count
        
        total = 0
        for count in freq.values():
            if count == max_freq:
                total += count
        
        return total
        