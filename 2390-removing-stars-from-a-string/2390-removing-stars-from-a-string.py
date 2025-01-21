class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s) # length of the original string, used for loop
        stack = [] # stack to store the output string

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        
        result = "".join(map(str, stack))
        return result
