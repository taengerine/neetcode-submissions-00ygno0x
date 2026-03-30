class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        match = { ")" : "(",  "}" : "{",  "]" : "[" }

        for bracket in s:           # iterate input array 
            if bracket not in match :           # if its opening => 
                stack.append(bracket)               # store opening parenthese in stack 

            else:                               # else its closing => 
                if not stack:                       # check if stack = empty 
                    return False                    
                elif match[bracket] != stack[-1]:          # check if closing matches stack 
                    return False
                else:
                    stack.pop()
            
        if not stack: 
            return True
        else:
            return False