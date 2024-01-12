class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        h = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        symbols = "MDCLXVI"
        var = num
        roman, i = "", 0
        while i < len(h):
            if i%2 == 1 and var//h[symbols[i+1]] == 9:
                roman += symbols[i+1] + symbols[i-1]
                i += 1
            elif i%2 == 0 and var//h[symbols[i]] == 4:
                roman += symbols[i] + symbols[i-1]
            else:
                var = var//h[symbols[i]]
                roman = roman + symbols[i] * var
            var = num%h[symbols[i]]
            i += 1
        return roman