class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # count = Counter(nums)
        # buckets = [[] for i in range (n+1)]

        # for num, freq in count.items():
        #     buckets[freq].append(num)
        
        # res = []
        # for i in range(n, 0, -1):
        #     for num in buckets[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res

        n = len(nums)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        heap = []
        for c in count.keys():
            heapq.heappush(heap,(count[c],c))
        while len(heap)>k:
            heapq.heappop(heap)
        res = []

        print(heap)
        for freq,num in heap:
            res.append(num)
        return res
      