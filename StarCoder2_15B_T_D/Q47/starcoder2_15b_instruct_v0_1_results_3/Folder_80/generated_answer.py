import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(24) + ',' + str(33) + '}'
    substrings = re.findall(pattern, string[35:89])
    for substring in substrings:
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes