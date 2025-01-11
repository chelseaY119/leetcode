class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0

        while i < j:
            sum = nums[i] + nums[j]
            if sum > k :
                j -= 1
            elif sum == k:
                count += 1
                i += 1
                j -= 1
            else:
                i += 1
        
        return count

        
        