class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 

        n = len(nums)
        left = 0
        longest_array = 0
        zeros = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            longest_array = max(longest_array, right - left)
        
        return longest_array