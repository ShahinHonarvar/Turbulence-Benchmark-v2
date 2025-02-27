def palindromes_between_indices(s):
    letters = set([c.lower() for c in s[5:8]])
    palindromes = {letter * 4 for letter in letters}
    return set(filter(lambda p: p == p[::-1], palindromes))