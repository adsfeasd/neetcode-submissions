class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 A 是短数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = nums1, nums2
        m, n = len(A), len(B)

        # 左半部分应该有 k 个元素
        k = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = left + (right - left) // 2
            j = k - i

            # 四个边界值，越界用 ±inf
            A_left  = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i]     if i < m else float('inf')
            B_left  = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j]     if j < n else float('inf')

            if A_left <= B_right and B_left <= A_right:
                # 找到正确分割
                if (m + n) % 2 == 1:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                right = i - 1      # i 太大
            else:
                left = i + 1       # i 太小

        return 0.0