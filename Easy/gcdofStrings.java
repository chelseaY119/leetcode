// package Easy;

// //#1071 
// class Solution {
//     public String gcdofString(String s1, String s2) {

//         String divider = "";

//         // if two strings has the same length : check if they are the same,
//         // if not, return empty string
//         if (s1.length() == s2.length()) {
//             if (s1.equals(s2)) {
//                 divider = s1;
//             }
//         }

//         else {
//             int l1 = s1.length();
//             int l2 = s2.length();
//             String longStr = (l1 > l2) ? s1 : s2;
//             String shortStr = (l1 > l2) ? s2 : s1;
//             char[] longChar = longStr.toCharArray();
//             char[] shortChar = shortStr.toCharArray();

//             StringBuilder sb = new StringBuilder();
//             int time = longChar.length / shortChar.length;
//             for (int j = 0; j < shortChar.length; j++) {
//                 for (int i = 0; i < time; i++) {
//                     if (longChar[i * shortChar.length + j] == shortChar[j]) {

//                     }
//                 }
//             }

//             divider = sb.toString();
//         }

//         return divider;

//     }
// }

package Easy;

//#1071 
class Solution {
    public String gcdofString(String s1, String s2) {

        String divider = "";
        int l1 = s1.length();
        int l2 = s2.length();

        if (l1 == l2) {
            if (!s1.equals(s2)) {
                return divider;
            }
        }

        String longStr = (l1 > l2) ? s1 : s2;
        String shortStr = (l1 > l2) ? s2 : s1;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < shortStr.length(); i++) {

            while (longStr.charAt(i) == shortStr.charAt(i)) {
                sb.append(shortStr.charAt(i));
            }

        }

        return divider;
    }
}