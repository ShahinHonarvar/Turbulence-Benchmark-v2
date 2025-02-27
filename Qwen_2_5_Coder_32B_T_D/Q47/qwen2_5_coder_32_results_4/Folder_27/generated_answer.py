import re

def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    palindromes = set()
    for i in range(len(s) - 25):
        for j in range(26, 30):
            if i + j <= len(s):
                substring = s[i:i + j]
                if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes