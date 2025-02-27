import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:201]
    pattern = re.compile('[a-zA-Z]{5,10}')
    for i in range(len(substring)):
        for j in range(i + 5, min(i + 11, len(substring) + 1)):
            substring_window = substring[i:j]
            if substring_window == substring_window[::-1]:
                palindromes.add(substring_window)
    return palindromes