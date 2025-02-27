import re

def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[127:289]
    pattern = '[a-zA-Z]{' + str(119) + ',' + str(141) + '}'
    for match in re.findall(pattern, substring, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes