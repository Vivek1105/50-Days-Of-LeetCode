import heapq
from collections import Counter

class T:
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, nums, k):
        result = []
        counter = Counter(nums)
        min_heap = []

        for num, freq in counter.items():
            heapq.heappush(min_heap, T(num, freq))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        while min_heap:
            result.append(heapq.heappop(min_heap).num)

        return result
