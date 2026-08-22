class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 
        def canship(m):
            ships,currCap = 1,m
            for w in weights:
                if currCap < w:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = m
                currCap -= w
            return True

        l,r = max(weights),sum(weights)
        res = 0
        while l <= r:
            m = (l+r)//2
            if canship(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res