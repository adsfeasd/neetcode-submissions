class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs:
                # 右括号：检查栈顶
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # 左括号：入栈
                stack.append(ch)

        return not stack