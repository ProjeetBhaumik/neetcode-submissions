class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        n = len(heights)
        l,r = 0,n-1

        while l <= r:
            left = heights[l] 
            right = heights[r]
            area = min(right,left) * (r-l)
            maxA = max(area,maxA)
            if left < right:
                l += 1
            else:
                r -= 1
        
        return maxA