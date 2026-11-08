class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for right in range(len(nums)):

            # 1. 删除已经离开窗口的元素
            while q and q[0] <= right - k:
                q.popleft()

            # 2. 删除队尾中不可能再成为最大值的元素
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            # 3. 加入当前元素的下标
            q.append(right)

            # 4. 窗口形成后，记录最大值
            if right >= k - 1:
                result.append(nums[q[0]])

        return result
