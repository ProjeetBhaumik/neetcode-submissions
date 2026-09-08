class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) -1

        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            
            # left side sorted
            if nums[l] <= nums[m]:
                # target in left side
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # target not in left side
                else:
                    l = m + 1
            
            # right side sorted
            else:
                # target in right side
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # target in left side
                else:
                    r = m -1
        
        return -1 


                    
            