import re

def palindromes_of_specific_lengths(string):
    regex = '[a-zA-Z]{' + str(42) + ',' + str(77) + '}'
    matches = re.findall(regex, string[12:93], flags=re.IGNORECASE)
    palindromes = set((match for match in matches if match == match[::-1]))
    return palindromes