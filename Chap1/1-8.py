##################################
# ******** Write Code ******** #
##################################

# O(n) space needed
# def mark_zero_col(mat, col_num):
#     for i in range(len(mat)):
#         mat[i][col_num] = 0

# def mark_zero_row(mat, row_num):
#     for i in range(len(mat[row_num])):
#         mat[row_num][i] = 0

# def zero_matrix(mat):
#     rows = set()
#     cols = set()
#     for i, row in enumerate(mat):
#         for j, val in enumerate(row):
#             if val == 0:
#                 rows.add(i)
#                 cols.add(j)
    
#     for row_num in rows:
#         mark_zero_row(mat, row_num)
    
#     for col_num in rows:
#         mark_zero_col(mat, col_num)
    
#     return mat

# O(1) space needed
def zero_matrix(mat):
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if val == 0:
                row[0] = 0
                mat[0][j] = 0
    
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if mat[0][j] == 0 or mat[i][0] == 0:
                mat[i][j] = 0

    return mat

##################################
# ******** Testing Area ******** #
##################################

test_cases = [
    (
        [
            [1, 4, 2, 3],
            [6, 0, 10, 7],
            [1, 5, 2, 1],
            [9, 0, 6, 0],
        ], 
        [
            [1, 0, 2, 0],
            [0, 0, 0, 0],
            [1, 0, 2, 0],
            [0, 0, 0, 0],
        ],  
    )
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_results(test_input, expected):
    correct = True
    result = zero_matrix(test_input)
    for i, row in enumerate(result):
        for j, val in enumerate(row):
            correct = correct and expected[i][j] == val

    assert correct
