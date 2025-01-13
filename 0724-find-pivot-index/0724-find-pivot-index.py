class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum = 0
        rightsum = 0

        for i in range(len(nums)):
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i+1:])

            if leftsum == rightsum:
                return i
        
        return -1

        



