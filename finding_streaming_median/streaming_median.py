# insertion or deletion in heapq is O(log(n)) and accessing it is O(1)
# The idea is have a sorted array where you grab the middle value
# break the list into two halves and use priority Queue
# small heap and large heap, make sure elements in both of the heaps are balanced
# small heap--> max heap, O(1)
# Large heap--> min heap, O(1)

import heapq


class MedianFinder:
    def __init__(self):
        # initializing two arrays
        self.small, self.large = [], []

    def add_num(self, num):
        # pushing elements into small heap
        heapq.heappush(self.small, -1 * num)
        # make sure that small heap is <= every elem in large heap
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            # By default min heap is implemented in python hence we need to mutiply by -1
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def find_median(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return ((-1 * self.small[0]) + (self.large[0])) / 2

