class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # 第一遍：res[i] = 左边所有元素的乘积
        left = 1
        for i in range(n):
            res[i] = left          # 先记下"不含自己"的左边乘积
            left *= nums[i]        # 再把 nums[i] 累进 left，留给下一个位置

        # 第二遍：res[i] 再乘上右边所有元素的乘积
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right        # 左边乘积 × 右边乘积
            right *= nums[i]       # 把 nums[i] 累进 right，留给前一个位置

        return res     