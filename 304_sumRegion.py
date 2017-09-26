class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.sum_matrix = []
            return
        self.sum_matrix = matrix[:]
        for j in range(1, len(matrix[0])):
            self.sum_matrix[0][j] = self.sum_matrix[0][j - 1] + matrix[0][j]
        for i in range(1, len(matrix)):
            self.sum_matrix[i][0] = self.sum_matrix[i - 1][0] + matrix[i][0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.sum_matrix[i][j] = self.sum_matrix[i - 1][j] + self.sum_matrix[i][j - 1] - self.sum_matrix[i - 1][j - 1] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.sum_matrix == []:
            return 0
        return self.sum_matrix[row2][col2] - (row1 > 0) * self.sum_matrix[row1 - 1][col2] - (col1 > 0) * self.sum_matrix[row2][col1 - 1] + (row1 > 0 and col1 > 0) * self.sum_matrix[row1 - 1][col1 - 1]
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    given_mat = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
    ]

    num_mat = NumMatrix(given_mat)
    print(num_mat.sumRegion(2, 1, 4, 3))
    print(num_mat.sumRegion(1, 1, 2, 2))
    print(num_mat.sumRegion(1, 2, 2, 4))