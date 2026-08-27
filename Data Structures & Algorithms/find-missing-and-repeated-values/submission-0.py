class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        gridSum = 0
        gridSqSum = 0

        for i in range(N):
            for j in range(N):
                gridSum += grid[i][j]
                gridSqSum += grid[i][j] * grid[i][j]

        totSum = (N * N * (N * N + 1)) // 2
        diff = gridSum - totSum  # a - b

        totSqSum = (N * N * (N * N + 1) * (2 * N * N + 1)) // 6
        sqDiff = gridSqSum - totSqSum  # (a^2) - (b^2)

        sum = sqDiff // diff  # a + b

        a = (sum + diff) // 2
        b = sum - a
        return [a, b]