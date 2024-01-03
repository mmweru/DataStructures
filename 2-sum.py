# # # class Solution(object):
# # def twoSum(nums, target):
# #     """
# #     :type nums: List[int]
# #     :type target: int
# #     :rtype: List[int]
# #     """
# #     size = len(nums)
# #     i = 0
# #     j = 0
# #     output = []
# #     while i < size:
# #         while j < (size - 1):
# #             if (nums[i] + nums[j + 1]) == target:
# #                 output.append(i)
# #                 output.append(j + 1)
# #                 break
# #             j += 1
# #         i += 1
# #         return (output)
# #         break
# #
# #
# # nums = [2, 4, 5, 6, 7]
# # # solution = Solution()
# # print(twoSum(nums, 9))
# # # for i in range(size - 1):
# # #     for j in range(size - 1):
# #
# def merge(nums1, m, nums2, n):
#     """
#     :type nums1: List[int]
#     :type m: int
#     :type nums2: List[int]
#     :type n: int
#     :rtype: None Do not return anything, modify nums1 in-place instead.
#     """

# def merge(nums1, m, nums2, n):
#     for i in range(m, m + n):
#         nums1[i] = nums2[i - m]
#     nums1.sort()
#     return nums1
#
#
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# print(merge(nums1, m, nums2, n))

# def moveZeroes(nums):
#     empt = []
#     case = []
#     for i in nums:
#         if i != 0:
#             #nums.remove(i)
#             empt.append(i)
#     for ele in nums:
#         if ele not in empt:
#             case.append(ele)
#     nums = empt + case
#     return nums
#
# nums = [0,0, 1]
# print(moveZeroes(nums))




