import re

def palindromes_of_specific_lengths(string):
    substring = string[23:78]
    pattern = re.compile('[a-zA-Z]{13,40}')
    palindromes = set()
    for length in range(13, 41):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes