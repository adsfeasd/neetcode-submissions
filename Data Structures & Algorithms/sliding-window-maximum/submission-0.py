class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []   # (-值, 下标)
        res = []

        for i in range(n):
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                # 清理不在窗口内的堆顶
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])

        return res