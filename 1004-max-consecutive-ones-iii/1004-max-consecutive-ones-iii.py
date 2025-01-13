class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        max_consecutive = 0
        zeros = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_consecutive = max(max_consecutive, right - left + 1)
        
        return max_consecutive
                
     