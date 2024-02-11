class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, max_water = 0, len(height)-1, 0
        while l < r:
            max_water = max(min(height[l], height[r])*(r-l), max_water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water