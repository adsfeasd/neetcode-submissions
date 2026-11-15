class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 首尾加 0 作为哨兵
        heights = [0] + heights + [0]
        stack = []   # 存下标，对应高度单调递增
        ans = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                mid = stack.pop()
                left = stack[-1]   # 新栈顶就是左边界
                width = i - left - 1
                ans = max(ans, heights[mid] * width)
            stack.append(i)

        return ans