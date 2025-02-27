import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(30) + ',' + str(46) + '}'
    matches = re.findall(pattern, string[26:85])
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes