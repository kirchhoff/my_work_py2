# coding=utf-8
from timeit import timeit

import operator


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        mmax = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > mmax:
                    mmax = count
                count = 0
        if count > mmax:
            mmax = count

        return mmax


class Solution2(object):
    def findMaxConsecutiveOnes(self, nums):
        return max(map(len, ''.join(map(str, nums)).split('0')))  # 效率低一点，但是比较另类


if __name__ == '__main__':
    print timeit(lambda: [Solution2().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])], number=1)
    print map(operator.mul, [1, 2, 3], [4, 5, 6])
