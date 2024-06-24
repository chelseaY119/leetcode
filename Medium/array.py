# array - related medium questions


# no.209 minimum sized sub array
# class minSubArray(object):
#     def solution(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         pA = 0
#         pB = 0
#         minlen = 0
#         sum = nums[pA]

#         while pB < len(nums):
#             if sum < target:
#                 if pB == len(nums) - 1:
#                     break
#                 pB += 1
#                 sum += nums[pB]
#             elif sum >= target:
#                 if minlen != 0:
#                     minlen = min(minlen, pB - pA + 1)
#                 else:
#                     minlen = pB - pA + 1
#                 sum -= nums[pA]
#                 pA += 1

#         return minlen

print(int(5 / 2))


# no. 59 spiral matrix
class spiralMatrix2(object):
    def generateMatrix(self, n):

        startIndex = 0
        endIndex = n - 1
        loop = int(n / 2)
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        count = 0

        while loop > 0:
            i = startIndex
            j = startIndex

            while j < endIndex:
                count += 1
                matrix[i][j] = count
                j += 1

            while i < endIndex:
                count += 1
                matrix[i][j] = count
                i += 1

            while j > startIndex:
                count += 1
                matrix[i][j] = count
                j -= 1

            while i > startIndex:
                count += 1
                matrix[i][j] = count
                i -= 1

            loop -= 1
            startIndex += 1
            endIndex -= 1

        if n % 2 != 0:
            middleIndex = int((n - 1) / 2)
            count += 1
            matrix[middleIndex][middleIndex] = count

        return matrix
