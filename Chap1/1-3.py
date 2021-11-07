##################################
# ******** Write Code ******** #
##################################

def urlify(url):
    url = list(url)
    i = len(url) - 1
    j = i

    while url[i] == ' ':
        i -= 1

    while (i >= 0):
        if url[i] == ' ':
            url[j-2] = '%'
            url[j-1] = '2'
            url[j] = '0'
            j -= 3
        else:
            url[j] = url[i]
            j -= 1
        i -= 1
    
    # Convert to string
    newUrl = ""
    for char in url:
        newUrl += char
    return newUrl


##################################
# ******** Testing Area ******** #
##################################


fn = urlify
test_cases = [
    (["Mr John Smith    ",], "Mr%20John%20Smith",),
]

import pytest
@pytest.mark.parametrize("test_input,expected", test_cases)
def test_1(test_input, expected):
    assert fn(*test_input) == expected
