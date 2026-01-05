class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        dp = [float('-inf')] * (l+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, l):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        
        return min(dp[l-1], dp[l-2])
        