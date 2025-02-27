from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:8].lower()
    unique_chars = set(sub_str)
    if len(unique_chars) < 5:
        return set()
    all_perms = set((''.join(p) for p in permutations(unique_chars, 5)))
    palindromes = set((p for p in all_perms if p == p[::-1]))
    return palindromes