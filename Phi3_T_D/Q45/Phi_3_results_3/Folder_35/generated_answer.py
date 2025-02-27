from itertools import permutations

def palindromes_between_indices(s):
    characters = s[2:5].lower()
    unique_chars = set(characters)
    valid_chars = {c for c in unique_chars if c.isalpha()}
    palindromes = {''.join(p) for c in valid_chars for p in permutations(valid_chars, len(valid_chars) // 2 + 1) * 2}
    result = {p for p in palindromes if len(p) >= 4}
    return result