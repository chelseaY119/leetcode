# array - related medium questions


# no.209 minimum sized sub array
class minSubArray(object):
    def solution(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        pA = 0
        pB = 0
        minlen = 0
        sum = nums[pA]

        while pB < len(nums):
            if sum < target:
                if pB == len(nums) - 1:
                    break
                pB += 1
                sum += nums[pB]
            elif sum >= target:
                if minlen != 0:
                    minlen = min(minlen, pB - pA + 1)
                else:
                    minlen = pB - pA + 1
                sum -= nums[pA]
                pA += 1

        return minlen
