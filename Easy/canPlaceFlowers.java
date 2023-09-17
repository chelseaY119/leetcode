package Easy;

// #605
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int plant = 0;
        int m = flowerbed.length;

        for (int i = 0; i < m; i++) {
            if (flowerbed[i] == 0) {
                int l = i == 0 ? 0 : flowerbed[i - 1];
                int r = i == m - 1 ? 0 : flowerbed[i + 1];

                if (l + r == 0) {
                    flowerbed[i] = 1;
                    plant++;
                }
            }

        }

        return plant >= n;
    }
}