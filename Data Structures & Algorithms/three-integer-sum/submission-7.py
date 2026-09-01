class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4,-1,-1,0,1,2
        nums.sort()
        res = []

        for index,number in enumerate(nums):
            l = index + 1
            r = len(nums) -1
            if index > 0 and number == nums[index-1]:
                continue

            while l < r:
                total = number + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([number,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1 


        
        return res
