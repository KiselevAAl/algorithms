class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        res = 0
        q = []
        for i in range(n):
            res += costs[i][0]
            heapq.heappush(q, costs[i][1] - costs[i][0])
        for i in range(n, 2 * n):
            res += costs[i][0]
            res += heapq.heappushpop(q, costs[i][1] - costs[i][0])
        return res