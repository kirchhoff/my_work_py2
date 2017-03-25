class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: list[str]
        """
        res = []
        for i in xrange(1,n+1):
            if i%15 ==0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 ==0:
                res.append("Buzz")
            else:
                res.append(i)
        return res
if __name__ == '__main__':
    print Solution().fizzBuzz(15)