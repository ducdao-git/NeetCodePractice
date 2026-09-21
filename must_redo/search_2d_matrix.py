class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid_row = (top + bot) // 2

            if top == bot:
                row = matrix[top]
                left, right = 0, len(row) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if row[mid] < target:
                        left = mid + 1
                    elif row[mid] > target:
                        right = mid - 1
                    else:
                        return True

                return False

            if matrix[mid_row][0] < target:
                if matrix[mid_row][-1] < target:
                    top = mid_row + 1
                else:
                    top = bot = mid_row
            elif matrix[mid_row][0] > target:
                bot = mid_row - 1
            else:
                return True

        return False


_matrix = [[1], [3]]
_target = 0
sol_test = Solution()
print(sol_test.searchMatrix(_matrix, _target))
