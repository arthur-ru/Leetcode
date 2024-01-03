class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        return max([points[k+1][0]-points[k][0] for k in range(len(points)-1)])
