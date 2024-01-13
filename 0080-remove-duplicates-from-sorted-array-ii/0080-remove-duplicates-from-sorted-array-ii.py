class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, k = len(nums), 0
        # Hashmap usage to reduce complexity
        h = {}
        for i in range(n):
            # Create the hash key if it isn't already in the hashmap
            if nums[i] not in h:
                h[nums[i]] = 0
            h[nums[i]] += 1
            # Check if the value isn't already twice in nums
            if h[nums[i]] <= 2:
                nums[k] = nums[i]
                k += 1
        return k