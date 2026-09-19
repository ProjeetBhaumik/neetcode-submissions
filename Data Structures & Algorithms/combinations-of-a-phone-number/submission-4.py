class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digchar = {"2":"abc","3":'def',"4":"ghi","5":"jkl","6":"mno",
                    "7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def backtrack(i,sub):
            if len(sub) == len(digits):
                res.append(sub)
                return
            for c in digchar[digits[i]]:
                backtrack(i+1,sub+c)
        if digits:
            backtrack(0,"")

        return res