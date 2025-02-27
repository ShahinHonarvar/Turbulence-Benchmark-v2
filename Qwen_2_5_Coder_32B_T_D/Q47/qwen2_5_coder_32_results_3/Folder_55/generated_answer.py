import re

def palindromes_of_specific_lengths(s):
    s = s[10:76].lower()
    letters_only = re.compile('[^a-z]')
    palindromes = set()
    for i in range(len(s) - 9):
        for j in range(i + 9, min(i + 20, len(s))):
            substring = letters_only.sub('', s[i:j + 1])
            if substring and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes