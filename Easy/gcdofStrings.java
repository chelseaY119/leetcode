package Easy;

//#1071 
class Solution {

    private int getGCD(int i, int j) {

        while (j != 0) {
            int temp = j;
            j = i % j;
            i = temp;
        }

        return i;
    }

    public String gcdofStrings(String s1, String s2) {

        String divider = "";
        if (!(s1 + s2).equals(s2 + s1)) {
            return divider;
        }

        int gcd = getGCD(s1.length(), s2.length());

        divider = s1.substring(0, gcd);

        return divider;
    }
}