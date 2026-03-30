class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1        # first pointer = index to put value 

        for right in range (1, len(nums)):   # second pointer scanning thru whole array 
            # if not duplicate, add to left pointer index 
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left = left + 1
        return left