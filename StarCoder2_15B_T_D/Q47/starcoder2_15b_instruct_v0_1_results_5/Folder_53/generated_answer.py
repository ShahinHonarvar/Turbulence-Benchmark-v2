import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[1:300]
    for length in range(3, 11):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1]:
                if re.match('^[a-zA-Z]+$', window):
                    palindromes.add(window)
    return palindromes