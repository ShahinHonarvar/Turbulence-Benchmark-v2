import re

def palindromes_of_specific_lengths(s):
    s = s[31:92].lower()
    palindromes = set()
    for i in range(len(s) - 49):
        for length in range(50, 54):
            if i + length <= len(s):
                sub = s[i:i + length]
                if sub == sub[::-1] and re.fullmatch('[a-z]+', sub):
                    palindromes.add(sub)
    return palindromes