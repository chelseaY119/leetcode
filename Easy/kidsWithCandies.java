package Easy;

import java.util.List;
import java.util.ArrayList;

// #1431
class Solution {

    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        List<Boolean> re = new ArrayList<Boolean>(candies.length);
        for (int i = 0; i < candies.length; i++) {
            re.add(true);
        }
        int Max = findMinMax(candies);

        for (int i = 0; i < candies.length; i++) {
            if (Max - candies[i] > extraCandies) {
                re.set(i, false);
            }
        }
        return re;
    }

    private int findMinMax(int[] intArray) {
        int max = intArray[0];
        for (int i = 0; i < intArray.length; i++) {
            if (intArray[i] > max) {
                max = intArray[i];
            }
        }
        return max;
    }
}
