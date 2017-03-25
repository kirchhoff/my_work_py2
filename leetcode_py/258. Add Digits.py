class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num % 10 != num:
            s = str(num)
            num = sum([int(x) for x in s])
        return  num

class Solution2(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        if num%9 == 0:
            return 9
        return num%9


if __name__ == '__main__':
    for i in xrange(20):
        print Solution2().addDigits(i)