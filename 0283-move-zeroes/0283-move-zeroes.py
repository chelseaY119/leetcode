class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = 0 # pointer to assign the position of each non-zero value
        j = 0 # pointer that scan through the whole loop

        while j < n:
            if nums[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                i +=1    
                j +=1
        
        while i < n:
            nums[i] = 0
            i +=1
        
            

                

        