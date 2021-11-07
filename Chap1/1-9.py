##################################
# ******** Write Code ******** #
##################################

def is_substring(s1, s2):
    return s1 in s2

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    concat = s2 + s2
    return is_substring(s1, concat)
        

##################################
# ******** Testing Area ******** #
##################################


fn = is_rotation
test_cases = [
    (["waterbottle", "erbottlewat"], True),
    (["waterbottle", "erbottlewet"], False),
    (["erbottlewat", "waterbottle"], True),
    (["waterbottle", "erbowet"], False),
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_results(test_input, expected):
    if isinstance(test_input, list):
        assert fn(*test_input) == expected
    else:
        assert fn(test_input) == expected
