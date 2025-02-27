import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[10:56]
    for length in range(3, 8):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes