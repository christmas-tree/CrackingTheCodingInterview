##################################
# ******** Write Code ******** #
##################################

def rotate_matrix(img):
    if not img or len(img) == 0:
        return
    
    n = len(img)

    for i in range(n):
        for j in range(i):
            tmp = img[i][j]
            img[i][j] = img[j][i]
            img[j][i] = tmp
    
    for i in range(n):
        for j in range(n // 2):
            tmp = img[i][j]
            img[i][j] = img[i][n-j-1]
            img[i][n-j-1] = tmp
    return img

##################################
# ******** Testing Area ******** #
##################################

test_cases = [
    (
        [
            [1, 4, 2, 3],
            [6, 2, 10, 7],
            [1, 5, 2, 1],
            [9, 0, 6, 3],
        ], 
        [
            [9, 1, 6, 1],
            [0, 5, 2, 4],
            [6, 2, 10, 2],
            [3, 1, 7, 3],
        ], 
    )
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_results(test_input, expected):
    correct = True
    result = rotate_matrix(test_input)
    for i, row in enumerate(result):
        for j, val in enumerate(row):
            correct = correct and expected[i][j] == val

    assert correct
