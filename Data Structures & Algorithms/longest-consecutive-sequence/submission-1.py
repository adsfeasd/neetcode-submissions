class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        length = {}          # 只存每条序列的"两个端点" → 该序列长度
        longest = 0

        for x in nums:
            if x in length:  # 重复数字，跳过
                continue

            left  = length.get(x - 1, 0)   # x 左边那条序列的长度
            right = length.get(x + 1, 0)   # x 右边那条序列的长度
            cur = left + 1 + right         # 合并后的新长度

            length[x] = cur                # 记下 x（也作为临时端点）
            length[x - left]  = cur        # 新序列的左端点
            length[x + right] = cur        # 新序列的右端点

            longest = max(longest, cur)

        return longest