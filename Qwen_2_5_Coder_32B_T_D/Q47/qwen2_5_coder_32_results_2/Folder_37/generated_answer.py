import re

def palindromes_of_specific_lengths(s):
    s = s[:10].lower()
    pattern = re.compile('[a-z]')
    letters = ''.join(pattern.findall(s))
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(2, 5):
            if i + j <= len(letters):
                sub = letters[i:i + j]
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes