class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0 # the left pointer
        n = len(height)
        j = n - 1 # right pointer
        max_area = 0

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area

    
        