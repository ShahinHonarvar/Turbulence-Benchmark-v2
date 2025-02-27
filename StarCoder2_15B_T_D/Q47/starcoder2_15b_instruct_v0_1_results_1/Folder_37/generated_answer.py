import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    regex = '[a-zA-Z]{' + str(3) + ',' + str(5) + '}'
    substring = string[:10]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 6, len(substring) + 1)):
            window = substring[i:j]
            reversed_window = window[::-1]
            if window.lower() == reversed_window.lower():
                palindromes.add(window)
    return palindromes