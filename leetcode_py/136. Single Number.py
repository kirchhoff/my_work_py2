# coding=utf-8
import operator


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)  # 66ms 28.32%


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)  # 45ms 90.8%


if __name__ == '__main__':

    print Solution().singleNumber([1, 2, 3, 2, 1, 3, 4, 5, 5, 6, 8, 8, 6])



