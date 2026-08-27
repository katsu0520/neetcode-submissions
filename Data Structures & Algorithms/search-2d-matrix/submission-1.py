class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        target_row = -1
        for i in range(rows):
            if target <= matrix[i][cols-1]:
                target_row = i
                break
        if target_row == -1:
            return False
        l = 0
        r = cols -1
        while l <= r:
            m = (l+r)//2
            if target < matrix[target_row][m]:
                r=m-1
            elif target == matrix[target_row][m]:
                return True
            else:
                l = m+1
        return False

        