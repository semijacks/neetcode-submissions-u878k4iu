class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for p in points:
            d = -(math.sqrt((p[0]-0) ** 2 + (p[1]-0) ** 2))
            heapq.heappush(maxHeap, (d, p))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [p for d, p in maxHeap]

        

        