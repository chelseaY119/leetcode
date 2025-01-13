class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = set('aeiou') #vowels
        n = len(s)

        current_vowel = sum(1 for i in range(k) if s[i] in vowels)
        max_vowel = current_vowel

        for i in range (k, n):
            if s[i - k] in vowels:
                current_vowel -= 1
            if s[i] in vowels:
                current_vowel += 1
            
            max_vowel = max(max_vowel, current_vowel)

        return max_vowel




