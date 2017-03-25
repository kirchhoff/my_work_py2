class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        r = 0
        row = len(grid)
        column = len(grid[0])
        for i in xrange(row):
            for j in xrange(column):
                if grid[i][j] == 1:
                    count = 4
                    if 0 <= i - 1 < row and 0 <= j < column and grid[i - 1][j] == 1:
                        count -= 1
                    if 0 <= i + 1 < row and 0 <= j < column and grid[i + 1][j] == 1:
                        count -= 1
                    if 0 <= i < row and 0 <= j - 1 < column and grid[i][j - 1] == 1:
                        count -= 1
                    if 0 <= i < row and 0 <= j + 1 < column and grid[i][j + 1] == 1:
                        count -= 1

                    r += count
        return r


if __name__ == '__main__':
    print Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
