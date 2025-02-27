import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[63:71]
    regex = re.compile('[a-zA-Z]{4,5}')
    for i in range(len(substring)):
        for j in range(i + 4, min(i + 6, len(substring))):
            window = substring[i:j]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes