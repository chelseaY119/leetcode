class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        n = len(nums)
        current_sum = sum(nums[:k])
        max_total = current_sum

        for i in range(k, n):
            current_sum = current_sum + nums[i] - nums[i - k]
            if current_sum > max_total:
                max_total = current_sum
        
        return float(max_total) / k
            


        