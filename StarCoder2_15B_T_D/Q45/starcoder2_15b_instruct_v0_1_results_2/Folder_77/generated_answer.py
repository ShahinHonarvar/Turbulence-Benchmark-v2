import re

def palindromes_between_indices(string):
    pattern = '[a-zA-Z]'
    letters = re.findall(pattern, string)
    palindromes = set()
    for i in range(4, min(len(letters) - 3, 7)):
        for j in range(len(letters) - i + 1):
            s = ''.join(letters[j:j + i])
            if s.lower() == s[::-1].lower():
                palindromes.add(s)
    return palindromes