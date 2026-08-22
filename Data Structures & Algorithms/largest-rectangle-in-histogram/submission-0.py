class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxH = 0
        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxH = max(maxH,height*(i-index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            maxH = max(maxH,h*(len(heights)-i))

        return maxH