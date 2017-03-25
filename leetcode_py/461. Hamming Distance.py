#coding=utf-8
'''
题目中解释的很清楚了，两个数字之间的汉明距离就是其二进制数对应位不同的个数，那么最直接了当的做法就是按位分别取出两个数对应位上的数并异或，
我们知道异或的性质上相同的为0，不同的为1，我们只要把为1的情况累加起来就是汉明距离了
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s = bin(x^y)[2:]
        count = 0
        for i in s:
            if i == '1':
                count += 1
        return count

class Solution2(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        exc = x ^ y
        while exc > 0:
            exc = exc & (exc-1) #移除最后一个1
            count+=1

        return count


if __name__ == '__main__':
    print Solution().hammingDistance(1,4)
    print Solution2().hammingDistance(1,4)