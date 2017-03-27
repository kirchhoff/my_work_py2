#coding=utf-8
import string


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        k_v = {}
        t = [s.find(i) for i in string.ascii_letters if s.count(i) == 1]
        print t
        if t == []:
            return -1
        else:
            return min(t)  #最小的index


if __name__ == '__main__':
    print Solution().firstUniqChar("leetcode")
    print string.ascii_letters