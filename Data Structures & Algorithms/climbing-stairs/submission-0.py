class Solution:
    def climbStairs(self, n: int) -> int:
        mp = {1:1,2:2}

        def f(n):
            if n in mp:
                return mp[n]
            else:
                mp[n] = f(n-1) + f(n-2)
                return mp[n]
        return f(n)