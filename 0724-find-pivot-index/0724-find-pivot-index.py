class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        totalsum = sum(nums) # total sum
        leftsum = 0

        for i in range(len(nums)):
            # leftsum vs rightsum (totalsum - leftsum - current number)
            if leftsum == totalsum - leftsum - nums[i]:
                return i
            leftsum += nums[i]

        return -1

        




        



