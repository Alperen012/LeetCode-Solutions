class Solution:
    def numOfWays(self, n: int) -> int:
        
        dp = [0]*(n+1)
        
        abc = 6
        aba = 6
        if(n==1):return 12
        dp[1] = 12
        for i in range(2,n+1):
            Nabc = (2 * abc + 2 * aba) % 1000000007
            Naba = (3 * aba + 2 * abc) % 1000000007

            abc = Nabc
            aba = Naba
        
        return (abc + aba) % 1000000007
        