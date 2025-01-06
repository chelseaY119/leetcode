# no 977 sorted array square
class sortedSquares:
    def solution(self, nums):
        """
        :type nums: a list of sorted int nums
        :return: sorted array that has the squares nums
        """
        left = 0
        right = len(nums) - 1
        k = right
        result = [0] * (k + 1)

        while left <= right:
            if nums[right] * nums[right] > nums[left] * nums[left]:
                result[k] = nums[right] * nums[right]
                right -= 1
            elif nums[right] * nums[right] <= nums[left] * nums[left]:
                result[k] = nums[left] * nums[left]
                left += 1
            k -= 1

        return result
