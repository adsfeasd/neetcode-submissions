class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            # 剪枝：最小的数都 > 0，后面不可能凑出 0
            if nums[i] > 0:
                break

            # 去重：固定数 nums[i] 跳过重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                cur = nums[left] + nums[right]

                if cur == target:
                    res.append([nums[i], nums[left], nums[right]])

                    # 去重：left 跳过重复
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 去重：right 跳过重复
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif cur < target:
                    left += 1
                else:
                    right -= 1

        return res