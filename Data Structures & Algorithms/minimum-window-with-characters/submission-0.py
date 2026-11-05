class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)
        window = {}
        valid = 0

        left = 0
        start = 0
        min_len = float('inf')

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                valid += 1

            # 窗口满足条件，尝试收缩求最短
            while valid == len(need):
                # 更新答案
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1

                # 移除 s[left]
                left_ch = s[left]
                if left_ch in need and window[left_ch] == need[left_ch]:
                    valid -= 1
                window[left_ch] -= 1
                left += 1

        return s[start:start + min_len] if min_len != float('inf') else ""