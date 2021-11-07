##################################
# ******** Write Code ******** #
##################################

def checkPermutation(string, subString):
    if len(string) != len(subString):
        return False
    charCount = dict()
    for char in string:
        count = charCount.get(char, 0)
        charCount[char] = count + 1

    for char in subString:
        count = charCount.get(char, 0)
        if count <= 0:
            return False
        charCount[char] = count - 1
    return True



##################################
# ******** Testing Area ******** #
##################################


fn = checkPermutation
test_cases = [
    (["FirstThirdSecond", "SecondFirstThird"], True),
    (["SecondFirstThird", "SecondFirstThirdss"], False),
    (["SecondFirstThird", "SecondFirStThird"], False),
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_1(test_input, expected):
    assert fn(*test_input) == expected
