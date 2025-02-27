import re

def palindromes_between_indices(string):
    letters = re.findall('[a-z]', string.lower())
    palindromes = set()
    for i in range(3, 10):
        for j in range(i + 1, 10):
            palindromes.add(''.join(letters[i:j]))
    return {p for p in palindromes if len(p) >= 5 and p == p[::-1]}