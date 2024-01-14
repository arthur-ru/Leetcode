class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = {")":"(", "]":"[", "}":"{"}
        stack = ""
        for i in s:
            if i in h:
                if len(stack) == 0 or stack[-1] != h[i]:
                    return False
                else:
                    stack = stack[:-1]
            else:
                stack += i
        return len(stack) == 0