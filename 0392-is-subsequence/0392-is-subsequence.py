class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 1:
            return s[0] in t 
        
        i = 0 #pointer for s
        j = 0 #pointer for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

            if j >= len(t):
                break

        return i == len(s)


        




        