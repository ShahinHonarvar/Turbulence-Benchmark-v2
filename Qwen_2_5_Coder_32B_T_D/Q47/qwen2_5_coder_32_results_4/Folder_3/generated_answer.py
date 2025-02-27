import re

def palindromes_of_specific_lengths(s):
    s = s[27:96].lower()
    palindromes = set()
    for i in range(len(s) - 48):
        for l in range(49, 52):
            if i + l <= len(s):
                sub = s[i:i + l]
                if re.fullmatch('[a-z]+', sub) and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes