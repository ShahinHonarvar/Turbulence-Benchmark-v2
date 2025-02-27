from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:8].lower()
    all_chars = ''.join(substring)
    unique_palindromes = set()
    for comb in permutations(all_chars, 6):
        candidate = ''.join(comb)
        if candidate == candidate[::-1]:
            unique_palindromes.add(candidate)
    return unique_palindromes