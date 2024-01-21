class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = int(1e9)
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        q = []
        heapq.heappush(q, (0, src, k + 1))
        dist = [[INF] * (k + 2) for _ in range(n)]
        while q:
            acc, cur, stops = heapq.heappop(q)
            if cur == dst:
                return acc
            
            if stops < 1:
                continue

            for adj, d in graph[cur]:
                cost = acc + d
                if cost < dist[adj][stops - 1]:
                    dist[adj][stops - 1] = cost
                    heapq.heappush(q, (cost, adj, stops - 1))

        return -1
