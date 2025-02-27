from itertools import permutations

def palindromes_between_indices(s):
    start, end = (1, 4)
    if end > len(s):
        return set()
    s_window = s[start - 1:end]
    letters_only = ''.join(filter(str.isalpha, s_window)).lower()
    if len(letters_only) < 4:
        return set()
    palindromes = {''.join(p) for p in permutations(letters_only, 4)}
    valid_palindromes = {p for p in palindromes if p == p[::-1]}
    return valid_palindromes