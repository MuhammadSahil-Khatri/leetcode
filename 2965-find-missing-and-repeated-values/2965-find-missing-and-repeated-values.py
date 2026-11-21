class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n

        expected_sum = N * (N + 1) // 2
        expected_sq_sum = N * (N + 1) * (2 * N + 1) // 6

        actual_sum = 0
        actual_sq_sum = 0

        for row in grid:
            for num in row:
                actual_sum += num
                actual_sq_sum += num * num

        diff = actual_sum - expected_sum
        sq_diff = actual_sq_sum - expected_sq_sum

        sum_ab = sq_diff // diff

        repeated = (diff + sum_ab) // 2
        missing = sum_ab - repeated

        return [repeated, missing]
