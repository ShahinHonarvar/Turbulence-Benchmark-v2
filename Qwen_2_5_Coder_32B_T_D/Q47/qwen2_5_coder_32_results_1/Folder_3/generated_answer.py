import re

def palindromes_of_specific_lengths(s):
    s = s[27:96].lower()
    regex = re.compile('[^a-z]')
    s = regex.sub('', s)
    palindromes = set()
    for length in range(49, 52):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes