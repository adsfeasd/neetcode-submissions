
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)

        # 确定答案的上下界
        left = max(1, (total + h - 1) // h)
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            # 计算当前速度需要的总时间
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid

            if hours <= h:
                # 当前速度可行，尝试更小的速度
                right = mid
            else:
                # 当前速度不可行，必须提高速度
                left = mid + 1

        return left
