import re

def palindromes_of_specific_lengths(s):
    s = s[124:284].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(115, 135):
            if i + j <= len(s):
                substr = s[i:i + j]
                if re.fullmatch('[a-z]+', substr) and substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes