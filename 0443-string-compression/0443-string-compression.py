class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        n = len(chars)
        i = 0 # writer
        j = 0 # reader

        while j < n:
            char = chars[j]
            count = 0

            # consecutive letters
            while j < n and chars[j] == char:
                j += 1
                count += 1

            # writer the char to the input array in the correct position
            chars[i] = char
            i += 1

            if count > 1:
                # if length more than 10, split into multiple characters
                for d in str(count):
                    chars[i] = d
                    i += 1
        
        return i



                




        