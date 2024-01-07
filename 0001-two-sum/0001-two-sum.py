class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # We use a one way pass in the list: O(n)
        # Create a hashmap to improve efficiency
        n = len(nums)
        h = {}
        for i in range(n):
            # Instead of searching for two numbers, we are now searching for one
            ans = target - nums[i]
            if ans in h:
                return i,h[ans]
            # If we can't find an addition that fits, we add the number to the hashmap
            h[nums[i]] = i