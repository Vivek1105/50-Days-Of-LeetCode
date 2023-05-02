# Problem - "1822. Sign of the Product of an Array"


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n = len(nums)
        negatives = 0
        for i in range(n):
            if nums[i] < 0:
                negatives += 1
            elif nums[i] == 0:
                return 0
        if negatives % 2 == 0:
            return 1
        else:
            return -1
