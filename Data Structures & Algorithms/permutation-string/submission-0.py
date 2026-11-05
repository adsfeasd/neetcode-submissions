class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        # 第一个窗口
        for i in range(n1):
            window[ord(s2[i]) - ord('a')] += 1

        if window == need:
            return True

        # 滑动窗口
        for right in range(n1, n2):
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[right - n1]) - ord('a')] -= 1

            if window == need:
                return True

        return False