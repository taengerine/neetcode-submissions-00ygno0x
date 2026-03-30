class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countmap = {}
        n = len(nums)
        majority = n/2

        for num in nums:
            if num not in countmap:
                countmap[num] = 1
            else:
                countmap[num] += 1
                if countmap[num] > majority:
                    return num

        return num
