class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        highest_alt = 0
        current_alt = 0

        for i in range(len(gain)):
            current_alt = current_alt + gain[i]
            highest_alt = max (highest_alt, current_alt)
        
        return highest_alt

        