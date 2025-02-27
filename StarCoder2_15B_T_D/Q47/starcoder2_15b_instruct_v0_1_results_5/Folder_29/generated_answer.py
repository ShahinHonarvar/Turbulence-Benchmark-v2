import re

def palindromes_of_specific_lengths(string):
    substring = string[15:95]
    pattern = re.compile('[a-zA-Z]{18,73}')
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if substring[i:j] == substring[i:j][::-1]:
                if pattern.match(substring[i:j]):
                    palindromes.add(substring[i:j])
    return palindromes