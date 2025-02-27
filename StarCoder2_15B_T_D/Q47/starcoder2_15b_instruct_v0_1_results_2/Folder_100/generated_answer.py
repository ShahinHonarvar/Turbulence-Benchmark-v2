import re

def palindromes_of_specific_lengths(string):
    substring = string[29:97]
    pattern = re.compile('[A-Za-z]{12,18}')
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 18, len(substring)) + 1):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes