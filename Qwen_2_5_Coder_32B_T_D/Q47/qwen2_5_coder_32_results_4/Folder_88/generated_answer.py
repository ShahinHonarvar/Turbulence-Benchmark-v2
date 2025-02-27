import re

def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for length in range(4, 6):
            if i + length <= len(s):
                sub = s[i:i + length]
                if re.fullmatch('[a-z]+', sub) and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes