class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):
            # 1. 右指针扩展窗口
            char = s[right]
            count[char] = count.get(char, 0) + 1

            # 2. 如果窗口不合法，就收缩左边界
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            # 3. 此时窗口合法，更新最长长度
            max_length = max(max_length, right - left + 1)

        return max_length
