class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        highest_alt = 0
        current_alt = 0
        n = len(gain)

        for i in range(n):
            current_alt += gain[i]
            highest_alt = max (highest_alt, current_alt)
        
        return highest_alt

        