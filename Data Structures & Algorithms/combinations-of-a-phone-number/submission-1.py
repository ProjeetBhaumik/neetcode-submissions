class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numdict = {'2':'abc','3':'def','4':'ghi',
        '5':'jkl','6':'mno',
        '7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        
        def backtrack(i, path):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            
            for c in numdict[digits[i]]:
                backtrack(i+1,path+c)
                

        if digits:
            backtrack(0,"")
        return res

