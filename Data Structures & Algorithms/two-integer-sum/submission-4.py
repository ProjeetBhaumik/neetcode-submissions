class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value -> index

        for index, num in enumerate(nums):
            res = target - num 
            if res in seen:
                return [seen[res],index]
            seen[num] = index
