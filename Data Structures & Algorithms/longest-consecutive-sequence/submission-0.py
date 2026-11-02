class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)          # O(1) 判存在
        longest = 0

        for x in num_set:
            if x - 1 in num_set:     # 不是起点，跳过（避免重复数）
                continue

            cur = x
            length = 1
            while cur + 1 in num_set:   # 从起点一路往上数
                cur += 1
                length += 1

            longest = max(longest, length)

        return longest