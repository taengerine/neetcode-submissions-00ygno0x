class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = len(arr) - 1
        maxval = arr[index]     # last element's value arr[5]

        for i in reversed(range(index)): # start from 5 thru 0 
            val = arr[i]        # store for later to compare 
            arr[i] = maxval 
            if val > maxval:
                maxval = val
        arr[index] = -1
        return arr