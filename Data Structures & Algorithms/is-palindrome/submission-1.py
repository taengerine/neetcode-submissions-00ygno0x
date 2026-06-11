import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r"[^a-zA-Z0-9]"
        result = re.sub(regex, "", s).lower()
        L, R = 0, len(result) - 1

        while L < R:
            if result[L] != result[R]: return False
            L += 1
            R -= 1
        
        return True 

