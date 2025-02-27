from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    middle_char_candidates = sorted(set(s))
    palindromes = set()
    for char in middle_char_candidates:
        prefix, middle, suffix = (s.replace(char, ''), char, '')
        if len(prefix) + len(suffix) + 1 < 4:
            continue
        for l in range(2, min(4, len(prefix)) + 1):
            for perm in set(permutations(prefix, l)):
                palindrome_candidate = ''.join(perm) + middle + ''.join(reversed(perm))
                palindromes.add(palindrome_candidate)
    return set(filter(lambda p: len(p) >= 4, palindromes))