import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(45) + ',' + str(52) + '}'
    sub_string = string[11:97]
    for match in re.findall(pattern, sub_string, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes