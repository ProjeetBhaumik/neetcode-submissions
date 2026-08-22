class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #index,temperature
        res = [0]*len(temperatures)
        for index,temp in enumerate(temperatures):

            while stack and stack[-1][1] < temp:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = index - stackInd
            stack.append((index,temp))
        return res