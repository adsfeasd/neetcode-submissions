class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # 维护大小为 k 的最小堆，堆顶是"当前 k 个里频率最小的"
        heap = []
        for num, cnt in freq.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for _, num in heap]  