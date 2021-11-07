##################################
# ******** Write Code ******** #
##################################

# With data structure

def hasUniqueCharacters(string):
    charSet = set()
    for char in string:
        if char in charSet:
            return False
        charSet.add(char)
    return True


# Without data structure
def hasUniqueCharactersWithoutDs(string):
    sorted = list(string)
    sorted.sort()
    for i in range(len(sorted) - 1):
        if sorted[i] == sorted[i+1]:
            return False
    return True


##################################
# ******** Testing Area ******** #
##################################


fn = hasUniqueCharactersWithoutDs
test_cases = [
    (["abcdef"], True),
    (["aaaaaaaaaaa"], False),
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_1(test_input, expected):
    assert fn(*test_input) == expected
