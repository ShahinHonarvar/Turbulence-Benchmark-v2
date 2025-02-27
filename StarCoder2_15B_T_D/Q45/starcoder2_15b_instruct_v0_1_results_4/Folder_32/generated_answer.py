import re

def palindromes_between_indices(s):
    pattern = '[a-zA-Z]'
    letters = re.findall(pattern, s)
    palindromes = set()
    for i in range(1, len(letters) - 6):
        for j in range(i + 5, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes