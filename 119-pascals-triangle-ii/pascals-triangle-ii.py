class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = []

        for i in range(rowIndex+1):
            row = [1] * (i + 1)
            
            for j in range(1, i):
                row[j] = rows[i-1][j-1] + rows[i-1][j]
            
            rows.append(row)

        return rows[rowIndex]