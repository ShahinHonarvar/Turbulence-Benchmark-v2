import re

def palindromes_of_specific_lengths(string):
    substring = string[1:300]
    pattern = re.compile('[a-zA-Z]{3,10}')
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 11, len(substring))):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes