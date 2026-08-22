class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxS = 0
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxS = max(count[s[r]],maxS)
        
            while (r-l+1) - maxS > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res