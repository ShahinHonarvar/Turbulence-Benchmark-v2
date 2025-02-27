import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[23:95]
    pattern = re.compile('[a-zA-Z]{17,55}')
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if substring[i:j] == substring[i:j][::-1]:
                if pattern.match(substring[i:j]):
                    palindromes.add(substring[i:j])
    return palindromes