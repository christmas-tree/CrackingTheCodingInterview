##################################
# ******** Write Code ******** #
##################################

def palindrome_permutation(string):
    charCount = dict()
    for char in string:
        if char == ' ':
            continue
        count = charCount.get(char, 0)
        charCount[char] = count + 1
    
    isOdd = False
    for count in charCount.values():
        if count % 2 == 0:
            continue

        if isOdd:
            return False
        
        isOdd = True
    return True

##################################
# ******** Testing Area ******** #
##################################


fn = palindrome_permutation
test_cases = [
    (["tact coa",], True),
    (["tact col",], False),
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_results(test_input, expected):
    assert fn(*test_input) == expected
