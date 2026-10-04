class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 5,4,3
        # -5,-4,-3
        #
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones,first-second)

        stones.append(0)
        return -(stones[0])