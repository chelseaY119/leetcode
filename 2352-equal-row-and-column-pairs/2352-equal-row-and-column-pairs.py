class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        map_row = {}
        map_col = {}

        for r in grid:
            rc = tuple(r)
            map_row[rc] = map_row.get(rc, 0) + 1
        

        for c in zip(*grid):
            map_col[c] = map_col.get(c, 0) + 1

        count = 0

        for tpl in map_row:
            if tpl in map_col:
                count += map_row[tpl] * map_col[tpl]

        
        return count
        


        