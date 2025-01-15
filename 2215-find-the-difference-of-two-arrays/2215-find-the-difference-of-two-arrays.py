class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        answer_1 = {}
        answer_2 = {}

        for n1 in nums1:
            answer_1[n1] = answer_1.get(n1, 0) + 1
        
        for n2 in nums2:
            answer_2[n2] = answer_2.get(n2, 0) + 1

        unique_1 = [key for key in answer_1 if key not in answer_2]
        unique_2 = [key for key in answer_2 if key not in answer_1]  

        
        return [unique_1, unique_2]
            

