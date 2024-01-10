import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        n = len(s)
        point1, point2 = 0, n-1
        for k in range(n//2):
            if s[point1] != s[point2]:
                return False
            point1 += 1
            point2 -= 1
        return True