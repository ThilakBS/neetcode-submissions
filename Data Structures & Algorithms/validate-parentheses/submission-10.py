class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parendict = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in parendict:
                if stack and stack[-1] == parendict[i]:
                    stack.pop()
                else:
                    return False
            if i not in parendict:
                stack.append(i)
        
        return True if not stack else False


        
        