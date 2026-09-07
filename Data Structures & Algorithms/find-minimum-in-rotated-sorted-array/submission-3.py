class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        if nums[l] <= nums[r]:
            return nums[l]

        while l < r:
            m = (l + r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]