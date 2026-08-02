class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        # Finding the tagest in a row
        def searchRow(row):
            st, end = 0, c-1
            while st <= end:
                mid = st + (end - st)//2
                if matrix[row][mid] == target:
                    return True
                elif target < matrix[row][mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            
            return False



        # Finding the Row
        st, end = 0, r-1
        while st <= end:
            mid = st + (end - st)//2

            if matrix[mid][0] <= target <= matrix[mid][c-1]:
                return searchRow(mid)
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                st = mid + 1

        return False
