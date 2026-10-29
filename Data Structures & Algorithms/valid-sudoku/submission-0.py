class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows  = [set() for _ in range(9)]   # rows[r]  : 第 r 行已出现的数字
        cols  = [set() for _ in range(9)]   # cols[c]  : 第 c 列已出现的数字
        boxes = [set() for _ in range(9)]   # boxes[k] : 第 k 个 3x3 盒子已出现的数字

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue                # 空格跳过

                box = (r // 3) * 3 + (c // 3)   # 关键：格子编号

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False                # 任一维度重复即非法

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True    