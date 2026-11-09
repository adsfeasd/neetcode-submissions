class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n          # j 后面没有更高的，i 也没有
                    break
                j = j + res[j]     # 跳到 j 的下一个更高元素

            if j < n:
                res[i] = j - i

        return res