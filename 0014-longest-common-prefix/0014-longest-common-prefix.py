class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
        n = len(strs)
        m = len(min(strs, key=len))
        i = 0
        for l in range(m):
            for k in range(n-1):
                if strs[k][i] != strs[k+1][i]:
                    return common
            common = common + strs[0][i]
            i += 1
        return common