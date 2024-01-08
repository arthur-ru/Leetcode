class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        h = {}
        for i in range(n):
            if nums[i] not in h:
                h[nums[i]] = 0
            h[nums[i]] += 1
        for j in range(k):
            max_index = max(h, key=h.get)
            ans.append(max_index)
            h[max_index] = 0
        return ans 
                