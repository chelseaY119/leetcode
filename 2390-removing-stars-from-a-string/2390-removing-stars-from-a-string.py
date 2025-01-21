class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [] # stack to store the output string
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        result = "".join(map(str, stack))
        return result
