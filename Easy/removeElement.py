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

