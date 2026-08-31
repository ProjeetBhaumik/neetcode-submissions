class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        input:


        i .. n
 
        


        output:



        """
        result = [0]*len(temperatures) # 1
        stack = [] 
# (index, temperature) (30,0),(38,1),(30,2),(36,3),(35,4),(40,5),(28,6)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                resindx, restemp = stack.pop()
                result[resindx] = index - resindx
            stack.append((index,temp))
        return result


