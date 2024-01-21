class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)

        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
            
        q = []
        dist = [INF] * len(graph)

        heapq.heappush(q, (0, k))
        dist[k] = 0
        while q:
            acc, cur = heapq.heappop(q)
            
            if dist[cur] < acc:
                continue
            
            for adj, d in graph[cur]:
                cost = acc + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(q, (cost, adj))

        return max(dist[1:]) if max(dist[1:]) < INF else -1
        