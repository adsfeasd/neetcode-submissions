class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)) + "#" + s)   # 长度 + '#' + 内容
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 1. 从 i 开始找 '#'，'#' 前是长度数字
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # 2. 内容从 j+1 开始，精确取 length 个字符
            start = j + 1
            res.append(s[start:start + length])

            # 3. 下一段的起点
            i = start + length
        return res