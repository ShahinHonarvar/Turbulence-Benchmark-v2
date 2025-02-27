import re

def palindromes_of_specific_lengths(s):
    index_range = s[101:293]
    palindromes = set()
    for length in range(154, 183):
        for i in range(len(index_range) - length + 1):
            substring = index_range[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes