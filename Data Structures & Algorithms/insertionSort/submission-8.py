# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        output = [] 
        output.append(pairs[:])
        for i in range(1, len(pairs)):  # i looping through the List 
            j = i - 1                   # j is left to i 
            while j >= 0 and (pairs[j].key > pairs[j+1].key):     # repeat until temp find right position 
                temp = pairs[j+1]       # temp = small value, need to find position 
                pairs[j+1] = pairs[j]
                pairs[j] = temp 
                j -= 1
            output.append(pairs[:])

                
        return output
            





        