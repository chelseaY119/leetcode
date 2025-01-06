class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        output = [1] * n
        prefix = postfix = 1

        #prefix computation:
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        #postfix computation
        for i in range(n-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output
 

        