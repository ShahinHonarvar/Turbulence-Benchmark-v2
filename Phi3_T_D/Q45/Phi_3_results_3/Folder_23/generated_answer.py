from itertools import permutations

def palindromes_between_indices(s):
    desired_chars = set(s[0:7].lower())
    four_char_palindromes = set()
    for c1, c2, c3, c4 in permutations('a' * len(desired_chars))[:len(desired_chars)]:
        candidate = ''.join((c1, c2, c3, c2, c1))
        if candidate in desired_chars:
            four_char_palindromes.add(candidate)
    return four_char_palindromes