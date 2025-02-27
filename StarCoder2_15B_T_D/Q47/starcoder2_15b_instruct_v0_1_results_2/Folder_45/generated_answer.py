import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[70:141]
    for length in range(3, 61):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                if re.match('^[a-zA-Z]+$', window):
                    palindromes.add(window)
    return palindromes