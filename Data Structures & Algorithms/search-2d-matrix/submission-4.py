class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows-1
        while top <= bottom:
            m = (top+bottom)//2
            if target > matrix[m][cols-1]:
                top = m+1
            elif target < matrix[m][0]:
                bottom = m-1
            else:
                target_row = m
                break
        else:
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