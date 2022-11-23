"""
Робот находится в верхнем левом углу(т.е. сетка[0][0]).
Роботу необходимо переместиться в правый нижний угол (т.е. в сетку[m - 1][n - 1]). Робот может двигаться только  вниз или вправо
Робот должен добраться до нижнего правого угла, за любое количество возможных уникальных путей

Сложность - O(N)

"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[n - 1]