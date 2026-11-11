class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        count = 0
        max_time = 0.0
        # 单调栈
        stack = []
        for p, s in cars:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)   