#coding=utf-8
import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: list[int]
        """
        # x^2=area
        x = math.sqrt(area)
        if int(x) == x:
            return [int(x), int(x)]
        x = int(x + 1)
        for i in xrange(x, 0, -1):
            temp = area / i
            if temp * i == area:
                return [max(temp, i), min(temp, i)]


class Solution2(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: list[int]
        """
        x = int(math.sqrt(area))
        while area % x != 0:
            x -= 1
            '''
            The worst scenario is when area is a huge prime number. So you always want to loop over the shorter side
            width instead of the longer side length, where width <= length.
            比如17 == 1*17
            sqrt(17)约等于4,显然便利[1~4]比较快得出结果，而[4-17]太长了
            '''
        return [area / x, x]


if __name__ == '__main__':
    print Solution().constructRectangle(3)
