# coding=utf-8
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT) #~((a % MIN_INT) ^ MAX_INT)


def count_one(n):
    """
    :type n:int
    :return: int
    1的个数
    """
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


def isPowerOfFour(n):
    return (not (n & (n - 1))) and (n & 0x55555555)


class Solution2(object):
    def getSum(self, a, b):
        if b == 0:
            return a
        return self.getSum(a ^ b, (a & b) << 1)


if __name__ == '__main__':
    print Solution().getSum(-1, -2)
