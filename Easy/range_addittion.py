def maxCount(m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_row, min_col = m, n
        for op in ops:
                ai, bi = op
                min_row = min(min_row, ai)
                min_col = min(min_col, bi)


        return min_row*min_col              



if __name__ == "__main__":
     print(maxCount(3,3,[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))