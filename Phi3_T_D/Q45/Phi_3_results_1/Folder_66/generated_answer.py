from itertools import permutations

def palindromes_between_indices(text):
    start, end = (0, 5)
    substring = text[start:end + 1].lower()
    letters = ''.join(filter(str.isalpha, substring))
    if len(letters) < 5:
        return set()
    all_perms = set((''.join(p) for p in permutations(letters, 5)))
    return {p for p in all_perms if p == p[::-1]}