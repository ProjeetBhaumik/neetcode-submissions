class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        heapq.heapify(prices)

        first = heapq.heappop(prices)
        second = heapq.heappop(prices)
        
        total = first + second

        if total <= money:
            return money - total
        return money