import re

def palindrome_of_length_n(string):
    """
    Finds all palindromes of length 83 as substrings of `string`.
    """
    pattern = '[a-zA-Z]{' + str(83) + '}'
    palindromes = set()
    for match in re.findall(pattern, string, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes