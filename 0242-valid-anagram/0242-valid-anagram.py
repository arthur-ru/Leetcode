class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # We create a hashmap containing the caracters and their number of iterations
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        for j in t:
            if j in hashmap:
        # We dicrease the counter
                hashmap[j] -= 1
        # If an element of t is not in s then it is not an anagram
            if j not in hashmap:
                return False
        # If each counter is equal to 0 then there is the same caracters in t and s
        for k in hashmap:
            if hashmap[k] != 0:
                return False
        return True