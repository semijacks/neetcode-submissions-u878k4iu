class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        minHeap = []
        res = [0] * len(queries)
        i = 0

        for q, original_idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[original_idx] = minHeap[0][0] if minHeap else -1

        return res
        