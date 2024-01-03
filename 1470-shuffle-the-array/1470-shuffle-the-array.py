class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for k in range(len(nums)/2):
            ans.append(nums[k])
            ans.append(nums[k+len(nums)/2])
        return ans