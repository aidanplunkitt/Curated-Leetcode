# https://leetcode.com/problems/rotate-image/submissions/
# O(n^2) time, O(1) space

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose, then reverse each row
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
