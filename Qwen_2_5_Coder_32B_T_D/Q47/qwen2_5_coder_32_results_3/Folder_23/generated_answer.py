import re

def palindromes_of_specific_lengths(s):
    s = s[23:95].lower()
    palindromes = set()
    for i in range(len(s)):
        for l in range(17, 56):
            if i + l <= len(s):
                substring = s[i:i + l]
                if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes