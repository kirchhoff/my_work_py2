#coding=utf-8
class Solution(object):
    #朴素做法
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = bin(num)[2:]
        l = len(s)
        res  = []
        for i in xrange(l):
            if s[i] == '0':
                res.append('1')
            else:
                res.append('0')
        return int("".join(res),2)

class Solution2(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i<= num:
            i = i << 1
        #now we get i > num
        return (i-1) ^ num
        # for example:
        # 10000 - 1 = 01111
        # and then 1111 ^ 1001 =0110 -->6

if __name__ == '__main__':
    print Solution2().findComplement(9)