class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(cap):
            # can we with the attempted capacity
            # ship all weights
            # in given number of days
            ships = 1
            currcap = cap
            for w in weights:
                # we add the weight as long as capacity is met
                if currcap - w  >= 0:
                    currcap -= w
                else:
                    ships += 1
                    currcap = cap - w
            
            if ships > days:
                return False
            return True

        
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            m = (l+r)//2
            if canship(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
            