package Easy;

//#1768. Merge Alternative Strings
class Solution {

    public String mergeAlternatively(String w1, String w2) {

        int l1 = w1.length();
        int l2 = w2.length();

        int min = Math.min(l1, l2);

        String longer = "";

        if (l1 == min) {
            longer = w1;
        } else if (l2 == min) {
            longer = w2;
        }

        char[] char1 = w1.toCharArray();
        char[] char2 = w2.toCharArray();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < min; i++) {
            sb.append(char1[i]);
            sb.append(char2[i]);
        }

        sb.append(longer.substring(min));

        return sb.toString();

    }

}
