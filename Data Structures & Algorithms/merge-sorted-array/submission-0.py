class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = m - 1, n - 1
        curr = len(nums1) - 1
        while 0 <= ptr1 and 0 <= ptr2:
            if nums2[ptr2] > nums1[ptr1]:
                nums1[curr] = nums2[ptr2]
                ptr2 -= 1
                curr -= 1
            else: 
                nums1[curr] = nums1[ptr1]
                ptr1 -= 1
                curr -= 1
        
        if 0 <= ptr2:
            while 0 <= curr:
                nums1[curr] = nums2[ptr2]
                ptr2 -= 1
                curr -= 1

        

        