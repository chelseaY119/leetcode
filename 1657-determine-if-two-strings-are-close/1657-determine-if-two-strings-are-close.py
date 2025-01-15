class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        word1_map = {}
        word2_map = {}

        # return false if the length of two words is different 
        if len(word1) != len(word2):
            return False

        for char in word1:
            word1_map[char] = word1_map.get(char, 0) + 1
        
        for char in word2:
            word2_map[char] = word2_map.get(char, 0) + 1
        
        if set(word1_map.keys()) != set(word2_map.keys()):
            return False
        
        if sorted(word1_map.values()) != sorted(word2_map.values()):
            return False
        
        return True