# 704. binary search
class binarySearch:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :return: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] == target:
                return middle

        return -1