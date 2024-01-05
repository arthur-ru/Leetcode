class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # We first sort the array
        # This way if the list contains duplicates they will be to each other
        nums.sort()
        # We check duplicates
        for k in range(1,len(nums)):
            if nums[k] == nums[k-1]:
                return True
        return False