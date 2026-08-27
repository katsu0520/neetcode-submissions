class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows-1
        while top <= bottom:
            mid_row = (top+bottom)//2
            if target > matrix[mid_row][cols-1]:
                top = mid_row+1
            elif target < matrix[mid_row][0]:
                bottom = mid_row-1
            else:
                target_row = mid_row
                break
        else:
            return False    
        l = 0
        r = cols -1
        while l <= r:
            mid_col = (l+r)//2
            if target < matrix[target_row][mid_col]:
                r=mid_col-1
            elif target == matrix[target_row][mid_col]:
                return True
            else:
                l = mid_col+1
        return False