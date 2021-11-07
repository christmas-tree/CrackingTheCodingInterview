##################################
# ******** Write Code ******** #
##################################

def compress_string(string):
    if not string:
        return ""

    result = ""
    count = 0
    cur_letter = "a"

    for letter in string:
        if letter == cur_letter:
            count += 1
            continue
        if count != 0:
            result += cur_letter + str(count)
        cur_letter = letter
        count = 1
    
    if count != 0:
        result += cur_letter + str(count)

    if len(result) > len(string):
        return string
    return result
        

##################################
# ******** Testing Area ******** #
##################################


fn = compress_string
test_cases = [
    ("aaaabbbbccdddd", "a4b4c2d4"),
    ("abc", "abc"),
    ("aabcccccaaa", "a2b1c5a3"),
    ("a", "a"),
    ("", ""),
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_results(test_input, expected):
    if isinstance(test_input, list):
        assert fn(*test_input) == expected
    else:
        assert fn(test_input) == expected
