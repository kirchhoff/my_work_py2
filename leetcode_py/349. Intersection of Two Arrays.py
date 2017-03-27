class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: list[int]
        :type nums2: list[int]
        :rtype: list[int]
        """
        return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    print Solution().intersection([1, 2, 2, 1], [2, 2])
