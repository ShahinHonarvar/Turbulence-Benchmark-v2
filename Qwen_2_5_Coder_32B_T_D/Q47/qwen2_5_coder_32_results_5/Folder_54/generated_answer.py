import re

def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    palindromes = set()
    for i in range(len(s) - 17):
        for l in range(18, 20):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                    palindromes.add(sub)
    return palindromes