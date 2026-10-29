class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1                       # 键不存在时默认 0，再 +1

        # 按"值"（频率）降序排序，取前 k 个的键
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_items[:k]]       