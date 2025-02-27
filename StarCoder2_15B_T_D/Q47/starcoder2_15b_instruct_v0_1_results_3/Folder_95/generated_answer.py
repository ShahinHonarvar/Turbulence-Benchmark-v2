import re

def palindromes_of_specific_lengths(string):
    substring = string[12:57]
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(substring) - length + 1):
            substring_to_check = substring[i:i + length]
            if substring_to_check.lower() == substring_to_check[::-1].lower():
                palindromes.add(substring_to_check)
    return palindromes