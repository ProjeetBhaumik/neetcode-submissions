class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t == "+":
                a,b = stk.pop(), stk.pop()
                stk.append(a+b)
            elif t == "-":
                a,b = stk.pop(), stk.pop()
                stk.append(b - a)
            elif t == "*":
                a,b = stk.pop(), stk.pop()
                stk.append(a * b)
            elif t == "/":
                a,b = stk.pop(), stk.pop()
                stk.append(int(float(b) / a))
            else:
                stk.append(int(t))
        return stk[-1]