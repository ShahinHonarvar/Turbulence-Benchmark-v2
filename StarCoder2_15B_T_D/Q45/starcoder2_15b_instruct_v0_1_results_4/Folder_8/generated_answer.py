import re

def palindromes_between_indices(s):
    pattern = re.compile('[a-z]', re.IGNORECASE)
    letters = pattern.findall(s)
    palindromes = set()
    for i in range(1, 6):
        for j in range(i + 1, len(letters) + 1):
            substring = ''.join(letters[i:j])
            reversed_substring = substring[::-1]
            if substring == reversed_substring and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes