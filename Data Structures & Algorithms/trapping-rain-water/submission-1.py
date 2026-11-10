class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []   # 存下标，对应高度单调递减
        ans = 0

        for i in range(len(height)):
            # 当前柱子比栈顶高，形成凹槽
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()   # 凹槽底部

                if not stack:
                    break           # 左边没有柱子，接不了水

                left = stack[-1]
                width = i - left - 1
                h = min(height[left], height[i]) - height[mid]
                ans += width * h

            stack.append(i)

        return ans