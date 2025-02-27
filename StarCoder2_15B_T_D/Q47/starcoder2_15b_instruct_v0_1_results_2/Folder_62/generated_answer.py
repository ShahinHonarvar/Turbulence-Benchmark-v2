import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[26:88]
    pattern = '[A-Za-z]{' + str(52) + ',' + str(56) + '}'
    palindrome_matches = re.findall(pattern, substring, flags=re.IGNORECASE)
    for match in palindrome_matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes