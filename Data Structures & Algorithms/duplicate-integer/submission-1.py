class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dups = {}

        for num in nums:
            if num not in count_dups:
                count_dups[num] = 1
            else:
                return True
    
        return False
        
