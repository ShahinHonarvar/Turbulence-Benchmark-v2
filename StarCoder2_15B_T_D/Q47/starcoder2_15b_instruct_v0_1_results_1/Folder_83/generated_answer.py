import re

def palindromes_of_specific_lengths(string):
    sub_string = string[75:96]
    pattern = '[a-zA-Z]{' + str(7) + ',' + str(9) + '}'
    matches = re.findall(pattern, sub_string, flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes