class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            total = 0
            for p in piles:
                total += (p + k - 1) // k   # 向上取整
                if total > h:               # 提前剪枝
                    return False
            return total <= h

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid          # mid 满足，答案在 [left, mid]
            else:
                left = mid + 1       # mid 不满足，答案在 [mid+1, right]

        return left