##################################
# ******** Write Code ******** #
##################################

def is_one_edit_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False

    if len(string1) < len(string2):
        tempString = string2
        string2 = string1
        string1 = tempString

    i, offset = 0, 0
    editted = False
    while i < len(string1) and i - offset < len(string2):
        if string1[i] == string2[i - offset]:
            i += 1
            continue

        if editted:
            return False
        editted = True
        if string1[i + 1] == string2[i]:
            offset = 1
            i += 2
        else:
            i += 1
    return editted or len(string1) != len(string2)
        

        
        

##################################
# ******** Testing Area ******** #
##################################


fn = is_one_edit_away
test_cases = [
    (["pale", "ple"], True),
    (["pales", "pale"], True),
    (["pale", "pales"], True),
    (["pale", "bale"], True),
    (["pale", "bake"], False),
    (["pale", "pale"], False),
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_results(test_input, expected):
    assert fn(*test_input) == expected
