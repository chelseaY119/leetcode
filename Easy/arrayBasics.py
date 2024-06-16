# array - related easy questions (very basic ones)


# # no. 27 remove element
class removeElement:
    # use two pointers, one fast and one slow
    def removeElement(self, nums, val):
        """
        :params nums: List[int]
        :params val: int
        :return: int
        """

        slowIndex = 0
        fastIndex = 0

        while fastIndex < len(nums):
            if nums[fastIndex] == val:
                fastIndex += 1
            else:
                nums[slowIndex] = nums[fastIndex]
                # print("slow after", nums[slowIndex])
                fastIndex += 1
                slowIndex += 1

        nums = nums[0:slowIndex]
        print(nums)

        return slowIndex


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


ss = sortedSquares()
result = ss.solution([-4, -3, 0, 3, 10])
print(result)
