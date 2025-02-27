import re

def palindromes_of_specific_lengths(s):
    s = s[17:96].lower()
    regex = re.compile('[^a-z]')
    s = regex.sub('', s)
    palindromes = set()
    for start in range(len(s) - 12):
        for end in range(start + 12, min(start + 49, len(s)) + 1):
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes