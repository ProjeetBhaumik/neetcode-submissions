class Solution:
    def isValid(self, s: str) -> bool:
        
        opentoclose = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in opentoclose:
                if stack and opentoclose[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack


                
