import re

def palindromes_of_specific_lengths(string):
    regex = '[a-zA-Z]{' + str(23) + ',' + str(39) + '}'
    palindromes = set()
    for match in re.findall(regex, string[31:75]):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes