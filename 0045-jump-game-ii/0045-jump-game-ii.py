class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        left, right = 0, 0
        furthest = 0
        while right < len(nums) - 1:
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])
            left = right + 1
            right = furthest
            ans += 1
        return ans