#coding=utf-8
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        n = len(nums)
        s = set(nums) #已出现的数字
        res = [i for i in xrange(1,n+1)]
        res = set(res)
        for i in s:
            res.remove(i)
        return list(res) # beats 92.6% 268ms


if __name__ == '__main__':
    print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])