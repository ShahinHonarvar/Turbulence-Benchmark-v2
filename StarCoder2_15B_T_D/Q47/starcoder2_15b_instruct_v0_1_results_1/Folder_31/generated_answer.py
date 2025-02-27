import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(37) + ',' + str(60) + '}'
    regex = re.compile(pattern, re.IGNORECASE)
    palindromes = set()
    for match in regex.finditer(string[11:84]):
        palindromes.add(match.group().lower())
    return palindromes