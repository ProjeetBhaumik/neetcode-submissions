class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen = {')':'(','}':'{',']':'['}

        stack = []

        for c in s:
            #is character a closing bracket
            if c in closetoopen:
                #if end of stack is opening brackets
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
            #add character to stack
                stack.append(c)
        
        return True if not stack else False
