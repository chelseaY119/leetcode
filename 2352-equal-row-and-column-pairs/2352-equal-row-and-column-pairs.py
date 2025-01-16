class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        map_row = {}
        map_col = {}

        n = len(grid)

        for row in range(n):
            map_row[row] = tuple(grid[row])

        for col in range(n):
            map_col[col] = tuple(grid[row][col] for row in range(n))

        count = 0

        for row in map_row.values():
            for col in map_col.values():
                if row == col:
                    count += 1
        

        return count
        


        