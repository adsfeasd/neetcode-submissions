class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. 按位置降序排序：离 target 近的在前
        cars = sorted(zip(position, speed), reverse=True)

        count = 0
        max_time = 0.0

        for p, s in cars:
            t = (target - p) / s

            # 比当前最慢的 fleet 还慢 → 新 fleet
            if t > max_time:
                count += 1
                max_time = t

        return count