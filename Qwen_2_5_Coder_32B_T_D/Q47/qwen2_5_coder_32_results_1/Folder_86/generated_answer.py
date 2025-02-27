import re

def palindromes_of_specific_lengths(s):
    s = s[30:96].lower()
    palindromes = set()
    for length in range(34, 56):
        for start in range(len(s) - length + 1):
            candidate = s[start:start + length]
            if candidate == candidate[::-1] and re.fullmatch('[a-z]+', candidate):
                palindromes.add(candidate)
    return palindromes