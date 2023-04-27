# Problem - 2336. Smallest Number in Infinite Set

class SmallestInfiniteSet:

    def __init__(self):
        self.set = set(range(1, 1001))
        
    def popSmallest(self) -> int:
        smallest = min(self.set)
        self.set.remove(smallest)
        return smallest
        
    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
