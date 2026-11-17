class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1      # 最小值在右边，mid 排除
            else:
                right = mid         # 最小值在左边或就是 mid

        return nums[left]