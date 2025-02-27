import re

def palindromes_of_specific_lengths(s):
    s = s[15:95].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(18, 74):
            if i + j <= len(s):
                subs = s[i:i + j]
                if re.fullmatch('[a-z]+', subs) and subs == subs[::-1]:
                    palindromes.add(subs)
    return palindromes