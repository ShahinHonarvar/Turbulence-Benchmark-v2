import re

def palindromes_of_specific_lengths(s):
    s = s[15:96].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 20, min(i + 67, len(s) + 1)):
            substring = s[i:j]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes