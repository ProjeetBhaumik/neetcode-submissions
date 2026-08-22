class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1

        for i,n in count.items():
            if n == 1:
                return i