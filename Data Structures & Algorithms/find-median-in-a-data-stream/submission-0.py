class MedianFinder:

    def __init__(self):
        self.small = [] #max heap
        self.big = []   #min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num)
        if self.big and num > self.big[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big,val)

        if len(self.small) > len(self.big) +1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big,val)
        if len(self.big) > len(self.small) +1:
            val = heapq.heappop(self.big)
            heapq.heappush(self.small,-1 * val)        
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            val = -1 * self.small[0]
            return val
        if len(self.big) > len(self.small):
            return self.big[0]
        
        return (-1*self.small[0]+self.big[0]) / 2