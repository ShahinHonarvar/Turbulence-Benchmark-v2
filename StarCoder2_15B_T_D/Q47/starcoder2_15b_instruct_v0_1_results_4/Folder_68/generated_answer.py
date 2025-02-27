import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    string_length = len(string)
    for i in range(string_length - 1):
        for j in range(i + 1, min(i + 101, string_length)):
            substring = string[i:j]
            if substring == substring[::-1]:
                if len(substring) >= 50 and len(substring) <= 100:
                    palindromes.add(substring)
    return palindromes