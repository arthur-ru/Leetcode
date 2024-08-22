class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count_paper = [0]*(n+1)

        for i in range(n):
            count_paper[min(citations[i],n)] += 1
        
        h = n
        current_paper = count_paper[n]
        while current_paper < h:
            h -= 1
            current_paper += count_paper[h]
        
        return h