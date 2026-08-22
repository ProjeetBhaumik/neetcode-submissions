class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temp, index pair
        res = [0]*len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                s_temp, s_index = stack.pop()
                res[s_index] = i - s_index
            stack.append((n, i))
        return res

