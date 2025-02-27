import re

def palindromes_of_specific_lengths(s):
    s = s[16:61].lower()
    r = re.compile('[a-z]')
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 15, min(i + 40, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and len(r.findall(substring)) == len(substring):
                palindromes.add(substring)
    return palindromes