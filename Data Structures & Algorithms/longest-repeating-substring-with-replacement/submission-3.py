class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        n = len(s)
        count = defaultdict(int)
        maxC = 0
        res = 0

        for r in range(n):
            count[s[r]] += 1
            maxC = max(maxC,count[s[r]])

            while (r - l +1) - maxC > k:
                count[s[l]] -=1
                l += 1
            res = max(res,r-l+1)
        
        return res


