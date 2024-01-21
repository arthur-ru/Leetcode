class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a, b = 0, len(nums)
        k = 0
        while k < len(nums)//2 + 1:
            if nums[(a+b)//2] == target:
                return (a+b)//2
            elif nums[(a+b)//2] < target:
                a = (a+b)//2
            elif nums[(a+b)//2] > target:
                b = (a+b)//2
            k += 1
        return -1