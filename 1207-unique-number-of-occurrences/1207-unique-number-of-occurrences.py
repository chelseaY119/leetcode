class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        check_map = {}

        for num in arr:
            check_map[num] = check_map.get(num, 0) + 1
        
        occurrence = list(check_map.values())

        return len(occurrence) == len(set(occurrence))
        