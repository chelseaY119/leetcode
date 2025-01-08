class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
            
        small = float('inf') #smallest number
        middle = float('inf') # second smallest number

        for num in nums:
            if num <= small:
                small = num
            elif num <= middle:
                middle = num
            else:
                return True
        
        return False
                


        