class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = [] # keep track of previous strings and counts
        num = 0
        string = ""

        for char in s:
            if char.isdigit(): # found the repeat number
                num = int(char) # convert char to number
            elif char == "[":
                stack.append((string, num)) # store number and string onto stack
                num = 0
                string = ""
            elif char == "]":
                prev, count = stack.pop()
                string = prev + string * count
            else:
                string += char
        
        return string


                






        