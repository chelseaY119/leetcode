package Easy;

// #345 two pointer approach
class Solution {

    public String reverseVowels(String s) {

        String vowel = "aeiouAEIOU";

        // acsii code for char: from 0 to 127
        boolean[] vowels = new boolean[128];

        for (char c : vowel.toCharArray()) {
            vowels[c] = true;
        }

        int length = s.length();
        int left = 0;
        int right = length - 1;

        char[] charstring = s.toCharArray();

        while (left < right) {

            while (left < right && !vowels[charstring[left]]) {
                left++;
            }

            while (left < right && !vowels[charstring[right]]) {
                right--;
            }

            if (left < right) {
                char temp = s.charAt(right);

                charstring[right] = s.charAt(left);
                charstring[left] = temp;
                left++;
                right--;
            }
        }

        return new String(charstring);

    }

}