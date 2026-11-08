class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val, idx):
        self.heap.append((val, idx))
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return top

    def peek(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] > self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = MaxHeap()
        res = []

        for i in range(len(nums)):
            heap.push(nums[i], i)

            if i >= k - 1:
                # 懒删除：堆顶如果已经滑出窗口，就弹出
                while heap.peek()[1] <= i - k:
                    heap.pop()
                res.append(heap.peek()[0])

        return res