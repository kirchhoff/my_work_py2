class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: list[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j= 0, 0
        l = len(nums)
        while i < l:
            if nums[i] == 0:
                j=i+1
                while j < l:
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
                    j+=1
            i+=1



if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print nums