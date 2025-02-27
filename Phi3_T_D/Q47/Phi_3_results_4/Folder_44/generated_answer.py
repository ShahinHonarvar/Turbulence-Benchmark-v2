import re

def palindromes_of_specific_lengths(s):
    substring = s[18:99]
    palindromes = set()
    for length in range(31, 52):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].isalpha():
                substr = substring[i:i + length]
                substr_lower = substr.lower()
                if substr_lower == substr_lower[::-1]:
                    palindromes.add(substr_lower)
    return palindromes