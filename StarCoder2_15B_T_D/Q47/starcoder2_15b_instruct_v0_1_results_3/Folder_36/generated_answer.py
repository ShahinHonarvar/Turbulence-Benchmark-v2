import re

def palindromes_of_specific_lengths(string):
    substring = string[124:284]
    regex = '[a-zA-Z]{' + str(115) + ',' + str(134) + '}'
    palindromes = set(re.findall(regex, substring, re.IGNORECASE))
    return palindromes