import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    length_range = range(3, 5)
    substring = string[1:9]
    for length in length_range:
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                if re.match('^[a-zA-Z]+$', window):
                    palindromes.add(window)
    return palindromes