package Medium;

// 151
class Solution {

    public String reverseWords(String s) {

        String trimmedString = s.trim();
        String[] origin = trimmedString.split("\\s+");
        String[] newStrings = new String[origin.length];

        int left = 0;
        int right = newStrings.length - 1;

        while (left <= right) {
            String temp = origin[left];
            newStrings[right] = temp;
            newStrings[left] = origin[right];
            left++;
            right--;

            if (left == right) {
                newStrings[right] = origin[right];
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < origin.length; i++) {
            sb.append(newStrings[i]);
            if (i != (origin.length - 1)) {
                sb.append(" ");
            }
        }

        return sb.toString();

    }

}
