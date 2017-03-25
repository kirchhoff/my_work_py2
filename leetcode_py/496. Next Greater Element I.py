class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: list[int]
        :type nums: list[int]
        :rtype: list[int]
        """
        res = []
        for i in findNums:
            j = nums.index(i)
            flag = 1
            for k in nums[j:]:
                if k > i:
                    res.append(k)
                    flag = 0
                    break
            if flag == 1:
                res.append(-1)
        return res


if __name__ == '__main__':
    print Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
